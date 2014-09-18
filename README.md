cp2kase
==================

A python module that provides an ASE interface to CP2K, an atomistic and molecular simulation software.

Installation:
------------------

These installation instructions are for Ubuntu, and are tested only on Ubuntu 14.04 x64.

  1. This package depends on the numpy and ASE packages. Please install them first.
  2. Pull this repository to any location on your computer.
  3. The correct input structure for your cp2k executable is automatically created upon setup. Please make sure that you have cp2k installed, and callable from terminal with the name cp2k
  4. Install the package by running the setup script in terminal:
```
    sudo python setup.py install
```
