#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""This module defines an ASE calculator interface to CP2K."""

from pycp2k.parsedclasses import _CP2K_INPUT1
from ase.calculators.interface import Calculator
from subprocess import call
from pycp2k.utilities import print_title, print_message, print_warning
import re
import pycp2k.config
import numpy as np
import os
import pipes


#===============================================================================
class CP2K(Calculator, object):
    """Class for doing CP2K calculations.

    This class is an ASE compatible calculator interface for CP2K. You use it
    to create an input file for CP2K in a pythonic object-oriented way. The
    advantages of this are:
        -Access to ASE's structure creation tools
        -ASE input/output
        -Script multiple runs with python
        -Automatic syntax correctness for the input file
        -Code completion if provided by your python IDE
        -Quick access to documentation if provided by your IDE

    Attributes:
        CP2K_INPUT: pycp2k.parsedclasses._CP2K_INPUT1
            The root of the input tree
        input_path: string
            Path where the input file is stored
        output_path: string
            Path where the output file is stored
        output_path: string
            Path in which CP2K is executed. Defaults to the output path
            directory.
        cp2k_command: string
            The command with which CP2K is called
        cp2k_flags: dict
            Contains any additional cp2k executable flags
        mpi_on: bool
            Whether MPI parallellization should be used
        mpi_flags: dict
            Contains any additional MPI executable flags
        mpi_command: string
            The name of MPI command
        old_input: string
            The input file for the last CP2K run
        new_input: string
            The input file for a new CP2K run
        output: string
            The output of the last CP2K run
    """
    def __init__(self, input_path=None, output_path=None):
        """Construct CP2K-calculator object."""
        self.CP2K_INPUT = _CP2K_INPUT1()
        self.input_path = input_path
        self.output_path = output_path
        self.working_directory = None
        self._project_name = None
        self.cp2k_command = pycp2k.config.cp2k_default_command
        self.cp2k_flags = {}
        self.mpi_on = True
        self.mpi_flags = {}
        self.mpi_n_processes = None
        self.mpi_command = pycp2k.config.mpi_default_command
        self.old_input = None
        self.new_input = None
        self.output = None

    @property
    def project_name(self):
        """Property for project name. Properties need new-style classes to work
        so the class inherits object as well.
        """
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        """Setter for project name. Sets up the Project name in input tree."""
        self._project_name = value
        self.CP2K_INPUT.GLOBAL.Project_name = value

    def set_input_path(self, input_path):
        """Set the path where the input is located."""
        self.input_path = input_path

    def set_output_path(self, output_path):
        """Set the path where all the output is stored."""
        self.output_path = output_path

    def calculation_required(self, atoms=None, quantities=None):
        """Check if a calculation is required.

        Available quantitites: forces, energy

        This method is used to check if a quantity is available without further
        calculations. For unknown/unsupported quantities this returns true,
        indicating that the quantity is not available.

        Because it is very hard to know what parameters affect the calculation
        of different quantities (energy, forces, etc.), this function simply
        checks that has the input file changed since last evaluation.
        """
        available_quantities = ["energy", "forces"]
        for quantity in quantities:
            if quantity not in available_quantities:
                print_warning("Quantity '" + quantity + "' not available.")
                return True

        if self.old_input is None:
            return True
        else:
            new_input = self.CP2K_INPUT.print_input(-1)
            return new_input != self.old_input

    def get_forces(self, atoms=None):
        """Return the forces."""
        if self.calculation_required(quantities=["forces"]):
            self.run()

        force_matches = re.findall(r"ATOMIC FORCES in.*\n\n.*\n((?:\s{6}.*\n)*) SUM OF ATOMIC FORCES", self.output)
        if len(force_matches) != 0:
            if len(force_matches) > 1:
                print_warning("More than one 'ATOMIC FORCES' entries were found in the output file. Probably due to the fact that outputs are appended to the same file. The last entry is returned.")
        else:
            raise Exception("'ATOMIC FORCES' entry was not found in the CP2K output file. Please make sure that you have the correct 'GLOBAL.Run_type'")

        # Parse the force string
        force_string = force_matches[-1]
        lines = force_string.splitlines()
        forces = np.zeros([len(lines), 3])
        for i, line in enumerate(lines):
            words = line.split()
            z = float(words[-1])
            y = float(words[-2])
            x = float(words[-3])
            forces[i, 0] = x
            forces[i, 1] = y
            forces[i, 2] = z

        return forces

    def get_potential_energy(self, atoms=None, force_consistent=False):
        """Return total energy.

        Only the energy extrapolated to zero Kelvin is currently supported.
        """
        if force_consistent:
            print_warning("Fetching the energy consistent with the forces (the free energy) is not implemented yet.")
            return None

        if self.calculation_required(quantities=["energy"]):
            self.run()

        energy = re.findall(r"ENERGY\|.*:\s*([-+]?\d*\.\d+|\d+)", self.output)
        if len(energy) != 0:
            if len(energy) > 1:
                print_warning("More than one 'ENERGY' entries were found in the output file. Probably due to the fact that outputs are appended to the same file. The last entry is returned.")
            return float(energy[-1])
        else:
            raise Exception("'ENERGY' entry was not found in the CP2K output file. Please make sure that you have the correct 'GLOBAL.Run_type'")

    def get_stress(self, atoms):
        """Return the stress."""

    def create_cell(self, subsys, atoms):
        """Creates the cell for a SUBSYS from an ASE Atoms object.

        Creates the cell unit vectors and replicates the periodic boundary
        conditions. Notice that this doesn't affect the PBCs used for
        electrostatics! (use create_poisson_periodicity())

        args:
            subsys: pycp2k.parsedclasses._subsys1
                The SUBSYS for which the cell is created.
            atoms: ASE Atoms
                The ASE Atoms object from which the cell is extracted.
        """
        cell = atoms.get_cell()
        A = cell[0, :]
        B = cell[1, :]
        C = cell[2, :]
        subsys.CELL.A = str(A[0]) + " " + str(A[1]) + " " + str(A[2])
        subsys.CELL.B = str(B[0]) + " " + str(B[1]) + " " + str(B[2])
        subsys.CELL.C = str(C[0]) + " " + str(C[1]) + " " + str(C[2])

        pbc = atoms.get_pbc()
        if not any(pbc):
            subsys.CELL.Periodic = "NONE"
        else:
            subsys.CELL.Periodic = pbc[0]*"X" + pbc[1]*"Y" + pbc[2]*"Z"

    def create_coord(self, subsys, atoms):
        """Creates the atomic coordinates for a SUBSYS from an ASE Atoms object.

        args:
            subsys: The SUBSYS for which the coordinates are created.
            atoms: The ASE Atoms object from which the coordinates are extracted.
        """
        atom_list = []
        for atom in atoms:
            atom_list.append([atom.symbol, atom.position[0], atom.position[1], atom.position[2]])
        subsys.COORD.Default_keyword = atom_list

    def create_poisson_periodicity(self, poisson, atoms):
        """Creates the poisson periodicity for a POISSON section from an ASE
        Atoms object.

        args:
            poisson: POISSON section
                The poisson section from DFT or MM for which the periodicity is
                created.
            atoms: ASE Atoms object
                The atoms from which the periodicity is extracted.
        """
        pbc = atoms.get_pbc()
        if not any(pbc):
            poisson.Periodic = "NONE"
        else:
            poisson.Periodic = pbc[0]*"X" + pbc[1]*"Y" + pbc[2]*"Z"

    def create_constraints(self, subsys, atoms):
        """Creates contraints for the the given SUBSYS from the given ASE Atoms object.

        args:
            subsys: The SUBSYS for which the contraints apply.
            atoms: The ASE Atoms object from which the contraints are extracted.
        """
        pass

    def write_input_file(self):
        """Creates an input file for CP2K executable from the object tree
        defined in CP2K_INPUT
        """
        self.old_input = self.new_input
        self.new_input = self.CP2K_INPUT.print_input(-1)

        # Write the file
        with open(self.get_input_path(), 'w') as input_file:
            input_file.write(self.new_input)

    def read_input_file(self, file_name):
        """Reads an existing CP2K input file and creates the corresponding
        object tree from it"""

        # Open the file
        with open(self.file_name, 'r') as input_file:
            pass

    def get_input_path(self):
        """Determine input file path."""
        if self.input_path is not None:
            return self.input_path
        else:
            return self.working_directory + "/" + self.project_name + ".inp"

    def get_output_path(self):
        """Determine output file path."""
        if self.output_path is not None:
            return self.output_path
        else:
            return self.working_directory + "/" + self.project_name + ".out"

    def run(self, print_input=False, print_output=False):
        """Runs the input script."""

        self.write_input_file()
        command_list = []

        # MPI command and flags
        if self.mpi_on:
            command_list.append(self.mpi_command)
            if self.mpi_n_processes is not None:
                self.mpi_flags["-n"] = self.mpi_n_processes
            for flag, value in self.mpi_flags.iteritems():
                command_list.append(str(flag))
                command_list.append(str(value))

        # CP2K command and flags
        self.cp2k_flags["-o"] = self.get_output_path()
        self.cp2k_flags["-i"] = self.get_input_path()

        command_list.append(self.cp2k_command)
        for flag, value in self.cp2k_flags.iteritems():
            command_list.append(str(flag))
            command_list.append(str(value))

        # When shell=True the command is passed as string rather than a
        # sequence as instructed in subprocess documentation.
        command_string = " ".join(command_list)

        print_message("CP2K START", "Calculation started with command " + command_string)
        if print_input:
            print_title("CP2K INPUT")
            print self.input

        # Run in the output directory by default, can be changed with working_directory
        if self.working_directory is None:
            working_directory = os.path.dirname(self.output_path)
        else:
            working_directory = self.working_directory

        # Call the subprocess. shell=True is used to access srun and
        # environment variable expansions.
        call(command_string, shell=True, cwd=working_directory)

        # Open the output file
        with open(self.get_output_path(), 'r') as output_file:
            self.output = output_file.read()

        if print_output:
            print_title("CP2K OUTPUT")
            print self.output
