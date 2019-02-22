from pycp2k.inputsection import InputSection
from ._point26 import _point26


class _bond_rotation2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.P1_bond1 = None
        self.P2_bond1 = None
        self.P1_bond2 = None
        self.P2_bond2 = None
        self.POINT_list = []
        self._name = "BOND_ROTATION"
        self._keywords = {'P2_bond2': 'P2_BOND2', 'P2_bond1': 'P2_BOND1', 'P1_bond1': 'P1_BOND1', 'P1_bond2': 'P1_BOND2'}
        self._repeated_subsections = {'POINT': '_point26'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point26()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section

