cp2kase
==================

A python module that provides an ASE interface to CP2K, an atomistic and molecular simulation software.

Installation:
------------------

These installation instructions were tested on Ubuntu 14.04 x64:

1. This package depends on the numpy and ASE packages. Please install them first.
   1. [Full SciPy stack](http://www.scipy.org/install.html)
   2. [ASE](https://wiki.fysik.dtu.dk/ase/)
2. Pull this repository to any location on your computer:
```
   git clone https://github.com/lauri-codes/cp2kase.git
```
3. The correct input structure for your cp2k executable is automatically created upon setup. Please make sure that you have cp2k installed, and callable from terminal with the name cp2k. **If you install a new version of cp2k** at some point, you must repeat this installation procedure for cp2kase to workd properly.
4. Install the package by running the setup script in terminal:
```
   sudo python setup.py install
```

Usage:
------------------
Here is an example of a cp2k input file creation with cp2kase. 
