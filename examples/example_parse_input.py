"""Reads CP2K input file
and writes it out through the module
pycp2k.CP2K

The resulting content should match the
given input file.
"""

from pycp2k import CP2KInputParser

filename = "si_bulk.inp"
print("CP2K INPUT FILE", filename)

inpparser = CP2KInputParser()

calc = inpparser.parse(filename)

print("info about input parser")
print(inpparser)

print("cp2k info storage \n")
print(inpparser.storage_obj)

print("raw input \n")
print(inpparser.input_lines)


calc.working_directory = "."
calc.project_name = "rewritten_cp2k"
calc.write_input_file()

print("file written TO", calc.project_name + ".inp")
