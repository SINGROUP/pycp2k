from pycp2k.inputsection import InputSection
from ._lennard_jones2 import _lennard_jones2
from ._williams2 import _williams2
from ._goodwin2 import _goodwin2
from ._genpot2 import _genpot2


class _nonbonded141(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.LENNARD_JONES_list = []
        self.WILLIAMS_list = []
        self.GOODWIN_list = []
        self.GENPOT_list = []
        self._name = "NONBONDED14"
        self._repeated_subsections = {'LENNARD_JONES': '_lennard_jones2', 'GOODWIN': '_goodwin2', 'WILLIAMS': '_williams2', 'GENPOT': '_genpot2'}
        self._attributes = ['LENNARD_JONES_list', 'WILLIAMS_list', 'GOODWIN_list', 'GENPOT_list']

    def LENNARD_JONES_add(self, section_parameters=None):
        new_section = _lennard_jones2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LENNARD_JONES_list.append(new_section)
        return new_section

    def GOODWIN_add(self, section_parameters=None):
        new_section = _goodwin2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.GOODWIN_list.append(new_section)
        return new_section

    def WILLIAMS_add(self, section_parameters=None):
        new_section = _williams2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.WILLIAMS_list.append(new_section)
        return new_section

    def GENPOT_add(self, section_parameters=None):
        new_section = _genpot2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.GENPOT_list.append(new_section)
        return new_section

