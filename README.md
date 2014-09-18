cp2kase
==================

A python module that provides an ASE interface to CP2K, an atomistic and molecular simulation software.

Installation:
------------------

These installation instructions are for Ubuntu, and are tested only on Ubuntu 14.04 x64.

  1. This package depends on the numpy and ASE packages. Please install them first.
  2. Pull this repository to any location on your computer.
  3. By default, an input structure for cp2k 2.4 is provided. A tool for creating the correct input structure for the cp2k version specific to your own. Please see the section **Creating an input structure for specifif cp2k version**
  4. Install the package by running the setup script in terminal:
```
    sudo python setup.py install
```

Creating an input structure for specifif cp2k version:
------------------
You can create an xml-file of the input structure used by cp2k by running the command:
```
    cp2k --xml
```
This xml file can be used to automatically create a correct input structure for any cp2k version. 
