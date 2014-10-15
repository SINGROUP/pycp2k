#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Misc. utility functions."""
import textwrap


#===============================================================================
def make_title(title, width=80):
    """Styles a title to be printed into console.
    """
    space = width-len(title)-4
    pre_space = space/2-1
    post_space = space-pre_space
    line = "|" + str((pre_space)*"=") + " "
    line += title
    line += " " + str((post_space)*"=") + "|"
    return line


#===============================================================================
def print_subtitle(title, width=80):
    """Styles a title to be printed into console.
    """
    space = width-len(title)-4
    pre_space = space/2-1
    post_space = space-pre_space
    line = "|" + str((pre_space)*"-") + " "
    line += title
    line += " " + str((post_space)*"-") + "|"
    print line


#===============================================================================
def make_message(message, width=80, spaces=0):
    """Styles a message to be printed into console.
    """
    wrapper = textwrap.TextWrapper(width=width-6)
    lines = wrapper.wrap(message)
    styled_message = ""
    for line in lines:
        styled_message += spaces*" " + "|  " + line + (width-6-len(line))*" " + "  |\n"
    styled_message += spaces*" " + "|" + (width-2)*"-" + "|"
    return styled_message


#===============================================================================
def print_title(title, width=80):
    """Prints styled title into console.
    """
    print make_title(title, width=width)


#===============================================================================
def print_message(title, message, width=80):
    """Returns a styled warning message to be printed into console.
    """
    print make_title(title) + "\n" + make_message(message) + "\n"


#===============================================================================
def print_warning(message, width=80):
    """Returns a styled warning message to be printed into console.
    """
    print "\n        " + make_title("WARNING", width=64) + "\n" + make_message(message, width=64, spaces=8) + "\n"


#===============================================================================
def print_error(message, width=80):
    """Returns a styled warning message to be printed into console.
    """
    print "\n        " + make_title("ERROR", width=64) + "\n" + make_message(message, width=64, spaces=8) + "\n"
