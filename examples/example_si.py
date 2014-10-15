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
# Setup directories and mpi. You can setup the cp2k command (cp2k by default)
# with calc.cp2k_command, and the mpi command (mpirun by default) with
# calc.mpi_command. The input/output flag for cp2k is automatically set by
# specifying calc.input_path/calc.output_path. MPI can be turned on or off with
# calc.mpi_on (on by default). The -n flag can be setup with
# calc.mpi_n_processes. Any special flags can be specified by using
# calc.cp2k_flags or calc.mpi_flags.
calc = CP2K()
script_path = "/home/lauri"
project_name = "Si_bulk"
calc.input_path = script_path + "/" + project_name + ".inp"
calc.output_path = script_path + "/" + project_name + ".out"
calc.mpi_n_processes = 2

#===============================================================================
# Create shortcuts for the most used subtrees of the input. You don't have to
# specify these but they will make your life easier.
CP2K_INPUT = calc.CP2K_INPUT  # This is the root of the input tree
GLOBAL = CP2K_INPUT.GLOBAL
FORCE_EVAL = CP2K_INPUT.FORCE_EVAL_add()  # Repeatable items X are added with X_add() function
SUBSYS = FORCE_EVAL.SUBSYS
DFT = FORCE_EVAL.DFT
SCF = DFT.SCF

#===============================================================================
# Fill input tree. Section names are in upper case, keywords are capitalized.
# Most IDEs will be able to automatically suggest the entries as you begin
# typing them. Relevant parts of the documentation have been copied to
# parsedclasses.py and some IDEs provide quick access to them (e.g. in spyder
# you can search documentation for keyword with the command "go to definition".
GLOBAL.Run_type = "ENERGY_FORCE"
GLOBAL.Project = "Si_bulk8"
GLOBAL.Print_level = "LOW"

# These utility functions will create entries to the input tree from the ASE
# Atoms object created earlier. As arguments you should give the subsys where
# the entries should be created and the Atoms object from which they are
# exctracted.
calc.create_cell(SUBSYS, lattice)
calc.create_coord(SUBSYS, lattice)

FORCE_EVAL.Method = "Quickstep"
FORCE_EVAL.PRINT.FORCES.Section_parameters = "ON"
DFT.Basis_set_file_name_add("BASIS_SET")
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

KIND = SUBSYS.KIND_add()
KIND.Section_parameters = "Si"
KIND.Element = "Si"
KIND.Basis_set = "DZVP-GTH-PADE"
KIND.Potential = "GTH-PADE-q4"

#===============================================================================
# Calculate and print energy. This function is part of the ASE calculator
# interface, and should provide to be useful. You can also use the calc.run()
# function to simply run cp2k without using these ASE specific functions.
print calc.get_potential_energy()
