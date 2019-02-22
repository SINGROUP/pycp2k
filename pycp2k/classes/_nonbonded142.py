from pycp2k.inputsection import InputSection
from ._lennard_jones4 import _lennard_jones4
from ._williams4 import _williams4
from ._goodwin4 import _goodwin4
from ._genpot4 import _genpot4


class _nonbonded142(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.LENNARD_JONES_list = []
        self.WILLIAMS_list = []
        self.GOODWIN_list = []
        self.GENPOT_list = []
        self._name = "NONBONDED14"
        self._repeated_subsections = {'LENNARD_JONES': '_lennard_jones4', 'GOODWIN': '_goodwin4', 'WILLIAMS': '_williams4', 'GENPOT': '_genpot4'}
        self._attributes = ['LENNARD_JONES_list', 'WILLIAMS_list', 'GOODWIN_list', 'GENPOT_list']

    def LENNARD_JONES_add(self, section_parameters=None):
        new_section = _lennard_jones4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.LENNARD_JONES_list.append(new_section)
        return new_section

    def GOODWIN_add(self, section_parameters=None):
        new_section = _goodwin4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.GOODWIN_list.append(new_section)
        return new_section

    def WILLIAMS_add(self, section_parameters=None):
        new_section = _williams4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.WILLIAMS_list.append(new_section)
        return new_section

    def GENPOT_add(self, section_parameters=None):
        new_section = _genpot4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.GENPOT_list.append(new_section)
        return new_section

