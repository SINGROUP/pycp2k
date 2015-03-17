#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""This module defines an ASE calculator interface to CP2K."""

from pycp2k.parsedclasses import _CP2K_INPUT1
from pycp2k.utilities import print_title, print_text, print_warning, print_error
import pycp2k.config
from ase.calculators.interface import Calculator
from subprocess import call, check_output, CalledProcessError
import re
import numpy as np
import os
from ase.constraints import FixAtoms
import time


#===============================================================================
class CP2K(Calculator, object):
    """Class for creating and running CP2K calculations.

    This is the main class of the pycp2k package. You use it to create an input
    for CP2K in a pythonic object-oriented way and you can also directly run
    cp2k with the input.

    The advantages of doing CP2K calculations with PYCP2K are:

        -Use python data structures and algorithms to create and modify the
         input
        -Create and run CP2K simulations with one python script.
        -Structure creation and loading with ASE
        -Autocompletion if provided by your IDE
        -Built-in documentation for all keywords and sections.
        -Use additional python libraries (numpy, scipy, matplotlib, etc.) to
         also analyze the results - all with python.

    Attributes:
        CP2K_INPUT: pycp2k.parsedclasses._CP2K_INPUT1
            The root of the input tree
        input_path: string
            Path where the input file is stored
        output_path: string
            Path where the output file is stored
        working_directory: string
            Path in which CP2K is executed. Defaults to the output path
            directory if not specified.
        project_name: string
            If given, this attribute together with working_directory is used
            for naming the input and output files. Also sets the
            GLOBAL.Project_name.
        cp2k_command: string
            The command with which CP2K is called
        cp2k_flags: dict
            Contains any additional cp2k executable flags. Usage:
            cp2k_flags.append("--xml")
        mpi_on: bool
            Whether MPI parallellization should be used
        mpi_flags: dict
            Contains any additional MPI executable flags. Usage:
            mpi_flags.append("-debug")
        mpi_command: string
            The name of MPI command
        mpi_n_processes: int
            The number of processes used by MPI
        old_input: string
            The input file for the latest succesful CP2K run
        new_input: string
            The input file for a new CP2K run
        output: string
            The output of the last CP2K run
    """
    def __init__(self, atoms=None, input_path=None, output_path=None):
        """Construct CP2K-calculator object."""
        self.CP2K_INPUT = _CP2K_INPUT1()
        self.input_path = input_path
        self.output_path = output_path
        self.working_directory = None
        self._project_name = None
        self.cp2k_command = pycp2k.config.cp2k_default_command
        self.cp2k_flags = []
        self.mpi_on = True
        self.mpi_flags = []
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

    def calculation_required(self, atoms=None, quantities=None):
        """Check if a calculation is required.

        Available quantitites: forces, energy

        This method is used to check if a quantity is available without further
        calculations. For unknown/unsupported quantities this returns true,
        indicating that the quantity is not available.

        Because it is very hard to know what parameters affect the calculation
        of different quantities (energy, forces, etc.), this function simply
        checks that has the input file changed since last evaluation.

        args:
            quantitities: list of strings
                The names of the required quantitities.
        """
        available_quantities = ["energy", "forces"]
        for quantity in quantities:
            if quantity not in available_quantities:
                print_warning("Quantity '{}' not available.".format(quantity))
                return True

        if self.old_input is None:
            return True
        else:
            new_input = self.CP2K_INPUT._print_input(-1)
            return new_input != self.old_input

    def get_forces(self, atoms=None):
        """Return the forces.

        Returns a numpy array of 3D forces for each atom in the same order in
        which atoms have been defined.
        """
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

    def create_cell(self, subsys, atoms):
        """Creates the cell for a SUBSYS from an ASE Atoms object.

        Creates the cell unit vectors and replicates the periodic boundary
        conditions. Notice that this doesn't affect the PBCs used for
        electrostatics! (use create_poisson())

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
        subsys.CELL.A = A.tolist()
        subsys.CELL.B = B.tolist()
        subsys.CELL.C = C.tolist()

        pbc = atoms.get_pbc()
        if sum(pbc) == 0:
            subsys.CELL.Periodic = "NONE"
        else:
            subsys.CELL.Periodic = pbc[0]*"X" + pbc[1]*"Y" + pbc[2]*"Z"

    def create_coord(self, subsys, atoms, molnames=None):
        """Creates the atomic coordinates for a SUBSYS from an ASE Atoms object.

        args:
            subsys: pycp2k.parsedclasses._subsys1
                The SUBSYS for which the coordinates are created.
            atoms: ASE Atoms
                Atoms from which the coordinates are extracted.
            molnames: list of strings
                The MOLNAME for each atom in correct order
        """
        atom_list = []
        for i_atom, atom in enumerate(atoms):
            new_atom = [atom.symbol, atom.position[0], atom.position[1], atom.position[2]]
            if molnames is not None:
                new_atom.append(molnames[i_atom])
            atom_list.append(new_atom)
        subsys.COORD.Default_keyword = atom_list

    def create_poisson(self, poisson, atoms):
        """Creates the periodicity for a POISSON section and tries to guess a
        good solver.

        args:
            poisson: pycp2k.parsedclasses._poisson1
                The poisson section from DFT or MM for which the periodicity is
                created.
            atoms: ASE Atoms
                The atoms from which the periodicity is extracted.
        """
        # Define periodicity
        pbc = atoms.get_pbc()
        if sum(pbc) == 0:
            poisson.Periodic = "NONE"
        else:
            poisson.Periodic = pbc[0]*"X" + pbc[1]*"Y" + pbc[2]*"Z"

    def create_fixed_atoms(self, subsys, atoms):
        """Creates the constraints corresponding to ASE's FixAtoms class.

        The way constraints are defined in ASE and CP2K are very different.
        Only few special cases have a 1-to-1 mapping between them and thus most
        CP2K constraints cannot be created from ASE constraints. FixAtoms is
        one of the special cases.

        args:
            subsys: pycp2k.parsedclasses._subsys1
                The SUBSYS for which the contraint applies.
            atoms: ASE Atoms
                Atoms from which the FixAtom contraint is extracted.
        """
        CONSTRAINT = self.CP2K_INPUT.MOTION.CONSTRAINT
        constraints = atoms._constraints
        n_constraints = 0
        if type(constraints) is not list:
            constraints = [constraints]
        for constraint in constraints:
            # FixAtoms -> CONSTRAINT.FIXED_ATOMS
            n_constraints += 1
            if isinstance(constraint, FixAtoms):
                if len(constraint.index) == len(atoms) and all(i <= 1 for i in constraint.index):
                    indices = np.where(constraint.index)[0]
                else:
                    indices = constraint.index
                # CP2K indexing starts at 1
                indices = [x+1 for x in indices]
                fixed_atoms = CONSTRAINT.FIXED_ATOMS_add()
                fixed_atoms.Components_to_fix = "XYZ"
                fixed_atoms.List = " ".join(map(str, indices))
        if n_constraints == 0:
            print_warning("No 'FixAtoms' constraints found.")

    def write_input_file(self):
        """Creates an input file for CP2K executable from the object tree
        defined in CP2K_INPUT.
        """
        self.old_input = self.new_input
        self.new_input = self.CP2K_INPUT._print_input(-1)

        # Write the file
        with open(self.get_input_path(), 'w') as input_file:
            input_file.write(self.new_input)

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

        print_title("PYCP2K RUN STARTED")

        # Run in the output directory by default, can be changed with working_directory
        if self.working_directory is None:
            working_directory = os.path.dirname(self.output_path)
        else:
            working_directory = self.working_directory

        # Check that the cp2k version is correct
        print_text(">> CP2K version check...")
        command_for_version_check = " ".join([self.cp2k_command, "-v "])
        version_result = check_output(command_for_version_check, shell=True, cwd=working_directory)
        result_lines = version_result.splitlines()
        run_version = result_lines[0].rsplit(None, 1)[2]
        run_revision = result_lines[1].rsplit(None, 1)[-1]
        build_version = pycp2k.config.build_version
        build_revision = pycp2k.config.build_revision

        if run_version != build_version:
            print_warning("The CP2K version does not match the version for which PYCP2K was configured. This will affect the availability of keywords and sections in the input tree!")
        elif run_revision != build_revision:
            print_warning("The CP2K revision does not match the version for which PYCP2K was configured. This will affect the availability of keywords and sections in the input tree!")

        # Write input file and possibly show it
        print_text(">> Creating CP2K input file...")
        self.write_input_file()
        if print_input:
            print_text(">> CP2K input file:")
            print self.input

        command_list = []

        # MPI command and flags
        if self.mpi_on:
            command_list.append(self.mpi_command)
            if self.mpi_n_processes is not None:
                command_list.append("-n " + str(self.mpi_n_processes))
            for flag in self.mpi_flags:
                command_list.append(str(flag))

        # CP2K command and flags
        command_list.append(self.cp2k_command)
        command_list.append("-o " + str(self.get_output_path()))
        command_list.append("-i " + str(self.get_input_path()))
        for flag in self.cp2k_flags:
            command_list.append(str(flag))

        # When shell=True the command is passed as string rather than a
        # sequence as instructed in subprocess documentation.
        command_string = " ".join(command_list)

        # Perform syntax check
        print_text(">> Performing syntax check on input file...")
        command_for_syntax_check = " ".join([self.cp2k_command, "-i " + str(self.get_input_path()), "--check"])
        syntax_result = check_output(command_for_syntax_check, shell=True, cwd=working_directory)
        if syntax_result[0:7] != "SUCCESS":
            print_error("Syntax error in the input file. See the following output for further details.")
            print syntax_result
            raise Exception

        # Call the subprocess. shell=True is used to access srun and
        # environment variable expansions.
        print_text(">> Running CP2K:")
        print_text("   -CP2K version: {}".format(run_version))
        print_text("   -CP2K revision: {}".format(run_revision))
        print_text("   -CP2K command: {}".format(os.path.basename(self.cp2k_command)))
        if self.mpi_on:
            print_text("   -MPI command: {}".format(self.mpi_command))
            print_text("   -Processes: {}".format(self.mpi_n_processes))
        start = time.time()
        try:
            check_output(command_string, shell=True, cwd=working_directory)
        except CalledProcessError:
            error_output_path = self.get_output_path()
            print_error("Error occured during CP2K calculation. See the output from {} for further details.".format(error_output_path))
            raise
        end = time.time()
        elapsed = end - start
        m, s = divmod(elapsed, 60)
        h, m = divmod(m, 60)
        print_text(">> CP2K calculation finished succesfully!")
        print_text(">> Elapsed time: {:.0f}h:{:.0f}m:{:.0f}s".format(h, m, s))

        # Open the output file
        with open(self.get_output_path(), 'r') as output_file:
            self.output = output_file.read()

        if print_output:
            print_text(">> CP2K output file:")
            print self.output

        print_title("PYCP2K RUN FINISHED")

    def vmd_view_trajectory(self):
        """View the MD trajectory with VMD.

        Opens a blocking vmd window and loads the .xyz file created from MD
        simulation.
        """
        # Run in the output directory by default, can be changed with working_directory
        if self.working_directory is None:
            working_directory = os.path.dirname(self.output_path)
        else:
            working_directory = self.working_directory

        # Determine the file format
        file_format = None
        for print_section in self.CP2K_INPUT.MOTION.PRINT_list:
            file_format = print_section.TRAJECTORY.Format
            if file_format is not None:
                break

        if file_format is None or file_format == "XYZ" or file_format == "XMOL":
            file_suffix = ".xyz"
        elif file_format == "PDB":
            file_suffix = ".pdb"
        elif file_format == "DCD":
            file_suffix = ".dcd"
        else:
            print_warning("Cannot open the file format {} directly with VMD.".format(file_format))
            return

        filename = working_directory + "/" + self.CP2K_INPUT.GLOBAL.Project_name + "-pos-1" + file_suffix
        command = "vmd " + filename
        # Call the subprocess. shell=True is used to access srun and
        # environment variable expansions.
        call(command, shell=True, cwd=working_directory)
