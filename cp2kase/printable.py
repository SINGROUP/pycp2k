#! /usr/bin/env python

"""Defines a printing interface which all classes parsed by inputparser.py will
follow."""


#===============================================================================
class printable(object):

    def __init__(self):
        self.default_keywords = []
        self.repeated_default_keywords = []
        self.keywords = []
        self.repeated_keywords = []
        self.subsections = []
        self.repeated_subsections = []
        self.inp_name = ""

    def print_input(self, level):

        inp = ""
        # Non-repeatable default keywords
        for attname, realname in self.default_keywords:
            value = self.__dict__[attname]
            if value is not None:
                inp += (level+1)*"  " + str(value) + "\n"

        # Repeatable default keywords
        for attname, realname in self.repeated_default_keywords:
            value = self.__dict__[attname]
            if value is not None:
                inp += (level + 1) * "  " + realname + " " + str(value) + "\n"
            for keyword in self.__dict__["list" + attname]:
                if keyword is not None:
                    inp += (level + 1) * "  " + str(keyword) + "\n"

        # Non-repeatable keywords
        for attname, realname in self.keywords:
            value = self.__dict__[attname]
            if value is not None:
                inp += (level+1)*"  " + realname + " " + str(value) + "\n"

        # Repeatable keywords
        for attname, realname in self.repeated_keywords:
            value = self.__dict__[attname]
            if value is not None:
                inp += (level + 1) * "  " + realname + " " + str(value) + "\n"
            for keyword in self.__dict__["list" + attname]:
                if keyword is not None:
                    inp += (level + 1) * "  " + realname + " " + str(keyword) + "\n"

        # Non-repeatable subsections
        for attname, realname in self.subsections:
            value = self.__dict__[attname]
            substring = value.print_input(level + 1)
            if substring != "":
                inp += substring + "\n"

        # Repeatable subsections
        for attname, realname in self.repeated_subsections:
            value = self.__dict__[attname]
            substring = value.print_input(level + 1)
            if substring != "":
                inp += substring + "\n"
            for subsection in self.__dict__["list" + attname]:
                if subsection is not None:
                    substring = subsection.print_input(level + 1)
                    if substring != "":
                        inp += substring + ""

        # Don't print the CP2K_INPUT root
        if level != -1:
            # Header and footer
            has_section_parameter = False
            inp_header = level * "  " + "&" + self.name
            if hasattr(self, "_SECTION_PARAMETERS"):
                if self._SECTION_PARAMETERS is not None:
                    inp_header += " " + self._SECTION_PARAMETERS + "\n"
                    has_section_parameter = True
            if not has_section_parameter:
                inp_header += "\n"
            inp_footer = level * "  " + "&END " + self.name

            if not has_section_parameter and inp == "":
                return ""
            else:
                return inp_header + inp + inp_footer
        else:
            return inp
