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
def main():
    # Start setup
    utilities.print_title("PYCP2K INSTALLATION STARTED")
    # Start package setup
    setup(
        name='pycp2k',
        version='0.2.1',
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
