# Copyright 2015-2018 Lauri Himanen, Fawzi Mohamed, Ankit Kariryaa
# 
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from future import standard_library
standard_library.install_aliases()
from builtins import object
import os
import re
from io import StringIO
import logging
import pickle
import numpy as np
#from nomadcore.baseclasses import AbstractBaseParser
#import nomadcore.configurationreading
#from cp2kparser.generic.inputparsing import metainfo_data_prefix, metainfo_section_prefix

from pint import UnitRegistry
import ase

from pycp2k.cp2k import CP2K

ureg = UnitRegistry()
#logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
#logging.basicConfig(filename='pycp2k.log', level=logging.INFO)


class CP2KInputParser():
    """Used to parse out a CP2K input file.

    CP2K offers a complete structure for the input in an XML file, which can be
    printed with the command cp2k --xml. This XML file has been preparsed into
    a native python object ('CP2KInput' class found in generic.inputparsing)
    and stored in a python pickle file. It e.g. contains all the default values
    that are often needed as they are used if the user hasn't specified a
    settings in the input. This XML file is used to get the default values
    because it is rather cumbersome to hard code them in the parser itself,
    especially if there will be lot's of them. Hard coded values will also be
    more error prone, and would have to be checked for each parser version.

    CP2K input supports including other input files and also
    supports variables. This is currently not supported, but may be added at
    some point.
    """
    def __init__(self):
        """
        Attributes:
            input_tree: The input structure for this version of CP2K. The
                structure is already present, in this module it will be filled with
                data found from the input file.
            input_lines: List of preprocessed lines in the input. Here all the
                variables have been stated explicitly and the additional input files have
                been merged.
        """
        self.storage_obj = CP2K()
        self.input_tree = None
        self.input_lines = None
        self.unit_mapping = {
            # Distance
            "BOHR": "bohr",
            "M": "m",
            "PM": "pm",
            "NM": "nm",
            "ANGSTROM": "angstrom",
            # Time
            "S": "s",
            "FS": "fs",
            "PS": "ps",
            "AU_T": "(hbar/hartree)",
            "WAVENUMBER_T": None,
        }

    def parse(self, filepath):

        # Preprocess to spell out variables and to include stuff from other
        # files
        self.preprocess_input(filepath)
        
        # Gather the information from the input file
        self.fill_input_tree(filepath)
        return self.storage_obj


    def get_pint_unit_string(self, cp2k_unit_string):
        """Translate the CP2K unit definition into a valid pint unit.
        """
        units = re.split('[\^\-\+\*\d]+', cp2k_unit_string)
        for unit in units:
            if unit == "":
                continue
            pint_unit = self.unit_mapping.get(unit.upper())
            if pint_unit is None:
                return None
            cp2k_unit_string = cp2k_unit_string.replace(unit, pint_unit)
        return cp2k_unit_string

    def _pythonize_cp2k_names(self, name):
        """handles CP2K special characters:
           python cannot handle variables with
                   - 
                   + 
           and starting 0-9
        """
        if name[0].isdigit():
            name = "NUM" + name
        name = name.replace("-","_")
        name = name.replace("+","PLUS")
        return name

    def fill_input_tree(self, file_path):
        """Parses a CP2K input file into an object tree.

        Return an object tree represenation of the input augmented with the
        default values and lone keyword values from the x_cp2k_input.xml file
        which is version specific. Keyword aliases are also mapped to the same
        data.

        The cp2k input is largely case-insensitive. In the input tree, we wan't
        only one standard way to name things, so all section names and section
        parameters will be transformed into upper case.

        To query the returned tree use the following functions:
            get_keyword("GLOBAL/PROJECT_NAME")
            get_parameter("GLOBAL/PRINT")
            get_default_keyword("FORCE_EVAL/SUBSYS/COORD")

        Args:
            : A string containing the contents of a CP2K input file. The
            input file can be stored as string as it isn't that big.

        Returns:
            The input as an object tree.
        """

        #self.setup_version(self.parser_context.version_id)
        section_stack = []
        section_objects = []
        #self.input_tree.root_section.accessed = True

        for line in self.input_lines:
            print(line, section_objects)

            # Remove comments and whitespaces
            line = line.split('!', 1)[0].split('#', 1)[0].strip()

            # Skip empty lines
            if len(line) == 0:
                continue

            # Section ends
            if line.upper().startswith('&END'):
                section_stack.pop()
                section_objects.pop()
            # Section starts
            elif line[0] == '&':
                parts = line.split(' ', 1)
                name = parts[0][1:].upper()
                # handling - + and 0-9
                name = self._pythonize_cp2k_names(name)
                #if name[0].isdigit():
                #    name = "NUM" + name
                #name = name.replace("-","_")
                #name = name.replace("+","PLUS")
                print(name)

                # creation of section objects
                if len(section_stack) == 0:
                    parent_section = self.storage_obj.CP2K_INPUT
                else:
                    parent_section = section_objects[-1]
                try:
                    section = getattr(parent_section, name)
                except AttributeError:
                    section = getattr(parent_section, name+"_add")()
                section_objects.append(section)
                section_stack.append(name)
                # Form the path
                path = ""
                for index, item in enumerate(section_stack):
                    if index != 0:
                        path += '/'
                    path += item

                # Mark the section as accessed.
                #self.input_tree.set_section_accessed(path)

                # Save the section parameters
                if len(parts) > 1:
                    setattr(section, self._pythonize_cp2k_names(parts[1].strip().upper()))
                    #self.input_tree.set_parameter(path, parts[1].strip().upper())
                    

            # Ignore variables and includes that might still be here for some
            # reason
            elif line.upper().startswith('@'):
                continue

            # Contents (keywords, default keywords)
            else:
                split = line.split(None, 1)
                if len(split) <= 1:
                    keyword_value = ""
                else:
                    keyword_value = split[1]
                keyword_name = split[0].upper()
                setattr(section, self._pythonize_cp2k_names(keyword_name), self._pythonize_cp2k_names(keyword_value))
                #self.input_tree.set_keyword(path + "/" + keyword_name, keyword_value, line)
        return

    def preprocess_input(self, filepath):
        """Preprocess the input file. Concatenate .inc files into the main
        input file and explicitly state all variables.
        """
        # Read the input file into memory. It shouldn't be that big so we can
        # do this easily
        input_lines = []
        with open(filepath, "r") as f:
            for line in f:
                input_lines.append(line.strip())

        # Merge include files to input
        extended_input = input_lines[:]  # Make a copy
        i_line = 0
        for line in input_lines:
            if line.startswith("@INCLUDE") or line.startswith("@include"):
                split = line.split(None, 1)
                includepath = split[1]
                basedir = os.path.dirname(filepath)
                filepath = os.path.join(basedir, includepath)
                filepath = os.path.abspath(filepath)
                if not os.path.isfile(filepath):
                    logger.warning("Could not find the include file '{}' stated in the CP2K input file. Continuing without it.".format(filepath))
                    continue

                # Get the content from include file
                included_lines = []
                with open(filepath, "r") as includef:
                    for line in includef:
                        included_lines.append(line.strip())
                    del extended_input[i_line]
                    extended_input[i_line:i_line] = included_lines
                    i_line += len(included_lines)
            i_line += 1

        # Gather the variable definitions
        variables = {}
        input_set_removed = []
        for i_line, line in enumerate(extended_input):
            if line.startswith("@SET") or line.startswith("@set"):
                components = line.split(None, 2)
                name = components[1]
                value = components[2]
                variables[name] = value
                logger.debug("Variable '{}' found with value '{}'".format(name, value))
            else:
                input_set_removed.append(line)

        # Place the variables
        variable_pattern = r"\$\{(\w+)\}|\$(\w+)"
        compiled = re.compile(variable_pattern)
        reserved = ("include", "set", "if", "endif")
        input_variables_replaced = []
        for line in input_set_removed:
            results = compiled.finditer(line)
            new_line = line
            offset = 0
            for result in results:
                options = result.groups()
                first = options[0]
                second = options[1]
                if first:
                    name = first
                elif second:
                    name = second
                if name in reserved:
                    continue
                value = variables.get(name)
                if not value:
                    logger.error("Value for variable '{}' not set.".format(name))
                    continue
                len_value = len(value)
                len_name = len(name)
                start = result.start()
                end = result.end()
                beginning = new_line[:offset+start]
                rest = new_line[offset+end:]
                new_line = beginning + value + rest
                offset += len_value - len_name - 1
            input_variables_replaced.append(new_line)

        self.input_lines = input_variables_replaced
        return self.input_lines


