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
3. The correct input structure for your cp2k executable is automatically created upon setup. Please make sure that you have cp2k installed, and callable from terminal with the name cp2k. **If you install a new version of cp2k** at some point, you must repeat this installation procedure for cp2kase to work properly.
4. Install the package by running the setup script in terminal:
```
   sudo python setup.py install
```
Example
------------------


Important notes:
------------------

1. All section names and keywords are in uppercase to prevent clashes with python keywords (global, print, etc.)
2. Section names 'X' that start with a numeric value have been renamed to 'NUMX'. This is because python doesn't support variable names which start with numbers
3. Sections and keywords which include the plus sign '+' have been renamed so that it is replaced by 'PLUS'. This is because python doesn't allow the plus sign within variable names.
4. Sections and keywords which include the minus/hyphen sign '-' have been renamed so that it is replaced by 'HYPMIN'. This is because python doesn't allow the minus/hyphen sign within variable names.
5. By default there is one accessable object for each item (section, keyword, etc.), repeatable or not. If you want to add more than one of the repeatable items, you must use the 'add[SECTION NAME]' function. For sections this function returns a reference to the newly created section object which you should store into a new variable for later access.
6. If you use aliases, use the same alias always within one script! Alias values are not linked because of string immutability.
7. The variable names for keywords, default keywords and section parameters start with '_'. This is in order to avoid clashing with subsection names (a section may have a keyword and a subsection with the same name).
