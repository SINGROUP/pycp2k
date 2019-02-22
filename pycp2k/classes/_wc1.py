from pycp2k.inputsection import InputSection
from ._point14 import _point14


class _wc1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Rcut = None
        self.Atoms = []
        self.Points = self.Atoms
        self.POINT_list = []
        self._name = "WC"
        self._keywords = {'Rcut': 'RCUT'}
        self._repeated_keywords = {'Atoms': 'ATOMS'}
        self._repeated_subsections = {'POINT': '_point14'}
        self._repeated_aliases = {'Points': 'Atoms'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point14()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section

