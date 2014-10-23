#! /usr/bin/env python
"""
Constraints from ASE Atoms.
"""
from pycp2k.cp2k import CP2K
from ase import Atoms, Atom
from ase.constraints import FixAtoms

#===============================================================================
# Setup calculator
calc = CP2K()
calc.working_directory = "/home/lauri"
calc.project_name = "constrained_water"
calc.mpi_n_processes = 2

#===============================================================================
# Structure
water = Atoms()
water.set_cell([24.955, 24.955, 24.955])
water.set_pbc(True)
water.append(Atom("O", [22.9836691917178939, 6.93183557997552668, 0.754607553842305823]))
water.append(Atom("H", [23.1493887587765457, 6.38145839360815526, 1.57291188465716791]))
water.append(Atom("H", [23.8522379765498265, 7.11351376960166615, 0.293542155628028989]))
water.append(Atom("O", [9.55748115579216773, 10.1625527712466361, -12.8321807856825103]))
water.append(Atom("H", [9.48825863164111638, 10.8031673228011336, -13.5969168437373611]))
water.append(Atom("H", [8.66207900403075648, 9.75244702889359871, -12.6587787478834102]))
water.append(Atom("O", [19.8436465738885985, 10.0378451904347870, 9.93036518412813862]))
water.append(Atom("H", [19.1357369126550836, 9.37699136789161081, 9.68109397285001450]))
water.append(Atom("H", [19.9908902622388958, 10.0115791753817565, 10.9191166153261410]))
fix_atoms = FixAtoms(indices=[0, 3, 6])
water.set_constraint(fix_atoms)

#===============================================================================
# Create shortcuts for the most used subtrees of the input.
CP2K_INPUT = calc.CP2K_INPUT
GLOBAL = CP2K_INPUT.GLOBAL
FORCE_EVAL = CP2K_INPUT.FORCE_EVAL_add()
SUBSYS = FORCE_EVAL.SUBSYS
MOTION = CP2K_INPUT.MOTION
DFT = FORCE_EVAL.DFT
FORCEFIELD = FORCE_EVAL.MM.FORCEFIELD

#===============================================================================
# GLOBAL
GLOBAL.Run_type = "MD"

#===============================================================================
# FORCE EVAL
FORCE_EVAL.Method = "FIST"

# Bond-bend potential
bend = FORCEFIELD.BEND_add()
bend.Atoms = ["H", "O", "H"]
bend.K = 0.0
bend.Theta0 = 1.8

# Bond-stretch potential
bond = FORCEFIELD.BOND_add()
bond.Atoms = ["O", "H"]
bond.K = 0.0
bond.R0 = 1.8

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

# Coulomb potential with Ewald summation
FORCE_EVAL.MM.POISSON.EWALD.Ewald_type = "ewald"
FORCE_EVAL.MM.POISSON.EWALD.Alpha = 0.44
FORCE_EVAL.MM.POISSON.EWALD.Gmax = 21

# Subsys
calc.create_cell(SUBSYS, water)
calc.create_coord(SUBSYS, water, len(water)*["H2O"])

#===============================================================================
# MOTION
calc.create_fixed_atoms(SUBSYS, water)
MOTION.MD.Ensemble = "NVT"
MOTION.MD.Steps = 100
MOTION.MD.Timestep = 2.5
MOTION.MD.Temperature = 298
MOTION.MD.THERMOSTAT.Region = "MOLECULE"
MOTION.MD.THERMOSTAT.NOSE.Length = 3
MOTION.MD.THERMOSTAT.NOSE.Yoshida = 3
MOTION.MD.THERMOSTAT.NOSE.Timecon = 1000
MOTION.MD.THERMOSTAT.NOSE.Mts = 2

#===============================================================================
# Run
calc.run()
calc.vmd_view_trajectory()
