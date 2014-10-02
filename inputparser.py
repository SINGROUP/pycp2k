#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Provides a function for creating an cp2k input structure from an xml file."""

import xml.etree.cElementTree as cElementTree
from subprocess import call


def validify_section(string):
    string = string.replace("-", "HYPMIN")
    string = string.replace("+", "PLUS")
    if string[0].isdigit():
        string = "NUM" + string
    return string


def validify_keyword(string):
    string = string.replace("-", "HYPMIN")
    string = string.replace("+", "PLUS")
    string = "_" + string
    return string


def recursive_class_creation(section, level, class_dictionary, version_dictionary):
    """
    """
    default_keywords = []
    repeated_default_keywords = []
    keywords = []
    repeated_keywords = []
    subsections = []
    repeated_subsections = []
    inp_name = ""

    # The root with tag CP2K_INPUT doesn't have a name. It is hardcoded here.
    sectionname = section.find("NAME")
    if sectionname is None:
        class_name = "CP2K_INPUT"
        inp_name = "CP2K_INPUT"
    else:
        class_name = sectionname.text
        inp_name = class_name
        class_name = validify_section(class_name)
        class_name = class_name.lower()

    # Start writing class body
    class_body = ""
    section_description = section.find("DESCRIPTION")
    if section_description is not None and section_description.text is not None:
        class_body += "    \"\"\"" + section_description.text + "\"\"\"\n"
    else:
        class_body += "    \"\"\"\"\"\"\n"
    class_body += "    def __init__(self):\n"

    # Create attribute for section parameter
    section_parameters = section.find("SECTION_PARAMETERS")
    if section_parameters is not None:
        class_body += "        self._SECTION_PARAMETERS" + " = None\n"

    #---------------------------------------------------------------------------
    # Create attribute for all the keywords
    for keyword in section.findall("KEYWORD"):

        # First find out the default name and whether the attribute is visible or not
        default_name = ""
        visible = True
        for keyname in keyword.findall("NAME"):
            keytype = keyname.get("type")
            name = keyname.text
            newname = validify_keyword(name)
            if keytype == "default":
                default_name = newname
                if name.startswith("__"):
                    visible = False

        # Now store the keywords as class attributes
        if visible:
            for keyname in keyword.findall("NAME"):
                name = keyname.text
                newname = validify_keyword(name)

                # Create original attribute for the default keyname
                if newname == default_name:

                    # Special case for repeateable keywords.
                    if keyword.get("repeats") == "yes":
                        class_body += "        self.list" + newname + " = []\n"
                        class_body += "        self." + newname + " = None\n"
                        repeated_keywords.append((newname, name))
                    else:
                        class_body += "        self." + newname + " = None"
                        keywords.append((newname, name))

                    # Write the description for the keyword
                    description = keyword.find("DESCRIPTION").text
                    if description is not None:
                        class_body += "    # " + description + "\n"
                    else:
                        class_body += "\n"

                # Create pointer for the aliases
                else:
                    class_body += "        self." + newname + " = self." + default_name + "\n"
                    if keyword.get("repeats") == "yes":
                        class_body += "        self.list" + newname + " = self.list" + default_name + "\n"
                        repeated_keywords.append((newname, name))
                    else:
                        keywords.append((newname, name))

    #---------------------------------------------------------------------------
    # Create a class attribute for all DEFAULT_KEYWORDS
    for default_keyword in section.findall("DEFAULT_KEYWORD"):

        # First find out the default name and whether the attribute is visible or not
        default_name = ""
        visible = True
        for keyname in default_keyword.findall("NAME"):
            keytype = keyname.get("type")
            name = keyname.text
            if keytype == "default":
                newname = validify_keyword(name)
                default_name = newname
                if name.startswith("__"):
                    visible = False

        # Now store the keywords as class attributes
        if visible:
            for keyname in default_keyword.findall("NAME"):
                name = keyname.text
                newname = validify_keyword(name)

                # Create original attribute for the default keyname
                if newname == default_name:

                    # Special case for repeateable default_keywords. Create a dictionary of the
                    # keyword and add a function for creating them.
                    if default_keyword.get("repeats") == "yes":
                        class_body += "        self.list" + newname + " = []\n"
                        class_body += "        self." + newname + " = None"
                        repeated_default_keywords.append((newname, name))
                    else:
                        class_body += "        self." + newname + " = None"
                        default_keywords.append((newname, name))

                    # Write the description for the keyword
                    description = default_keyword.find("DESCRIPTION").text
                    if description is not None:
                        class_body += "    # " + description + "\n"
                    else:
                        class_body += "\n"

                # Create pointer for the aliases
                else:
                    class_body += "        self." + newname + " = self." + default_name + "\n"
                    if default_keyword.get("repeats") == "yes":
                        class_body += "        self.list" + newname + " = self.list" + default_name + "\n"
                        repeated_default_keywords.append((newname, name))
                    else:
                        default_keywords.append((newname, name))

    #---------------------------------------------------------------------------
    # Create attribute for each subsection
    for subsection in section.findall("SECTION"):
        member_class_name = recursive_class_creation(subsection, level+1, class_dictionary, version_dictionary)
        member_name = subsection.find("NAME").text
        member_name = member_name.replace("-", "_")
        member_name = member_name.replace("+", "PLUS")
        if member_name[0].isdigit():
            member_name = "_" + member_name

        # Special case for repeateable sections. Create a dictionary of the
        # subsections and add a function for creating them.
        if subsection.get("repeats") == "yes":
            class_body += "        self.list" + member_name + " = []\n"
            class_body += "        self." + member_name + " = " + member_class_name + "()\n"
            repeated_subsections.append((member_name, member_class_name))
        else:
            class_body += "        self." + member_name + " = " + member_class_name + "()\n"
            subsections.append((member_name, subsection.find("NAME").text))
    #---------------------------------------------------------------------------
    # Write a list of the stored variable names
    class_body += "        self.name = \"" + str(inp_name) + "\"\n"
    class_body += "        self.keywords = " + str(keywords) + "\n"
    class_body += "        self.repeated_keywords = " + str(repeated_keywords) + "\n"
    class_body += "        self.default_keywords = " + str(default_keywords) + "\n"
    class_body += "        self.repeated_default_keywords = " + str(repeated_default_keywords) + "\n"
    class_body += "        self.subsections = " + str(subsections) + "\n"
    class_body += "        self.repeated_subsections = " + str(repeated_subsections) + "\n"

    # Empty initializer needs to have at least "pass" in it
    if len(section.findall("KEYWORD")) == 0 and len(section.findall("SECTION")) == 0:
        class_body += "        pass\n"

    # Write a function for adding repeateable sections
    for repeated in repeated_subsections:
        attribute_name = repeated[0]
        attribute_class_name = repeated[1]
        class_body += "\n    def add" + attribute_name + "(self):\n"
        class_body += "        new_section = " + attribute_class_name + "()\n"
        class_body += "        self.list" + attribute_name + ".append(new_section)\n"
        class_body += "        return new_section\n"

    # Write a function for adding repeateable keywords
    for repeated in repeated_keywords:
        class_body += "\n    def add" + repeated[0] + "(self, value):\n"
        class_body += "        self.list" + repeated[0] + ".append(value)\n"

    # Write a function for adding repeateable default keywords
    for repeated in repeated_default_keywords:
        class_body += "\n    def add" + repeated[0] + "(self, value):\n"
        class_body += "        self.list" + repeated[0] + ".append(value)\n"

    # Write a function for printing original CP2K input files
    class_body += "\n    def print_input(self, level):\n"
    class_body += "        return printable.print_input(self, level)\n"

    #---------------------------------------------------------------------------
    # The class names are not unique.
    exists = False
    version_number = version_dictionary.get(class_name)
    if version_number is None:
        version_dictionary[class_name] = 1
        class_dictionary[class_name+str(1)] = class_body
        return class_name+str(1)

    for version in range(version_number):
        old_class_body = class_dictionary[class_name+str(version + 1)]
        if old_class_body == class_body:
            exists = True
            version_number = version + 1
            break

    if not exists:
        version_dictionary[class_name] = version_number + 1
        class_dictionary[class_name+str(version_number + 1)] = class_body
        return class_name+str(version_number + 1)
    else:
        return class_name+str(version_number)


def main():
    """
    """
    # First call cp2k --xml to create the xml file of the input structure
    call(["cp2k", "--xml"])

    # Start parsing here
    tree = cElementTree.parse("cp2k_input.xml")
    root = tree.getroot()
    module_header = (
        "#! /usr/bin/env python\n"
        "# -*- coding: utf-8 -*-\n\n"
        "\"\"\"This module holds all the classes parsed from xml file created with command\ncp2k --xml\"\"\"\n\n"
        "from pycp2k.printable import printable\n"
    )
    class_dictionary = {}
    version_dictionary = {}
    recursive_class_creation(root, 0, class_dictionary, version_dictionary)

    # Write one modeule containing all the parsed classes.
    with open('pycp2k/parsedclasses.py', 'w') as file:
        file.write(module_header)
        for class_name, class_body in class_dictionary.iteritems():
            class_body_header = (
                "\n\nclass " + class_name + "(printable):\n"
            )
            file.write(class_body_header)
            file.write(class_body)
