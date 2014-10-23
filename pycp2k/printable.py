#! /usr/bin/env python

"""Defines a printing interface which all classes parsed by inputparser.py will
follow."""


#===============================================================================
class printable(object):

    def parse_default_keyword(self, item, level):
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
            return (level + 1) * "  " + str(item) + "\n"

    def parse_repeatable_default_keyword(self, item, level):
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
                    output += str(value)
                output += "\n"
            return output
        else:
            return (level + 1) * "  " + str(item) + "\n"

    def parse_keyword(self, item, name, level):
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
            return (level + 1) * "  " + name + " " + str(item) + "\n"

    def parse_repeatable_keyword(self, item, name, level):
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
            return (level + 1) * "  " + name + " " + str(item) + "\n"

    def check_typos(self):
        for attribute in self.__dict__.iterkeys():
            typos_found = True
            if attribute in self._keywords.iterkeys():
                typos_found = False
            elif attribute in self._repeated_keywords.iterkeys():
                typos_found = False
            elif attribute in self._subsections.iterkeys():
                typos_found = False
            elif attribute in self._repeated_subsections.iterkeys():
                typos_found = False
            elif attribute in self._aliases.iterkeys():
                typos_found = False
            elif attribute in self._repeated_aliases.iterkeys():
                typos_found = False
            elif attribute in self._attributes:
                typos_found = False
            elif attribute[0] == "_":
                typos_found = False
            if typos_found:
                raise Exception("Nonexisting keyword '" + attribute + "' defined in CP2K input tree section '" + self._name + "'. This might be a typo.")

    def print_input(self, level):

        # Check if any undefined items have been created. These are usually typos.
        self.check_typos()

        inp = ""
        # Non-repeatable default keywords
        for attname, realname in self._default_keywords.iteritems():
            value = self.__dict__[attname]
            if value is not None:
                if not (type(value) is list and not value):
                    parsed = self.parse_default_keyword(value, level)
                    inp += parsed

        # Repeatable default keywords
        for attname, realname in self._repeated_default_keywords.iteritems():
            keyword = self.__dict__[attname]
            if keyword is not None:
                if not (type(keyword) is list and not keyword):
                    parsed = self.parse_repeatable_default_keyword(keyword, level)
                    inp += parsed

        # Non-repeatable keywords
        for attname, realname in self._keywords.iteritems():
            value = self.__dict__[attname]
            if value is not None:
                if not (type(value) is list and not value):
                    parsed = self.parse_keyword(value, realname, level)
                    inp += parsed

        # Repeatable keywords
        for attname, realname in self._repeated_keywords.iteritems():
            keyword = self.__dict__[attname]
            if keyword is not None:
                if not (type(keyword) is list and not keyword):
                    parsed = self.parse_repeatable_keyword(keyword, realname, level)
                    inp += parsed

        # Non-repeatable subsections
        for attname, realname in self._subsections.iteritems():
            value = self.__dict__[attname]
            substring = value.print_input(level + 1)
            if substring != "":
                inp += substring + "\n"

        # Repeatable subsections
        for attname, realname in self._repeated_subsections.iteritems():
            for subsection in self.__dict__[attname + "_list"]:
                if subsection is not None:
                    substring = subsection.print_input(level + 1)
                    if substring != "":
                        inp += substring + "\n"

        # Don't print the CP2K_INPUT root
        if level != -1:
            # Header and footer
            has_section_parameter = False
            inp_header = level * "  " + "&" + self._name
            if hasattr(self, "Section_parameters"):
                if self.Section_parameters is not None:
                    parsed = self.parse_default_keyword(self.Section_parameters, -1)
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
