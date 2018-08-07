"""
An example on how to read existing CP2K input files directly into the CP2K
object.
"""
from pycp2k import CP2K

# The CP2K object is normally initialized
calc = CP2K()

# This function tries to read the input file in the given path and places its
# contents to the input tree. Notice that this will overwrite any already set
# inputs.
calc.parse("parse_example.inp")

# The calculation can be modified and run after reading the input file
calc.CP2K_INPUT.GLOBAL.Project_name = "modified"
calc.write_input_file("parse_example_modified.inp")
