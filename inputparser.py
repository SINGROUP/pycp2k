#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Provides functions for creating a python classes from the cp2k_input.xml
file.
"""

import xml.etree.cElementTree as cElementTree
import utilities
import textwrap


#===============================================================================
def validify_section(string):
    """Modifies the section name so that it can be used as a valid attribute
    name in a python class.
    """
    original = string
    changed = False

    if "-" in string:
        changed = True
        string = string.replace("-", "_")

    if "+" in string:
        changed = True
        string = string.replace("+", "PLUS")

    if string[0].isdigit():
        changed = True
        string = "NUM" + string

    if '[' in string:
        changed = True
        string = string.replace("[", "_").replace("]", "")

    if changed:
        print("    Section {} replaced with {}".format(original, string))
    return string


#===============================================================================
def validify_keyword(string):
    """Modifies the keyword name so that it can be used as a valid attribute
    name in a python class.
    """
    original = string
    changed = False

    if "-" in string:
        changed = True
        string = string.replace("-", "_")

    if "+" in string:
        changed = True
        string = string.replace("+", "PLUS")

    if string[0].isdigit():
        changed = True
        string = "NUM" + string

    if '[' in string:
        changed = True
        string = string.replace("[", "_").replace("]", "")

    if changed:
        print("    Keyword {} replaced with {}".format(original, string))

    string = string.capitalize()
    return string


#===============================================================================
def create_docstring(item):
    description = item.find("DESCRIPTION")
    default_value = item.find("DEFAULT_VALUE")
    default_unit = item.find("DEFAULT_UNIT")

    # Description
    output = "        \"\"\"\n"
    if description is not None:
        if description.text is not None:
            for line in textwrap.wrap(description.text):
                output += "        " + line + "\n"

    # If the values are enumerated, document the possible values
    data_type = item.find("DATA_TYPE")
    if data_type.get("kind") == "keyword":
        output += "\n        Available values:\n"
        enumerations = data_type.find("ENUMERATION")
        for enum in enumerations.findall("ITEM"):
            output += "            " + enum.find("NAME").text + "\n"
            enum_description = enum.find("DESCRIPTION").text
            if enum_description is not None:
                for line in textwrap.wrap(enum_description):
                    output += "                " + line + "\n"

    # Default value
    if default_value is not None:
        if default_value.text is not None:
            output += "\n        Default value:\n"
            for line in textwrap.wrap(default_value.text):
                output += "            " + line + "\n"

    # Default unit
    if default_unit is not None:
        output += "\n        Default unit:\n"
        if default_unit.text is not None:
            for line in textwrap.wrap(default_unit.text):
                output += "            " + line + "\n"
    output += "        \"\"\"\n"
    return output


#===============================================================================
def recursive_class_creation(section, level, class_dictionary, version_dictionary):
    """Recursively goes throught the .xml file created by cp2k --xml command
    and creates a python class for each section. Keywords, default keywords,
    section parameters and subsections are stored as attributes.
    """
    default_keywords = {}
    repeated_default_keywords = {}
    keywords = {}
    repeated_keywords = {}
    subsections = {}
    repeated_subsections = {}
    repeated_aliases = {}
    aliases = {}
    attributes = []
    inp_name = ""

    # Initial string for each section of the class
    imports = ["from pycp2k.inputsection import InputSection"]
    docstring = ""
    properties = ""
    setters = ""
    public = (
        "    def __init__(self):\n"
        "        InputSection.__init__(self)\n"
    )
    private = ""
    class_subsections = ""
    functions = "\n"

    # The root with tag CP2K_INPUT doesn't have a name. It is hardcoded here.
    sectionname = section.find("NAME")
    if sectionname is None:
        class_name = "_CP2K_INPUT"
        inp_name = "CP2K_INPUT"
    else:
        class_name = sectionname.text
        inp_name = class_name
        class_name = validify_section(class_name)
        class_name = "_" + class_name.lower()

    # Start writing class body
    section_description = section.find("DESCRIPTION")
    # if section_description is not None and section_description.text is not None:
        # docstring += "    \"\"\"\n"
        # for line in textwrap.wrap(section_description.text):
            # docstring += "    " + line + "\n"
        # docstring += "    \"\"\"\n"
    # else:
        # docstring += "    \"\"\"\"\"\"\n"

    #---------------------------------------------------------------------------
    # Create attribute for section parameter
    section_parameters = section.find("SECTION_PARAMETERS")
    if section_parameters is not None:
        attributes.append("Section_parameters")
        public += "        self.Section_parameters = None\n"

        # Write the description for the section parameter
        # public += create_docstring(section_parameters)

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
                        public += "        self." + newname + " = []\n"
                        # public += create_docstring(keyword)
                        repeated_keywords[newname] = name
                    else:
                        public += "        self." + newname + " = None\n"
                        # public += create_docstring(keyword)
                        keywords[newname] = name

                # Create properties for aliases
                else:
                    if keyword.get("repeats") == "yes":
                        public += "        self." + newname + " = self." + default_name + "\n"
                        repeated_aliases[newname] = default_name
                    else:
                        aliases[newname] = default_name
                        properties += ("\n    @property\n"
                                       "    def " + newname + "(self):\n"
                                       "        \"\"\"\n"
                                       "        See documentation for " + default_name + "\n"
                                       "        \"\"\"\n"
                                       "        return self." + default_name + "\n")
                        setters += ("\n    @" + newname + ".setter\n"
                                    "    def " + newname + "(self, value):\n"
                                    "        self." + default_name + " = value\n")

    #---------------------------------------------------------------------------
    # Create a class attribute for all DEFAULT_KEYWORDS
    default_keyword = section.find("DEFAULT_KEYWORD")
    if default_keyword is not None:
        attributes.append("Default_keyword")
        # Special case for repeateable default_keywords. Create a dictionary of the
        # keyword and add a function for creating them.
        name = default_keyword.find("NAME").text
        newname = validify_keyword(name)

        if default_keyword.get("repeats") == "yes":
            public += "        self." + newname + " = []\n"
            # public += create_docstring(default_keyword)
            repeated_default_keywords[newname] = name
        else:
            public += "        self." + newname + " = None\n"
            # public += create_docstring(default_keyword)
            default_keywords[newname] = name

    #---------------------------------------------------------------------------
    # Create attribute for each subsection
    for subsection in section.findall("SECTION"):
        member_class_name = recursive_class_creation(subsection, level+1, class_dictionary, version_dictionary)
        member_name = subsection.find("NAME").text
        member_name = member_name.replace("-", "_")
        member_name = member_name.replace("+", "PLUS")
        if member_name[0].isdigit():
            member_name = "_" + member_name
        imports.append("from .{0} import {0}".format(member_class_name))

        # Special case for repeateable sections. Create a dictionary of the
        # subsections and add a function for creating them.
        if subsection.get("repeats") == "yes":
            class_subsections += "        self." + member_name + "_list = []\n"
            repeated_subsections[member_name] = member_class_name
            attributes.append(member_name + "_list")
        else:
            class_subsections += "        self." + member_name + " = " + member_class_name + "()\n"
            subsections[member_name] = subsection.find("NAME").text

    #---------------------------------------------------------------------------
    # Write a list of the stored variable names
    private += "        self._name = \"" + str(inp_name) + "\"\n"
    if len(keywords) != 0:
        private += "        self._keywords = " + str(keywords) + "\n"
    if len(repeated_keywords) != 0:
        private += "        self._repeated_keywords = " + str(repeated_keywords) + "\n"
    if len(default_keywords) != 0:
        private += "        self._default_keywords = " + str(default_keywords) + "\n"
    if len(repeated_default_keywords) != 0:
        private += "        self._repeated_default_keywords = " + str(repeated_default_keywords) + "\n"
    if len(subsections) != 0:
        private += "        self._subsections = " + str(subsections) + "\n"
    if len(repeated_subsections) != 0:
        private += "        self._repeated_subsections = " + str(repeated_subsections) + "\n"
    if len(aliases) != 0:
        private += "        self._aliases = " + str(aliases) + "\n"
    if len(repeated_aliases) != 0:
        private += "        self._repeated_aliases = " + str(repeated_aliases) + "\n"
    if len(attributes) != 0:
        private += "        self._attributes = " + str(attributes) + "\n"

    #---------------------------------------------------------------------------
    # Write a function for adding repeateable sections
    for repeated in repeated_subsections.items():
        attribute_name = repeated[0]
        attribute_class_name = repeated[1]
        functions += ("    def " + attribute_name + "_add(self, section_parameters=None):\n"
                      "        new_section = " + attribute_class_name + "()\n"
                      "        if section_parameters is not None:\n"
                      "            if hasattr(new_section, 'Section_parameters'):\n"
                      "                new_section.Section_parameters = section_parameters\n"
                      "        self." + attribute_name + "_list.append(new_section)\n"
                      "        return new_section\n\n")

    #---------------------------------------------------------------------------
    # The class names are not unique. Use numbering to identify classes.
    exists = False
    import_string = "\n".join(imports)
    class_string = docstring + public + class_subsections + private + functions + properties + setters
    version_number = version_dictionary.get(class_name)
    if version_number is None:
        version_dictionary[class_name] = 1
        class_dictionary[class_name+str(1)] = (import_string, class_string)
        return class_name+str(1)

    for version in range(version_number):
        old_class_body = class_dictionary[class_name+str(version + 1)]
        if old_class_body == class_string:
            exists = True
            version_number = version + 1
            break

    if not exists:
        version_dictionary[class_name] = version_number + 1
        class_dictionary[class_name+str(version_number + 1)] = (import_string, class_string)
        return class_name + str(version_number + 1)
    else:
        return class_name + str(version_number)


#===============================================================================
def main(xml_path):
    """Parses the classes and saves them to the package directory as
    parsedclasses.py.
    """
    # Start parsing here
    utilities.print_subtitle("CREATING INPUT STRUCTURE...")
    tree = cElementTree.parse(xml_path)
    root = tree.getroot()

    # Extract the cp2k version and revision
    version = root.find("CP2K_VERSION").text
    revision = root.find("COMPILE_REVISION").text

    class_dictionary = {}
    version_dictionary = {}
    recursive_class_creation(root, 0, class_dictionary, version_dictionary)

    # Put each class into its own module. This produces manu small files, but
    # this way it it easier for autocompletion to handle everything
    for class_name, class_body in class_dictionary.items():
        with open('pycp2k/classes/{}.py'.format(class_name), 'w') as file:
            file.write(class_body[0] + "\n\n\n")
            class_body_header = (
                "class " + class_name + "(InputSection):\n"
            )
            file.write(class_body_header)
            file.write(class_body[1])

    return (version, revision)

# Run main function by default
if __name__ == "__main__":
    main()
