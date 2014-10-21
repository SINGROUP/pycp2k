#! /usr/bin/env python

from pycp2k.cp2k import CP2K
from ase.lattice.cubic import Diamond

#===============================================================================
# Create the Si lattice here as an ASE Atoms object. We will use it later on to
# automatically create entries in the CP2K input. Here we use ASE specific
# function to do the job. One may also load any of the ase supported structure
# files by using ase.io.read() or use the ASE Atoms and Atom classes directly
# to create the structure.
lattice = Diamond(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                  symbol='Si',
                  latticeconstant=5.430697500,
                  size=(1, 1, 1))

#===============================================================================
# Setup directories and mpi parallelization. If you specify a working directory
# and a project name, the output and input file names and the
# GLOBAL.Project_name keyword are automatically generated for you. You can
# alternatively specify each separately. You can setup the cp2k command with
# calc.cp2k_command, and the mpi command with calc.mpi_command.  MPI can be
# turned on or off with calc.mpi_on (on by default). The -n flag can be setup
# with calc.mpi_n_processes. Any special flags can be specified by using
# calc.cp2k_flags or calc.mpi_flags. By default cp2k is run in the output
# directory, but you can change the working directory with
# calc.working_directory.
calc = CP2K()
calc.working_directory = "/home/lauri"
calc.project_name = "si_bulk"
calc.mpi_n_processes = 2

#===============================================================================
# Create shortcuts for the most used subtrees of the input. You don't have to
# specify these but they will make your life easier.
CP2K_INPUT = calc.CP2K_INPUT  # This is the root of the input tree
GLOBAL = CP2K_INPUT.GLOBAL
# Repeatable sections are added with X_add() function. Optionally you can
# provide the Section_parameter as an argument to this function.
FORCE_EVAL = CP2K_INPUT.FORCE_EVAL_add()
SUBSYS = FORCE_EVAL.SUBSYS
DFT = FORCE_EVAL.DFT
SCF = DFT.SCF

#===============================================================================
# Fill input tree. Section names are in upper case, keywords are capitalized.
# Most IDEs will be able to automatically suggest the entries as you begin
# typing them. Relevant parts of the documentation have been copied to
# parsedclasses.py and some IDEs provide quick access to them (e.g. in spyder
# you can search documentation for keyword with the command "go to definition"

# The keywords can entered as any python type that converts to string (int,
# float, etc.). Additionally you can provide non-repeatable keywords as lists.
# In that case the each list element is converted to string, separated with
# white space and printed into input file. Repeatable keywords can also be
# defined as lists, but in this case each list item corresponds to a new
# repeated item. For an example of these features see examples/example_qmmm.py.
GLOBAL.Run_type = "ENERGY_FORCE"
GLOBAL.Print_level = "LOW"

# These utility functions will create entries to the input tree from the ASE
# Atoms object created earlier. As arguments you should give the subsys where
# the entries should be created and the Atoms object from which they are
# exctracted.
calc.create_cell(SUBSYS, lattice)
calc.create_coord(SUBSYS, lattice)

FORCE_EVAL.Method = "Quickstep"
FORCE_EVAL.PRINT.FORCES.Section_parameters = "ON"
DFT.Basis_set_file_name = "BASIS_SET"
DFT.Potential_file_name = "GTH_POTENTIALS"
DFT.QS.Eps_default = 1.0E-10
DFT.MGRID.Ngrids = 4
DFT.MGRID.Cutoff = 300
DFT.MGRID.Rel_cutoff = 60
DFT.XC.XC_FUNCTIONAL.Section_parameters = "PADE"
SCF.Scf_guess = "ATOMIC"
SCF.Eps_scf = 1.0E-7
SCF.Max_scf = 300
SCF.DIAGONALIZATION.Section_parameters = "ON"
SCF.DIAGONALIZATION.Algorithm = "STANDARD"
SCF.MIXING.Section_parameters = "T"
SCF.MIXING.Method = "BROYDEN_MIXING"
SCF.MIXING.Alpha = 0.4
SCF.MIXING.Nbroyden = 8
FORCE_EVAL.PRINT.FORCES.Section_parameters = "ON"

KIND = SUBSYS.KIND_add("Si")  # Section_parameters can be provided as argument.
KIND.Element = "Si"
KIND.Basis_set = "DZVP-GTH-PADE"
KIND.Potential = "GTH-PADE-q4"

#===============================================================================
# After you have created your simulation you can choose how to run it.
# Typically there are three options:

# 1. Only write the input file. CP2K is then run manually or with some other
# script.
#calc.write_input_file()

# 2. Write the input file and run CP2K as a subprocess in python.
#calc.run()

# 3. Write the input file, run CP2K as a subprocess and fetch results from the output file.
print calc.get_potential_energy()
#print calc.get_forces()
