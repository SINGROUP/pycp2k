PYCP2K: a python interface to CP2K
==================================================

1. [Introduction](#introduction)  
2. [Example](#example)
3. [Installation on Linux Desktop](#linux)  
4. [Installation on Triton](#triton)
5. [Implementation Notes](#notes)

<a name="introduction"></a>
1\. Introduction 
--------------------------------------------------

PYCP2K is a python package providing a dynamic object-oriented interface to [CP2K](http://www.cp2k.org/), an atomistic and molecular simulation software.

PYCP2K allows the user to create and run entire CP2K simulations with python scripts. The simulation parameters can be dynamically created and altered thanks to an *object tree* that replaces the traditional CP2K input scripts.

The benefits of using PYCP2K over using the traditional CP2K input files:
- Use python data structures and algorithms to create and modify the input
- Create and run CP2K simulations with one python script.
- Modular simulation setup by e.g. using functions to create parts of the input
- Structure creation and loading with [ASE](https://wiki.fysik.dtu.dk/ase/)
- Easily extract results from the output file with predefined functions or with custom regular expressions
- Autocompletion if provided by your IDE (tested with [Spyder](https://code.google.com/p/spyderlib/))
- Built-in documentation for all keywords and sections (with [Spyder](https://code.google.com/p/spyderlib/) you can access documentation by control-clicking the variable names). 
- Use additional python libraries (numpy, scipy, matplotlib, etc.) to also analyze the results - all with python.

Technically the interfacing to CP2K happens simply by writing CP2K input files and reading the output files. There is no direct interface to the fortran code (i.e. F2PY not used).

<a name="example"></a>
2\. Example
--------------------------------------------------
An example script that calculates the energy and forces in a silicon lattice using DFT. To see a fully documented version of this example and other examples, look at the examples folder.
```python
#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pycp2k.cp2k import CP2K
from ase.lattice.cubic import Diamond

#====================== Create the structure with ASE ==========================
lattice = Diamond(directions=[[1, 0, 0], [0, 1, 0], [0, 0, 1]],
                  symbol='Si',
                  latticeconstant=5.430697500,
                  size=(1, 1, 1))
                  
#================= Define and setup the calculator object ======================
calc = CP2K()
calc.working_directory = "/home/lauri"
calc.project_name = "si_bulk"
calc.mpi_n_processes = 2

#==================== Define shortcuts for easy access =========================
CP2K_INPUT = calc.CP2K_INPUT
GLOBAL = CP2K_INPUT.GLOBAL
FORCE_EVAL = CP2K_INPUT.FORCE_EVAL_add() # Repeatable items have to be first created
SUBSYS = FORCE_EVAL.SUBSYS
DFT = FORCE_EVAL.DFT
SCF = DFT.SCF

#======================= Write the simulation input ============================
GLOBAL.Run_type = "ENERGY_FORCE"
GLOBAL.Print_level = "LOW"
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
KIND = SUBSYS.KIND_add("Si")  # Section_parameters can be provided as argument.
KIND.Basis_set = "DZVP-GTH-PADE"
KIND.Potential = "GTH-PADE-q4"
calc.create_cell(SUBSYS, lattice)
calc.create_coord(SUBSYS, lattice)

#======================= Run the simulation ============================
calc.run()

#======================= Fetch results ============================
print calc.get_potential_energy()
print calc.get_forces()
print calc.get_output_value(r"SCF run converged in\s*(\d*)\s*steps")

```
<a name="linux"></a>
3\. Installation on Linux Desktop
--------------------------------------------------
These installation instructions were tested on Ubuntu 14.04 x64:

1. This package depends on the [numpy package](http://www.scipy.org/install.html). Please install it first.
2. Install [ASE](https://wiki.fysik.dtu.dk/ase/) if you want to use ASE's structure creation or loading. Not mandatory.
2. Pull this repository to any location on your computer:

   ```
   git clone https://github.com/SINGROUP/pycp2k.git
   ```

3. The correct input structure is created from the .xml file that can be created by calling the CP2K executable with flag --xml. During the setup you will have the option of creating the .xml file by using a CP2K executable on your computer, or by using a pre-existing .xml file. The .xml files may differ between CP2K versions, and if you change CP2K version at some point, you should rerun this installation. The .xml files for CP2K 2.4.0 and 2.5.1 are provided with this repository.
4. Install the package by running the setup script in terminal. During setup you will be asked how you want to create the input structure (using executable or existing xml file) and what should the default CP2K and MPI commands be.
   For local setup use:

   ```
   python setup.py install --user
   ```
   
   For system-wide setup use:
   
   ```
   sudo python setup.py install
   ```

<a name="triton"></a>
4\. Installation on Triton
--------------------------------------------------

These instructions were made for and tested on Triton, the computing cluster at Aalto University, but they should be extensible to any other computer cluster with the appropriate changes.

1. Installation:
   1. Load the modules required for installation. Python >= 2.7.6 should be used. If you plan on using the default CP2K version on triton, you should load the following:
   
       ```
       module load triton/python/2.7.6 cp2k
       ```
   If on the other hand you plan on using your custom compiled version, remember to load the needed modules for running the CP2K executable during the setup (the CP2K executable is run during setup with the -xml flag to produce the input structure). E.g. for CP2K compiled with mkl library you should use:
   
       ```
       module load triton/python/2.7.6 mkl/2013.3.163
       ```
       
   2. Clone this repository to somewhere in your work directory:
   
      ```
      git clone https://github.com/SINGROUP/pycp2k.git
      ```
      
   3. Install the package locally. If you loaded the cp2k module you should be able to create the input structure from the cp2k executable. When the setup asks for default MPI executable provide an appropriate *srun* command.
   
      ```
      python setup.py install --user
      ```

2. Usage (MPI parallel run on Triton):
   1. Write the python script for your simulation. See the examples folder for inspiration.
   2. Make sure that you have the files for potentials and basis sets available. For testing you can e.g. use the files *GTH\_POTENTIALS* and *BASIS\_SET* found in the examples folder.
   2. Run the python script with a batch file. The batch file could look something like this:
   
      ```sh
      #!/bin/sh
      #SBATCH -n 12
      #SBATCH -N 1
      #SBATCH --constraint=xeon|xeonib
      #SBATCH --time=10:00
      #SBATCH --mem-per-cpu=500

      module load cp2k triton/python/2.7.6 numpy ase/3.6.0rev2515
      export PYTHONPATH=$PYTHONPATH:/full/path/to/pycp2k/package
      python example_si_triton.py
      ```
      
      NOTE: In each batch file you will have to tell the program where the PYCP2K package is located with the export command. Set this path to point to the git repository which you cloned in installation step ii.
      
      NOTE: At the moment you will have to load an older ASE 3.6 module. The default ASE 3.8 module is not working on Triton atm.
      
      NOTE: In the batch file you specify the number of processes that are allocated for you. This doesn't automatically mean that MPI is initialized with that many processes. You must specify the number of mpi processes in the python script with calculator attribute *mpi\_n\_processes*
      
      NOTE: The nodes are constrained to xeon/xeonib because the default version of cp2k on triton will not run on opteron nodes. On xeon ivy bridge nodes you might get a warning about fabric initialization but the calculations seem to run normally.
      
<a name="notes"></a>
5\. Implementation Notes
--------------------------------------------------

1. All section names are in uppercase to prevent clashes with python keywords (global, print, etc.)
2. The keyword names are capitalized. This is in order to avoid clashing with subsection names (yes, a section may have a keyword and a subsection with the same name) and python keywords.
3. Section and keyword names 'X' that start with a numeric value have been renamed to 'NUMX'. This is because python doesn't support variable names which start with numbers
4. Section and keyword names which include the plus sign '+' have been renamed so that it is replaced with 'PLUS'. This is because python doesn't allow the plus sign within variable names.
5. Section and keyword names which include the minus/hyphen sign '-' have been renamed so that it is replaced wih '_'. This is because python doesn't allow the minus/hyphen sign within variable names.
6. All the repeatable sections X have to be added with a function 'X\_add()'. This function returns a reference to the newly created object which you should store into a new variable for later access. Optionally you can provide the 'Section\_parameters' as an argument to this function. The list of the repeatable sections can be accessed from attribute 'X\_list'.
7. You can use aliases and even use several aliases for the same item in the scripts. However, the default name will be used in the input file.
