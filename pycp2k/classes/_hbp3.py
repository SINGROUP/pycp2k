from pycp2k.inputsection import InputSection
from ._point49 import _point49


class _hbp3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Rcut = None
        self.Shift = None
        self.Npoints = None
        self.Atoms = []
        self.Points = self.Atoms
        self.POINT_list = []
        self._name = "HBP"
        self._keywords = {'Shift': 'SHIFT', 'Npoints': 'NPOINTS', 'Rcut': 'RCUT'}
        self._repeated_keywords = {'Atoms': 'ATOMS'}
        self._repeated_subsections = {'POINT': '_point49'}
        self._repeated_aliases = {'Points': 'Atoms'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point49()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section

