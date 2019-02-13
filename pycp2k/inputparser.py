import os
import re
import logging


class CP2KInputParser():
    """Used to parse a CP2K input file into an object hierarchy.
    """
    def __init__(self):
        """
        """
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

    def parse(self, cp2kcalc, filepath):
        """
        Args:
            cp2kcalc(pycp2k.cp2k.CP2K): The CP2K object into which the input is
                parsed.
            filepath(str): Path to the CP2K input file.
        """
        self.storage_obj = cp2kcalc

        # Preprocess to spell out variables and to include stuff from other
        # files
        self.preprocess_input(filepath)

        # Gather the information from the input file
        self.fill_input_tree(filepath)
        return self.storage_obj

    def _pythonize_cp2k_names(self, name):
        """handles CP2K special characters:
           python cannot handle variables with
                   -
                   +
           and starting 0-9
        """
        if name[0].isdigit():
            name = "NUM" + name
        name = name.replace("-", "_")
        name = name.replace("+", "PLUS")
        return name

    def _set_keyword(self, section, keyword, value, path, full):

        try:
            keyword_attr = getattr(section, keyword)
            is_keyword = True
        except AttributeError:
            is_keyword = False
        # If keyword found, save it. If it can be repeated, then add it to a list.
        if is_keyword:
            keyword_attr_name = self._pythonize_cp2k_names(keyword)

            # If keyword can be repeated, then add it to list
            if keyword_attr_name in section._repeated_keywords:
                if isinstance(keyword_attr, list):
                    keyword_attr.append(value)
                else:
                    keyword_attr = [keyword_attr, value]
            # If keyword cannot be repeated, replace it
            else:
                setattr(section, self._pythonize_cp2k_names(keyword), value)
        # Keyword not found in the input tree, assuming it is a default keyword
        else:
            # See if section allows a default keyword
            try:
                section.Default_keyword
                is_default_keyword = True
            except AttributeError:
                is_default_keyword = False
            # If default keyword allowed, add it to list
            if is_default_keyword:
                section.Default_keyword.append(full)
            else:
                message = "The section {} does not contain the keyword {}, and there is no default keyword for this section".format(path,  keyword)
                logging.warning(message)
        return

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
        path = ""

        for line in self.input_lines:

            # Remove comments and whitespaces
            line = line.split('!', 1)[0].split('#', 1)[0].strip()

            # Skip empty lines
            if len(line) == 0:
                continue

            # Section ends
            if line.upper().startswith('&END'):
                section_stack.pop()
                section_objects.pop()
                if len(section_stack) > 0:
                    section = section_objects[-1]
            # Section starts
            elif line[0] == '&':
                parts = line.split(' ', 1)
                name = parts[0][1:].upper()
                # handling - + and 0-9
                name = self._pythonize_cp2k_names(name)

                # Creation of section objects
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

                # Save the section parameters
                if len(parts) > 1:
                    setattr(section, "Section_parameters", parts[1].strip())

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
                keyword_name = split[0].capitalize()

                self._set_keyword(section, self._pythonize_cp2k_names(keyword_name), keyword_value, path, full=line)
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
                    logging.warning("Could not find the include file '{}' stated in the CP2K input file. Continuing without it.".format(filepath))
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
                logging.debug("Variable '{}' found with value '{}'".format(name, value))
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
                    logging.error("Value for variable '{}' not set.".format(name))
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
