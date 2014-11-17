PYCP2K: a python interface to CP2K
==================

A python package that provides a python interface to CP2K, an atomistic and molecular simulation software.

PYCP2K allows the user to create and run entire CP2K simulation with python scripts only. The simulation parameters can be dynamically created and altered thanks to an *object tree* that replaces the traditional CP2K input scripts.

PYCP2K is able to use the ASE library for creating structures and loading [many different atomic structure files](https://wiki.fysik.dtu.dk/ase/ase/io.html). PYCP2K also is an ASE compatible atomic structure calculator. If you are not familiar with ASE, do not despair: you can yourself decide how much you want to utilize the functionality provided by ASE.

Technically the interfacing to CP2K happens simply by writing CP2K input files and reading the output files. There is no direct interface to the fortran code (i.e. F2PY not used).

Desktop Installation:
------------------

These installation instructions were tested on Ubuntu 14.04 x64:

1. This package depends on the numpy and the ASE package. Please install them first.
   1. [Full SciPy stack](http://www.scipy.org/install.html)
   2. [ASE](https://wiki.fysik.dtu.dk/ase/)
2. Pull this repository to any location on your computer:

   ```
   git clone https://github.com/lauri-codes/PYCP2K.git
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

Installation and usage on Triton (Aalto University's computing cluster):
------------------

These instructions were made for and tested on Triton, but they should be extensible to any other computer cluster with the appropriate changes.

1. Installation:
   1. Load the modules required for installation. Python >= 2.7.6 should be used.
   
       ```
       module load triton/python/2.7.6 cp2k
       ```
       
   2. Clone this repository to somewhere in your work directory:
   
      ```
      git clone https://github.com/lauri-codes/PYCP2K.git
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

Example Script
------------------
```python
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
# Atoms object created earlier. As arguments these two functions take the
# subsys where the entries should be created and the Atoms object from which
# they are exctracted.
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
calc.write_input_file()

# 2. Write the input file and run CP2K as a subprocess in python.
calc.run()

# 3. Write the input file, run CP2K as a subprocess and fetch results from the output file.
print calc.get_potential_energy()
print calc.get_forces()
```

Important notes:
------------------

1. All section names are in uppercase to prevent clashes with python keywords (global, print, etc.)
2. The keyword names are capitalized. This is in order to avoid clashing with subsection names (yes, a section may have a keyword and a subsection with the same name) and python keywords.
3. Section and keyword names 'X' that start with a numeric value have been renamed to 'NUMX'. This is because python doesn't support variable names which start with numbers
4. Section and keyword names which include the plus sign '+' have been renamed so that it is replaced with 'PLUS'. This is because python doesn't allow the plus sign within variable names.
5. Section and keyword names which include the minus/hyphen sign '-' have been renamed so that it is replaced wih '_'. This is because python doesn't allow the minus/hyphen sign within variable names.
6. All the repeatable sections X have to be added with a function 'X\_add()'. This function returns a reference to the newly created object which you should store into a new variable for later access. Optionally you can provide the 'Section\_parameters' as an argument to this function. The list of the repeatable sections can be accessed from attribute 'X\_list'.
7. You can use aliases and even use several aliases for the same item in the scripts. However, the default name will be used in the input file.
