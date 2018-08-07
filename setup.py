from setuptools import setup, find_packages
import inputparser
import utilities
import textwrap
import os
import os.path
from subprocess import call
import readline
import glob


#===============================================================================
def complete(text, state):
    """For filepath autocompletion."""
    return (glob.glob(text+'*')+[None])[state]


#===============================================================================
def which(program):
    """Tests if the given executable is available in system PATH.

    args:
        program: string
            The executable name.
    """
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
def ask(question, options):
    answer_valid = False
    while not answer_valid:
        answer = input(question)
        try:
            answer = int(answer)
            if answer not in options:
                raise ValueError
            answer_valid = True
        except ValueError:
            print(str(answer) + " is not a valid option. Please try again.")
    return answer


#===============================================================================
def main():
    # Start setup
    utilities.print_title("PYCP2K INSTALLATION STARTED")

    # Setup filepath autocompleter
    readline.set_completer_delims(' \t\n;')
    readline.parse_and_bind("tab: complete")
    readline.set_completer(complete)

    # Determine the available cp2k executables
    cp2k_commands = [
        ["cp2k", False],
        ["cp2k.sopt", False],
        ["cp2k.popt", False],
        ["cp2k.ssmp", False],
        ["cp2k.psmp", False]
    ]
    for item in cp2k_commands:
        if which(item[0]) is not None:
            item[1] = True

    #---------------------------------------------------------------------------
    # Ask user whether to use executable or xml
    print(textwrap.fill("How should the input structure be created?", width=80))
    options1 = ["from CP2K executable", "from .xml file"]
    print("")
    for i_option, option in enumerate(options1):
        print("    [{}]  {}".format(i_option+1, option))
    print("")
    opt = list(range(1, len(options1)+1))
    source = ask('Enter option number: ', opt)

    #---------------------------------------------------------------------------
    # Executable chosen
    if source == 1:

        # Ask user what to do
        print("|------------------------------------------------------------------------------|")
        print(textwrap.fill("Choose the CP2K executable. It will be used for creating the xml file and set as the default CP2K executable for PYCP2K. This setting can be changed by modifying config.py in the pycp2k folder, and can be dynamically overridden for each simulation with the 'cp2k_command' attribute.", width=80))
        print("")
        for i, [name, avail] in enumerate(cp2k_commands):
            if avail:
                print("    [{}] {}".format(i+1, name))
            else:
                print("    [x] {} not available".format(name))
        print("    [" + str(len(cp2k_commands)+1) + "] Custom CP2K executable name\n")
        options = [x for x in range(1, len(cp2k_commands)) if cp2k_commands[x-1][1]]
        options.append(len(cp2k_commands)+1)
        option_number = ask('Enter option number: ', options)

        if option_number == len(cp2k_commands)+1:
            cp2k_default_command = input('Enter CP2K executable name: ')
        else:
            cp2k_default_command = cp2k_commands[int(option_number-1)][0]

        # Call cp2k comand with flag --xml to create the xml file of the input structure
        try:
            call([cp2k_default_command, "--xml"])
        except OSError:
            utilities.print_error("Could not call executable {} with flag --xml. Canceling installation...".format(cp2k_default_command))
            utilities.print_title("INSTALLATION FAILED")
            return False
        xml_path = "cp2k_input.xml"

    #---------------------------------------------------------------------------
    # xml chosen
    else:
        print("|------------------------------------------------------------------------------|")
        xml_path = input('Enter path to .xml file: ')
        while not os.path.isfile(xml_path):
            print("Invalid path provided. Please try again")
            xml_path = input('Enter path to .xml file:')

        #---------------------------------------------------------------------------
        # Ask for the default CP2K command
        print("|------------------------------------------------------------------------------|")
        print(textwrap.fill("Choose the default CP2K executable if available. This executable is used by default for running CP2K. It can be changed by modifying config.py in the pycp2k folder, and can be dynamically overridden for each simulation with the 'cp2k_command' attribute.", width=80))
        print("")
        for i, [name, avail] in enumerate(cp2k_commands):
                print("    [" + str(i+1) + "] " + name)
        print("    [{}] Custom CP2K executable name".format(len(cp2k_commands)+1))
        print("")
        option_number = ask('Enter option number: ', list(range(1, len(cp2k_commands)+2)))

        if option_number == len(cp2k_commands)+1:
            cp2k_default_command = input('Enter CP2K executable name: ')
        else:
            cp2k_default_command = cp2k_commands[int(option_number-1)][0]

    #---------------------------------------------------------------------------
    # Ask for the default MPI command
    print("|------------------------------------------------------------------------------|")
    print(textwrap.fill("Choose the default MPI executable. If you wan't to perform only serial calculations or define MPI command later, choose option 1. The executable is used by default for MPI parallel runs. It can be changed by modifying config.py in the pycp2k folder, and can be dynamically overridden for each simulation with the 'mpi_command' attribute.", width=80))
    print("")
    mpi_commands = ["mpirun", "srun --mpi=openmpi", "srun --mpi=pmi2"]
    print("    [{}] No MPI command defined for now".format(1))
    for i, name in enumerate(mpi_commands):
        print("    [{}] {}".format(i+2, name))
    print("    [{}] Custom MPI executable name".format(len(mpi_commands)+2))
    print("")
    option_number = ask('Enter option number: ', list(range(1, len(mpi_commands)+3)))

    mpi_on_default = True
    if option_number == len(mpi_commands)+2:
        mpi_default_command = input('Enter MPI executable name: ')
    elif option_number == 1:
        mpi_default_command = ""
        mpi_on_default = False
    else:
        mpi_default_command = mpi_commands[int(option_number-2)]

    #---------------------------------------------------------------------------
    # Call input parser with the xml file
    (version, revision) = inputparser.main(xml_path)
    utilities.print_title("INSTALLING PACKAGE")

    #---------------------------------------------------------------------------
    # Write the config file
    with open('pycp2k/config.py', 'w') as config_file:
        contents = ("#! /usr/bin/env python\n"
                    "# -*- coding: utf-8 -*-\n\n"
                    "cp2k_default_command = \"" + cp2k_default_command + "\"\n"
                    "mpi_default_command = \"" + mpi_default_command + "\"\n"
                    "mpi_on_default = " + str(mpi_on_default) + "\n"
                    "build_version = \"" + version.split()[2] + "\"\n"
                    "build_revision = \"" + revision.split()[-1] + "\"")
        config_file.write(contents)

    # Start package setup
    setup(
        name='pycp2k',
        version='0.1',
        description='A python interface to CP2K',
        url='https://github.com/SINGROUP/pycp2k.git',
        author='Lauri Himanen',
        author_email='lauri.himanen@gmail.com',
        license='MIT',
        packages=find_packages(),
        install_requires=[
            'future',
            'numpy',
            'ase',
        ],
        zip_safe=False)

    utilities.print_title("INSTALLATION COMPLETED SUCCESFULLY")


# Run main function by default
if __name__ == "__main__":
    main()
