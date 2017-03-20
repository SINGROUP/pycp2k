class InputSection(object):
    """Base class for all the automatically created classes that represents
    sections in the CP2K input structure.
    """
    def __init__(self):
        self._name = None
        self._keywords = {}
        self._repeated_keywords = {}
        self._default_keywords = {}
        self._repeated_default_keywords = {}
        self._subsections = {}
        self._repeated_subsections = {}
        self._aliases = {}
        self._repeated_aliases = {}
        self._attributes = []

    def __getattr__(self, attr):
        """Called when self.attr doesn't exist
        """
        message = (
            "The attribute {0} does not exist. This is either a typo (remember"
            " that section names should be in uppercase, and keywords should be"
            " capitalized) or you are trying to access a repeatable item that"
            " should be first added with {0}_add() which returns the newly"
            " added object for that section."
        ).format(attr)
        raise AttributeError(message)

    def _format_variable(self, item):
        # The boolean values are reformatted
        if isinstance(item, bool):
            if item:
                item = "TRUE"
            else:
                item = "FALSE"
        return str(item)

    def _parse_default_keyword(self, item, level):
        """Parses default keywords into sensible input sections."""
        if type(item) is list:
            output = (level + 1) * "  "
            for i, value in enumerate(item):
                output += str(value)
                if i != len(item)-1:
                    output += " "
            output += "\n"
            return output
        else:
            return (level + 1) * "  " + self._format_variable(item) + "\n"

    def _parse_repeatable_default_keyword(self, item, level):
        """Parses repeatable default keywords into sensible input sections."""
        if type(item) is list:
            output = ""
            for i, value in enumerate(item):
                output += (level + 1) * "  "
                if type(value) is list:
                    for j, sub_value in enumerate(value):
                        output += str(sub_value)
                        if j != len(value)-1:
                            output += " "
                else:
                    output += self._format_variable(value)
                output += "\n"
            return output
        else:
            return (level + 1) * "  " + self._format_variable(item) + "\n"

    def _parse_keyword(self, item, name, level):
        """Parses non-repeatable keywords into sensible input sections."""
        if type(item) is list:
            output = (level + 1) * "  " + name
            for value in item:
                if type(value) is list:
                    for sub_value in value:
                        output += " " + str(sub_value)
                else:
                    output += " " + str(value)
            output += "\n"
            return output
        else:
            return (level + 1) * "  " + name + " " + self._format_variable(item) + "\n"

    def _parse_repeatable_keyword(self, item, name, level):
        """Parses repeatable keywords into sensible input sections."""
        if type(item) is list:
            output = ""
            for i, value in enumerate(item):
                output += (level + 1) * "  " + name
                if type(value) is list:
                    for sub_value in value:
                        output += " " + str(sub_value)
                else:
                    output += " " + str(value)
                output += "\n"
            return output
        else:
            return (level + 1) * "  " + name + " " + self._format_variable(item) + "\n"

    def _check_typos(self):
        for attribute in self.__dict__.keys():
            typos_found = True
            if attribute in iter(self._keywords.keys()):
                typos_found = False
            elif attribute in iter(self._repeated_keywords.keys()):
                typos_found = False
            elif attribute in iter(self._subsections.keys()):
                typos_found = False
            elif attribute in iter(self._repeated_subsections.keys()):
                typos_found = False
            elif attribute in iter(self._aliases.keys()):
                typos_found = False
            elif attribute in iter(self._repeated_aliases.keys()):
                typos_found = False
            elif attribute in self._attributes:
                typos_found = False
            elif attribute[0] == "_":
                typos_found = False
            if typos_found:
                raise Exception((
                    "Nonexisting keyword '{}' defined in CP2K input tree"
                    " section '{}'. This might be a typo (remember that section"
                    " names should be in uppercase, and keywords should be"
                    " capitalized)."
                ).format(attribute, self._name))

    def _print_input(self, level):

        # Check if any undefined items have been created. These are usually typos.
        self._check_typos()

        inp = ""
        # Non-repeatable default keywords
        for attname, realname in self._default_keywords.items():
            value = self.__dict__[attname]
            if value is not None:
                if not (type(value) is list and not value):
                    parsed = self._parse_default_keyword(value, level)
                    inp += parsed

        # Repeatable default keywords
        for attname, realname in self._repeated_default_keywords.items():
            keyword = self.__dict__[attname]
            if keyword is not None:
                if not (type(keyword) is list and not keyword):
                    parsed = self._parse_repeatable_default_keyword(keyword, level)
                    inp += parsed

        # Non-repeatable keywords
        for attname, realname in self._keywords.items():
            value = self.__dict__[attname]
            if value is not None:
                if not (type(value) is list and not value):
                    parsed = self._parse_keyword(value, realname, level)
                    inp += parsed

        # Repeatable keywords
        for attname, realname in self._repeated_keywords.items():
            keyword = self.__dict__[attname]
            if keyword is not None:
                if not (type(keyword) is list and not keyword):
                    parsed = self._parse_repeatable_keyword(keyword, realname, level)
                    inp += parsed

        # Non-repeatable subsections
        for attname, realname in self._subsections.items():
            value = self.__dict__[attname]
            substring = value._print_input(level + 1)
            if substring != "":
                inp += substring + "\n"

        # Repeatable subsections
        for attname, realname in self._repeated_subsections.items():
            for subsection in self.__dict__[attname + "_list"]:
                if subsection is not None:
                    substring = subsection._print_input(level + 1)
                    if substring != "":
                        inp += substring + "\n"

        # Don't print the CP2K_INPUT root
        if level != -1:
            # Header and footer
            has_section_parameter = False
            inp_header = level * "  " + "&" + self._name
            if hasattr(self, "Section_parameters"):
                if self.Section_parameters is not None:
                    parsed = self._parse_default_keyword(self.Section_parameters, -1)
                    inp_header += " " + parsed
                    has_section_parameter = True
            if not has_section_parameter:
                inp_header += "\n"
            inp_footer = level * "  " + "&END " + self._name

            if not has_section_parameter and inp == "":
                return ""
            else:
                return inp_header + inp + inp_footer
        else:
            return inp
