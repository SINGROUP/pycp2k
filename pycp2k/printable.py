#! /usr/bin/env python

"""Defines a printing interface which all classes parsed by inputparser.py will
follow."""


#===============================================================================
class printable(object):

    def __init__(self):
        self._default_keywords = []
        self._repeated_default_keywords = []
        self._keywords = []
        self._repeated_keywords = []
        self._subsections = []
        self._repeated_subsections = []
        self._name = ""

    def print_input(self, level):

        inp = ""
        # Non-repeatable default keywords
        for attname, realname in self._default_keywords:
            value = self.__dict__[attname]
            if value is not None:
                inp += (level+1)*"  " + str(value) + "\n"

        # Repeatable default keywords
        for attname, realname in self._repeated_default_keywords:
            for keyword in self.__dict__["list_" + attname]:
                if keyword is not None:
                    inp += (level + 1) * "  " + str(keyword) + "\n"

        # Non-repeatable keywords
        for attname, realname in self._keywords:
            value = self.__dict__[attname]
            if value is not None:
                inp += (level+1)*"  " + realname + " " + str(value) + "\n"

        # Repeatable keywords
        for attname, realname in self._repeated_keywords:
            for keyword in self.__dict__["list_" + attname]:
                if keyword.value is not None:
                    inp += (level + 1) * "  " + realname + " " + str(keyword.value) + "\n"

        # Non-repeatable subsections
        for attname, realname in self._subsections:
            value = self.__dict__[attname]
            substring = value.print_input(level + 1)
            if substring != "":
                inp += substring + "\n"

        # Repeatable subsections
        for attname, realname in self._repeated_subsections:
            for subsection in self.__dict__["list_" + attname]:
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
                    inp_header += " " + self.Section_parameters + "\n"
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
