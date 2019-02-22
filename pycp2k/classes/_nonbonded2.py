from pycp2k.inputsection import InputSection
from ._lennard_jones3 import _lennard_jones3
from ._williams3 import _williams3
from ._goodwin3 import _goodwin3
from ._genpot3 import _genpot3


class _nonbonded2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.LENNARD_JONES_list = []
        self.WILLIAMS_list = []
        self.GOODWIN_list = []
        self.GENPOT_list = []
        self._name = "NONBONDED"
        self._repeated_subsections = {'LENNARD_JONES': '_lennard_jones3', 'GOODWIN': '_goodwin3', 'WILLIAMS': '_williams3', 'GENPOT': '_genpot3'}
        self._attributes = ['LENNARD_JONES_list', 'WILLIAMS_list', 'GOODWIN_list', 'GENPOT_list']

    def LENNARD_JONES_add(self, section_parameters=None):
        new_section = _lennard_jones3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LENNARD_JONES_list.append(new_section)
        return new_section

    def GOODWIN_add(self, section_parameters=None):
        new_section = _goodwin3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.GOODWIN_list.append(new_section)
        return new_section

    def WILLIAMS_add(self, section_parameters=None):
        new_section = _williams3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.WILLIAMS_list.append(new_section)
        return new_section

    def GENPOT_add(self, section_parameters=None):
        new_section = _genpot3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.GENPOT_list.append(new_section)
        return new_section

