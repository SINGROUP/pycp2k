#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""This module defines an ASE calculator interface to CP2K."""

from pycp2k.parsedclasses import _CP2K_INPUT1
from ase.calculators.interface import Calculator
from subprocess import call
from pycp2k.utilities import print_title, print_message, print_warning
import re


#===============================================================================
class CP2K(Calculator):
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

    """
    def __init__(self, input_path=None, output_path=None):
        """Construct CP2K-calculator object."""
        self.CP2K_INPUT = _CP2K_INPUT1()
        self.input_path = input_path
        self.output_path = output_path
        self.cp2k_command = "cp2k.popt"
        self.cp2k_flags = {}
        self.mpi_on = True
        self.mpi_flags = {}
        self.mpi_n_processes = None
        self.mpi_command = "mpirun"
        self.old_input = None
        self.new_input = None
        self.output = None

    def __del__(self):
        """Destructor"""

    def set_input_path(self, input_path):
        """Set the path where the input is located."""
        self.input_path = input_path

    def set_output_path(self, output_path):
        """Set the path where all the output is stored."""
        self.output_path = output_path

    def calculation_required(self, atoms=None, quantities=None):
        """Check if a calculation is required.

        Check if the quantities in the quantities list have already been calculated
        for the atomic configuration atoms. The quantities can be one or more of:
        ‘energy’, ‘forces’, ‘stress’, ‘charges’ and ‘magmoms’.

        This method is used to check if a quantity is available without further
        calculations. For this reason, calculators should react to
        unknown/unsupported quantities by returning True, indicating that the
        quantity is not available.
        """
        return self.new_input != self.old_input

    def get_forces(self, atoms):
        """Return the forces."""

    def get_potential_energy(self, atoms=None, force_consistent=False):
        """Return total energy.

        Both the energy extrapolated to zero Kelvin and the energy consistent with
        the forces (the free energy) can be returned.
        """
        self.write_input_file()
        if self.calculation_required():
            self.run(create_input=False)

        energy = re.findall(r"ENERGY\|.*:\s*([-+]?\d*\.\d+|\d+)", self.output)
        if len(energy) != 0:
            if len(energy) > 1:
                print_warning("More than one ENERGY entries were found in the output file. Probably due to the fact that outputs are appended to the same file. The last entry is returned.")
            return float(energy[len(energy)-1])
        else:
            raise Exception("ENERGY entry was not found in the CP2K output file. Please make sure that you have the correct GLOBAL.Run_type")

    def get_stress(self, atoms):
        """Return the stress."""

    def create_cell(self, subsys, atoms):
        """Creates the cell for a SUBSYS from an ASE Atoms object.

        args:
            subsys: The SUBSYS for which the cell are created.
            atoms: The ASE Atoms object from which the cell is extracted.
        """
        cell = atoms.get_cell()
        A = cell[0, :]
        B = cell[1, :]
        C = cell[2, :]
        subsys.CELL.A = " " + str(A[0]) + " " + str(A[1]) + " " + str(A[2])
        subsys.CELL.B = " " + str(B[0]) + " " + str(B[1]) + " " + str(B[2])
        subsys.CELL.C = " " + str(C[0]) + " " + str(C[1]) + " " + str(C[2])

    def create_coord(self, subsys, atoms):
        """Creates the atomic coordinates for a SUBSYS from an ASE Atoms object.

        args:
            subsys: The SUBSYS for which the coordinates are created.
            atoms: The ASE Atoms object from which the coordinates are extracted.
        """
        for atom in atoms:
            subsys.COORD.add_Default_keyword(atom.symbol + " " + str(atom.position[0]) + " " + str(atom.position[1]) + " " + str(atom.position[2]))

    def write_input_file(self):
        """Creates an input file for CP2K executable from the object tree
        defined in CP2K_INPUT
        """
        self.old_input = self.new_input
        self.new_input = self.CP2K_INPUT.print_input(-1)

        # Write the file
        with open(self.input_path, 'w') as input_file:
            input_file.write(self.new_input)

    def read_input_file(self, file_name):
        """Reads an existing CP2K input file and creates the corresponding
        object tree from it"""

        # Open the file
        with open(self.file_name, 'r') as input_file:
            pass

    def run(self, print_input=False, print_output=False, create_input=True):
        """Runs the input script."""
        if create_input:
            self.write_input_file()

        command_list = []

        # MPI command and flags
        if self.mpi_on:
            command_list.append(self.mpi_command)
            self.mpi_flags["-n"] = self.mpi_n_processes
            for flag, value in self.mpi_flags.iteritems():
                command_list.append(str(flag))
                command_list.append(str(value))

        # CP2K command and flags
        self.cp2k_flags["-o"] = self.output_path
        self.cp2k_flags["-i"] = self.input_path

        command_list.append(self.cp2k_command)
        for flag, value in self.cp2k_flags.iteritems():
            command_list.append(str(flag))
            command_list.append(str(value))

        print_message("CP2K START", "Calculation started with command " + " ".join(command_list))
        if print_input:
            print_title("CP2K INPUT")
            print self.input
        call(command_list, shell=False)

        # Open the output file
        with open(self.output_path, 'r') as output_file:
            self.output = output_file.read()

        if print_output:
            print_title("CP2K OUTPUT")
            print self.output
