"""Reads CP2K input file
"""

from pycp2k import CP2KInputParser

filename = "parseme_cp2k.inp"
print(filename)

inpparser = CP2KInputParser()

inpparser.parse(filename)

print("info about input parser")
print(inpparser)

print("cp2k info storage", inpparser.storage_obj)

print("raw input" ,inpparser.input_lines)

