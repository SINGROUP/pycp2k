#! /usr/bin/env python
# -*- coding: utf-8 -*-
from pycp2k.classes._CP2K_INPUT1 import _CP2K_INPUT1
from pycp2k.utilities import print_title, print_text, print_warning, print_error
from pycp2k.inputparser import CP2KInputParser
import pycp2k.config
from subprocess import call, check_output, CalledProcessError
import re
import os
import time


class CP2K(object):
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
    def __init__(self, working_directory=None, input_path=None, output_path=None, project_name=None):
        """
        Args:
            working_directory (str): The path where all the output and input
                files will be stored in.
            input_path (str): The path where the input file will be stored in.
                Overrides working_directory.
            output_path (str): The path where the output file will be saved.
                Overrides working_directory.
            project_name (str): The name of the project. Will be placed in
                CP2K.GLOBAL.PROJECT_NAME
        """
        self.CP2K_INPUT = _CP2K_INPUT1()
        self._input_path = input_path
        self._output_path = output_path
        self.working_directory = working_directory
        self.project_name = project_name
        self.cp2k_command = pycp2k.config.cp2k_default_command
        self.cp2k_flags = []
        self.mpi_on = pycp2k.config.mpi_on_default
        self.mpi_flags = []
        self.mpi_n_processes = None
        self.mpi_command = pycp2k.config.mpi_default_command
        self.old_input = None
        self.new_input = None

    def parse(self, filepath):
        """Parses an existing CP2K input file into this object. Will overwrite
        things in the current object tree.

        Args:
            filepath(str): Path to a CP2K input file. The input file should be
            compatible with the CP2K version specified when installing pycp2k.
        """
        inputparser = CP2KInputParser()
        inputparser.parse(self, filepath)

    @property
    def output_path(self):
        if self._output_path is not None:
            return self._output_path
        else:
            return self.working_directory + "/" + self.project_name + ".out"

    @output_path.setter
    def output_path(self, x):
        self._output_path = x

    @property
    def input_path(self):
        if self._input_path is not None:
            return self._input_path
        else:
            return self.working_directory + "/" + self.project_name + ".inp"

    @input_path.setter
    def input_path(self, x):
        self._input_path = x

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
        periodicity = []
        if pbc[0]:
            periodicity.append("X")
        if pbc[1]:
            periodicity.append("Y")
        if pbc[2]:
            periodicity.append("Z")
        if len(periodicity) == 0:
            subsys.CELL.Periodic = "NONE"
        else:
            subsys.CELL.Periodic = "".join(periodicity)

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

    def write_input_file(self, filepath=None):
        """Creates an input file for CP2K executable from the object tree
        defined in CP2K_INPUT.

        Args:
            filepath(str): The filepath of where the input file will be written
                to.
        """
        if filepath is None:
            filepath = self.input_path

        # Write the file
        with open(filepath, 'w') as input_file:
            input_file.write(self.get_input_string())

    def get_input_string(self):
        """Creates an input file for CP2K executable from the object tree
        defined in CP2K_INPUT.
        """
        input_string = self.CP2K_INPUT._print_input(-1)
        return input_string

    def run(self, print_input=False):
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
        run_version = result_lines[0].split()[2].decode()
        run_revision = result_lines[1].split()[-1].decode()
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
            print(self.input)

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
        command_list.append("-o " + str(self.output_path))
        command_list.append("-i " + str(self.input_path))
        for flag in self.cp2k_flags:
            command_list.append(str(flag))

        # When shell=True the command is passed as string rather than a
        # sequence as instructed in subprocess documentation.
        command_string = " ".join(command_list)

        # Perform syntax check
        print_text(">> Performing syntax check on input file...")
        command_for_syntax_check = " ".join([self.cp2k_command, "-i " + str(self.input_path), "--check"])
        syntax_result = (check_output(command_for_syntax_check, shell=True, cwd=working_directory)).decode("utf-8")
        success_regex = re.compile("^SUCCESS", re.MULTILINE)
        match = success_regex.search(syntax_result)
        if match is None:
            print_error("Syntax error in the input file. See the following output for further details.")
            print(syntax_result)
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
            error_output_path = self.output_path
            print_error("Error occured during CP2K calculation. See the output from {} for further details.".format(error_output_path))
            raise
        end = time.time()
        elapsed = end - start
        m, s = divmod(elapsed, 60)
        h, m = divmod(m, 60)
        print_text(">> CP2K calculation finished succesfully!")
        print_text(">> Elapsed time: {:.0f}h:{:.0f}m:{:.0f}s".format(h, m, s))

        # Save this input to old_input
        self.old_input = self.CP2K_INPUT._print_input(-1)

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
