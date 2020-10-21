import re
from pycp2k import CP2K
from ase.build import fcc111
from ase import Atoms
from ase.constraints import FixAtoms
import numpy as np

#===============================================================================
# Creating Cu (111) surface with 4 layers 2x2 supercell in orthogonal cell
# through Atomic Simulation Envirnoment https://wiki.fysik.dtu.dk/ase/ build.
# Total amount of vacuum between the slabs is 10 Ang. CO molecule is added
# on-top of one of the top-most copper atoms.Later the atoms are ordered, so
# the top-most goes as first. Finally the two bottom layers of the slab are
# constrained, so they cannot relax.
slab = fcc111('Cu', size=(2,2,4), a=3.62, vacuum=5,
              orthogonal=True, periodic=True)
CO   = Atoms('CO', positions=[slab.positions[-1]+[0,0,1.85], 
                             slab.positions[-1]+[0,0,3.00]])
slab += CO
slab = slab[np.argsort(-1*slab.positions[:, 2])]
mask = [atom.tag > 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

#===============================================================================
# If you want to directly visualize the created slab uncomment following lines:
#from ase.visualize import view
#view(slab)

#===============================================================================
# If you want to print important information about the created slab uncomment
# following lines:
#print("informations about slab")
#print(slab)
#print(slab.get_cell())
#print(slab.get_pbc())
#print(slab.get_positions())
#print(slab.constraints[0].get_indices())
#print("---------")

#===============================================================================
# Setup directories and mpi parallelization. If you specify a working directory
# and a project name, the output and input file names and the
# GLOBAL.Project_name keyword are automatically generated for you. You can
# alternatively specify each separately. You can setup the cp2k command with
# calc.cp2k_command, and the mpi command with calc.mpi_command. MPI can be
# turned on or off with calc.mpi_on (on by default). The -n flag can be setup
# with calc.mpi_n_processes. Any special flags can be specified by using
# calc.cp2k_flags or calc.mpi_flags. By default cp2k is run in the output
# directory, but you can change the working directory with
# calc.working_directory.
calc = CP2K()
calc.working_directory = "./"
calc.project_name = "CO_Cu_2x2_slab"
calc.mpi_n_processes = 48  # optimization takes about 15 min on 48 cpus.

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
MOTION = CP2K_INPUT.MOTION
VDW = DFT.XC.VDW_POTENTIAL

#===============================================================================
# Fill input tree. Section names are in upper case, keywords are capitalized.
# Most IDEs will be able to automatically suggest the entries as you begin
# typing them. Relevant parts of the documentation have been copied to
# parsedclasses.py and some IDEs provide quick access to them (e.g. in spyder
# you can search documentation for keyword with the command "go to definition"

# The keywords can entered as any python type that converts to string (int,
# float, etc.). Additionally you can provide non-repeatable keywords as lists.
# In that case the each list element is converted to string, separated wi§§th
# white space and printed into input file. Repeatable keywords can also be
# defined as lists, but in this case each list item corresponds to a new
# repeated item. For an example of these features see examples/example_qmmm.py.
GLOBAL.Run_type = "GEO_OPT"
GLOBAL.Print_level = "MEDIUM"

# These utility functions will create entries to the input tree from the ASE
# Atoms object created earlier. As arguments these two functions take the
# subsys where the entries should be created and the Atoms object from which
# they are exctracted.
calc.create_cell(SUBSYS, slab)
calc.create_coord(SUBSYS, slab)

FORCE_EVAL.Method = "Quickstep"
FORCE_EVAL.PRINT.FORCES.Section_parameters = "ON"
FORCE_EVAL.PRINT.FORCES.Filename = "forces"
DFT.Basis_set_file_name = "BASIS_MOLOPT"
DFT.Potential_file_name = "GTH_POTENTIALS"
DFT.MGRID.Ngrids = 4
DFT.MGRID.Cutoff = 600
DFT.MGRID.Rel_cutoff = 60
DFT.XC.XC_FUNCTIONAL.Section_parameters = "PBE"
DFT.POISSON.Periodic = "XYZ"
DFT.POISSON.Poisson_solver = "PERIODIC"
DFT.QS.Method = "GPW"
DFT.QS.Eps_default = 1.0E-12
DFT.QS.Map_consistent = ".TRUE."
DFT.QS.Extrapolation = "USE_GUESS"
DFT.KPOINTS.Full_grid = ".TRUE."
DFT.KPOINTS.Scheme = "MONKHORST-PACK 6 7 1"

VDW.Potential_type = "PAIR_POTENTIAL"
vdw1 = VDW.PAIR_POTENTIAL_add()
vdw1.Type                  = "DFTD3(BJ)"
vdw1.Calculate_c9_term     = ".TRUE."
vdw1.Reference_c9_term     = ".TRUE."
vdw1.Long_range_correction = ".TRUE."
vdw1.Parameter_file_name   = "dftd3.dat"
vdw1.Reference_functional  = "PBE"

SCF.Scf_guess = "ATOMIC"
SCF.Eps_scf = 1.0E-7
SCF.Max_scf = 550
SCF.DIAGONALIZATION.Section_parameters = "ON"
SCF.DIAGONALIZATION.Algorithm = "STANDARD"
SCF.MIXING.Section_parameters = True
SCF.MIXING.Method = "BROYDEN_MIXING"
SCF.MIXING.Alpha    = 0.1
SCF.MIXING.Beta     = 1.5
SCF.MIXING.Nbroyden = 8
FORCE_EVAL.PRINT.FORCES.Section_parameters = "OFF" # Forces not important

KIND = SUBSYS.KIND_add("C")  # Section_parameters can be provided as argument.
KIND.Basis_set = "DZVP-MOLOPT-SR-GTH"
KIND.Potential = "GTH-PBE-q4"
KIND = SUBSYS.KIND_add("O")  # Section_parameters can be provided as argument.
KIND.Basis_set = "DZVP-MOLOPT-SR-GTH"
KIND.Potential = "GTH-PBE-q6"
KIND = SUBSYS.KIND_add("Cu")  # Section_parameters can be provided as argument.
KIND.Basis_set = "DZVP-MOLOPT-SR-GTH"
KIND.Potential = "GTH-PBE-q11"

#===============================================================================
# Here are settings for BFGS optimization and setting the constraints:
fix_list = slab.constraints[0].get_indices() # get indices of fixed atoms
fix_list += 1 # python logic (ASE) to Fortran logic (CP2L)

MOTION.GEO_OPT.Optimizer = "BFGS"
MOTION.GEO_OPT.Max_iter  = 240
CONSTRAINT = MOTION.CONSTRAINT
fix1 = CONSTRAINT.FIXED_ATOMS_add() 
fix1.Components_to_fix = "XYZ"
fix1.List = ' '.join(map(str,fix_list))

#===============================================================================
# After you have created your simulation you can choose how to run it.
# Typically there are two options:

# 1. Only write the input file. CP2K is then run manually or with some other
# script.
calc.write_input_file()

# 2. Write the input file and run CP2K as a subprocess in python.
calc.run()

#===============================================================================
# You can analyse the output with whatever tool you want. E.g. the final energy
# can simply be found with a regular expression:
with open(calc.output_path, "r") as fin:
    regex = re.compile(" ENERGY\| Total FORCE_EVAL \( QS \) energy \(a\.u\.\):\s+(.+)\n")
    for line in fin:
        match = regex.match(line)
        if match:
            print("Final energy: {}".format(match.groups()[0]))

