from setuptools import setup
import inputparser
from pycp2k import utilities
import textwrap
import os
import os.path
from subprocess import call


#===============================================================================
def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


#===============================================================================
def main():
    # Start setup
    utilities.print_title("PYCP2K INSTALLATION STARTED")

    #---------------------------------------------------------------------------
    # Ask user whether to use executable or xml
    print textwrap.fill("How should the input structure be created?", width=80)
    print "\n    [1]  from CP2K executable"
    print "    [2]  from .xml file\n"
    source_valid = False
    while not source_valid:
        try:
            source = raw_input('Enter option number:')
            source = int(source)
            source_valid = True
        except ValueError:
            print "That's not a valid integer number! Try again."

    #---------------------------------------------------------------------------
    # Executable chosen
    if source == 1:
        # Determine the available cp2k executables
        cp2k_commands = [["cp2k.popt", False], ["cp2k.sopt", False], ["cp2k.psmp", False]]
        for item in cp2k_commands:
            if which(item[0]) is not None:
                item[1] = True

        # Ask user what to do
        print "|------------------------------------------------------------------------------|"
        print textwrap.fill("Choose the CP2K executable used for creating the xml file:", width=80)
        for i, [name, avail] in enumerate(cp2k_commands):
            if avail:
                print "\n    [" + str(i+1) + "] " + name
            else:
                print "    [X] " + name + " not available"
        print "    [" + str(len(cp2k_commands)+1) + "] Custom CP2K executable name\n"
        valid_number = False
        while not valid_number:
            try:
                option_number = raw_input('Enter option number:')
                option_number = int(option_number)
                valid_number = True
            except ValueError:
                print "That's not a valid integer number! Try again."

        if option_number == len(cp2k_commands)+1:
            cp2k_path = raw_input('Enter CP2K executable name:')
        else:
            cp2k_path = cp2k_commands[int(option_number-1)][0]

        # Call cp2k comand with flag --xml to create the xml file of the input structure
        try:
            call([cp2k_path, "--xml"])
        except OSError:
            utilities.print_error("Could not call executable " + cp2k_path + " with flag --xml. Canceling installation...")
            utilities.print_title("INSTALLATION FAILED")
            return False
        xml_path = "cp2k_input.xml"

    #---------------------------------------------------------------------------
    # xml chosen
    else:
        available_versions = ["2.4"]
        print "|------------------------------------------------------------------------------|"
        print textwrap.fill("Which .xml file should be used:", width=80)
        for i, version in enumerate(available_versions):
            print "\n    [" + str(i+1) + "] cp2k_input_" + version + ".xml"
        print "    [" + str(len(available_versions)+1) + "] Provide path to .xml file\n"
        valid_number = False
        while not valid_number:
            try:
                option_number = raw_input('Enter option number:')
                option_number = int(option_number)
                valid_number = True
            except ValueError:
                print "That's not a valid integer number! Try again."

        if option_number == 2:
            xml_path = raw_input('Enter path to .xml file:')
            while not os.path.isfile(xml_path):
                print "Invalid path provided. Please try again"
                xml_path = raw_input('Enter path to .xml file:')
        else:
            xml_path = "cp2k_input_" + available_versions[option_number - 1] + ".xml"

    #---------------------------------------------------------------------------
    # Ask for the default CP2K command
    print "|------------------------------------------------------------------------------|"
    print textwrap.fill("Choose the default CP2K executable. This executable is used by default for running CP2K. It can be changed by modifying config.py in the pycp2k folder, and can be dynamically overridden for each simulation with the 'cp2k_command' attribute.", width=80)
    print "\n"
    for i, [name, avail] in enumerate(cp2k_commands):
            print "    [" + str(i+1) + "] " + name
    print "    [" + str(len(cp2k_commands)+1) + "] Custom CP2K executable name\n"
    valid_number = False
    while not valid_number:
        try:
            option_number = raw_input('Enter option number:')
            option_number = int(option_number)
            valid_number = True
        except ValueError:
            print "That's not a valid integer number! Try again."

    if option_number == len(cp2k_commands)+1:
        cp2k_default_command = raw_input('Enter CP2K executable name:')
    else:
        cp2k_default_command = cp2k_commands[int(option_number-1)][0]

    #---------------------------------------------------------------------------
    # Ask for the default MPI command
    print "|------------------------------------------------------------------------------|"
    print textwrap.fill("Choose the default MPI executable. This executable is used by default for MPI parallel runs. It can be changed by modifying config.py in the pycp2k folder, and can be dynamically overridden for each simulation with the 'mpi_command' attribute.", width=80)
    mpi_commands = ["mpirun"]
    for i, name in enumerate(mpi_commands):
        print "\n    [" + str(i+1) + "] " + name
    print "    [" + str(len(mpi_commands)+1) + "] Custom MPI executable name\n"
    valid_number = False
    while not valid_number:
        try:
            option_number = raw_input('Enter option number:')
            option_number = int(option_number)
            valid_number = True
        except ValueError:
            print "That's not a valid integer number! Try again."

    if option_number == len(mpi_commands)+1:
        mpi_default_command = raw_input('Enter MPI executable name:')
    else:
        mpi_default_command = mpi_commands[int(option_number-1)]

    #---------------------------------------------------------------------------
    # Write the config file
    with open('pycp2k/config.py', 'w') as config_file:
        contents = ("#! /usr/bin/env python\n"
                    "# -*- coding: utf-8 -*-\n\n"
                    "cp2k_default_command = \"" + cp2k_default_command + "\"\n"
                    "mpi_default_command = \"" + mpi_default_command + "\"")
        config_file.write(contents)

    #---------------------------------------------------------------------------
    # Call input parser with the xml file
    if inputparser.main(xml_path):
        utilities.print_title("INSTALLING PACKAGE")

        setup(name='pycp2k',
              version='0.1',
              description='A python interface to CP2K',
              url='https://github.com/lauri-codes/pycp2k.git',
              author='Lauri Himanen',
              author_email='lauri.himanen@gmail.com',
              license='GPL3',
              packages=['pycp2k'],
              zip_safe=False)

        utilities.print_title("INSTALLATION COMPLETED SUCCESFULLY")
    else:
        utilities.print_title("INSTALLATION FAILED")

# Run main function by default
if __name__ == "__main__":
    main()
