from pycp2k.inputsection import InputSection
from ._plane1 import _plane1
from ._point8 import _point8


class _angle_plane_plane1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PLANE_list = []
        self.POINT_list = []
        self._name = "ANGLE_PLANE_PLANE"
        self._repeated_subsections = {'PLANE': '_plane1', 'POINT': '_point8'}
        self._attributes = ['PLANE_list', 'POINT_list']

    def PLANE_add(self, section_parameters=None):
        new_section = _plane1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PLANE_list.append(new_section)
        return new_section

    def POINT_add(self, section_parameters=None):
        new_section = _point8()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section

