from pycp2k.inputsection import InputSection
from ._plane2 import _plane2
from ._point25 import _point25


class _angle_plane_plane2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PLANE_list = []
        self.POINT_list = []
        self._name = "ANGLE_PLANE_PLANE"
        self._repeated_subsections = {'PLANE': '_plane2', 'POINT': '_point25'}
        self._attributes = ['PLANE_list', 'POINT_list']

    def PLANE_add(self, section_parameters=None):
        new_section = _plane2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PLANE_list.append(new_section)
        return new_section

    def POINT_add(self, section_parameters=None):
        new_section = _point25()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section

