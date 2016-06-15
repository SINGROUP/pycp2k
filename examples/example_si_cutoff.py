import re
from pycp2k import CP2K
from ase.lattice.cubic import Diamond
from ase.visualize import view

#===============================================================================
# Create the Si lattice here
lattice = Diamond(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                  symbol='Si',
                  latticeconstant=5.430697500,
                  size=(1, 1, 1))

view(lattice)

#===============================================================================
# Setup directories and mpi
calc = CP2K()
calc.working_directory = "./"
calc.project_name = "si_bulk"
calc.mpi_n_processes = 2

#===============================================================================
# Create shortcuts for the most used subtrees of the input
CP2K_INPUT = calc.CP2K_INPUT
GLOBAL = CP2K_INPUT.GLOBAL
FORCE_EVAL = CP2K_INPUT.FORCE_EVAL_add()
SUBSYS = FORCE_EVAL.SUBSYS
DFT = FORCE_EVAL.DFT
SCF = DFT.SCF

#===============================================================================
# Fill input tree
GLOBAL.Run_type = "ENERGY"
GLOBAL.Print_level = "LOW"

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

KIND = SUBSYS.KIND_add("Si")
KIND.Basis_set = "DZVP-GTH-PADE"
KIND.Potential = "GTH-PADE-q4"

#===============================================================================
# Search for a good CUTOFF
energies = []
for cutoff in range(40, 90, 20):
    DFT.MGRID.Cutoff = cutoff
    calc.output_path = calc.working_directory + "/" + calc.project_name + str(cutoff) + ".out"
    calc.run()
    with open(calc.output_path, "r") as fin:
        regex = re.compile(" ENERGY\| Total FORCE_EVAL \( QS \) energy \(a\.u\.\):\s+(.+)\n")
        for line in fin:
            match = regex.match(line)
            if match:
                energies.append(match.groups()[0])

print energies
