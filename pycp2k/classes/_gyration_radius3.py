from pycp2k.inputsection import InputSection
from ._point40 import _point40


class _gyration_radius3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = []
        self.Points = self.Atoms
        self.Kinds = []
        self.POINT_list = []
        self._name = "GYRATION_RADIUS"
        self._repeated_keywords = {'Atoms': 'ATOMS', 'Kinds': 'KINDS'}
        self._repeated_subsections = {'POINT': '_point40'}
        self._repeated_aliases = {'Points': 'Atoms'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point40()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section

