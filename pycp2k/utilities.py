#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Misc. utility functions."""
import textwrap


#===============================================================================
def print_title(header, width=80):
    """Styles a title to be printed into console.
    """
    title = "|" + str((width-2)*"=")+"|\n"
    title += "|"
    space = width-len(header)-2
    pre_space = space/2
    post_space = space-pre_space
    title += str((pre_space)*" ")
    title += header
    title += str((post_space)*" ")
    title += "|\n"
    title += "|" + str((width-2)*"=")+"|"
    return title


#===============================================================================
def print_message(message, width=80):
    """Styles a message to be printed into console.
    """
    return textwrap.fill(message, width=width)


#===============================================================================
def print_warning(message, width=80):
    """Returns a styled warning message to be printed into console.
    """
    title = "    |" + str((width-2-8)*"=")+"|\n"
    title += "    |"
    space = width-len("WARNING")-2-8
    pre_space = space/2
    post_space = space-pre_space
    title += str((pre_space)*" ")
    title += "WARNING"
    title += str((post_space)*" ")
    title += "|\n"
    title += "    |" + str((width-2-8)*"=")+"|\n"
    lines = textwrap.wrap(message, width=72)
    for line in lines:
        line = "    " + line
        title += line + "\n"
    return title
