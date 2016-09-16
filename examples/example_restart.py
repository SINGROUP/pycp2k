"""
QM/MM test simulation
"""
from pycp2k import CP2K

#===============================================================================
# Setup calculator
calc = CP2K()
calc.working_directory = "./"
calc.project_name = "qmmmwaterrestart"
calc.mpi_n_processes = 2

#===============================================================================
# Create shortcuts for the most used subtrees of the input.
CP2K_INPUT = calc.CP2K_INPUT

#===============================================================================
# Create shortcuts for the most used subtrees of the input.
CP2K_INPUT = calc.CP2K_INPUT
GLOBAL = CP2K_INPUT.GLOBAL
EXT_RESTART = CP2K_INPUT.EXT_RESTART
FORCE_EVAL = CP2K_INPUT.FORCE_EVAL_add()
SUBSYS = FORCE_EVAL.SUBSYS
MOTION = CP2K_INPUT.MOTION
DFT = FORCE_EVAL.DFT
FORCEFIELD = FORCE_EVAL.MM.FORCEFIELD

#===============================================================================
# RESTART
EXT_RESTART.Restart_file_name = "./qmmmwater-1.restart"

#===============================================================================
# GLOBAL
GLOBAL.Run_type = "MD"

#===============================================================================
# FORCE EVAL
FORCE_EVAL.Method = "QMMM"
DFT.Basis_set_file_name = "BASIS_SET"
DFT.Potential_file_name = "GTH_POTENTIALS"
DFT.MGRID.Commensurate = "T"
DFT.MGRID.Cutoff = 300
DFT.SCF.Scf_guess = "atomic"
DFT.XC.XC_FUNCTIONAL.Section_parameters = "pade"

# Bond-bend potential
bend = FORCEFIELD.BEND_add()
bend.Atoms = ["H", "O", "H"]
bend.K = 0.002
bend.Theta0 = 1.823

# Bond-stretch potential
bond = FORCEFIELD.BOND_add()
bond.Atoms = ["O", "H"]
bond.K = 0.02
bond.R0 = 1.89

# Oxygen charge
charge_o = FORCEFIELD.CHARGE_add()
charge_o.Atom = "O"
charge_o.Charge = -0.8476

# Hydrogen charge
charge_h = FORCEFIELD.CHARGE_add()
charge_h.Atom = "H"
charge_h.Charge = 0.4238

# O-O Lennard-Jones
lj_oo = FORCEFIELD.NONBONDED.LENNARD_JONES_add()
lj_oo.Atoms = ["O", "O"]
lj_oo.Epsilon = 78.198
lj_oo.Sigma = 3.166
lj_oo.Rcut = 11.4

# O-H Lennard-Jones
lj_oh = FORCEFIELD.NONBONDED.LENNARD_JONES_add()
lj_oh.Atoms = ["O", "H"]
lj_oh.Epsilon = 0.0
lj_oh.Sigma = 3.6705
lj_oh.Rcut = 11.4

# H-H Lennard-Jones
lj_hh = FORCEFIELD.NONBONDED.LENNARD_JONES_add()
lj_hh.Atoms = ["H", "H"]
lj_hh.Epsilon = 0.0
lj_hh.Sigma = 3.30523
lj_hh.Rcut = 11.4

# # Coulomb potential with Ewald summation
FORCE_EVAL.MM.POISSON.EWALD.Ewald_type = "ewald"
FORCE_EVAL.MM.POISSON.EWALD.Alpha = 0.44
FORCE_EVAL.MM.POISSON.EWALD.Gmax = 21

QMMM = FORCE_EVAL.QMMM
QMMM.CELL.Abc = [8.0, 8.0, 8.0]
QMMM.E_coupl = "GAUSS"

# MM subsystem
h_mm = QMMM.MM_KIND_add("H")
h_mm.Radius = 0.44
o_mmm = QMMM.MM_KIND_add("O")
o_mmm.Radius = 0.78

# QM subsystem
h_qm = QMMM.QM_KIND_add("H")
h_qm.Mm_index = [2, 3]
o_qm = QMMM.QM_KIND_add("O")
o_qm.Mm_index = 1

# Subsys
h_kind = SUBSYS.KIND_add("H")
h_kind.Basis_set = "SZV-GTH-PADE"
h_kind.Potential = "GTH-PADE-q1"

h_kind = SUBSYS.KIND_add("O")
h_kind.Basis_set = "SZV-GTH-PADE"
h_kind.Potential = "GTH-PADE-q6"

#===============================================================================
# MOTION
MOTION.MD.Ensemble = "NVE"
MOTION.MD.Steps = 5
MOTION.MD.Timestep = 1.0
MOTION.MD.Temperature = 300

#===============================================================================
# Run
calc.run()
