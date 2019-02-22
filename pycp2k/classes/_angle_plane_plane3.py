from pycp2k.inputsection import InputSection
from ._plane3 import _plane3
from ._point42 import _point42


class _angle_plane_plane3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PLANE_list = []
        self.POINT_list = []
        self._name = "ANGLE_PLANE_PLANE"
        self._repeated_subsections = {'PLANE': '_plane3', 'POINT': '_point42'}
        self._attributes = ['PLANE_list', 'POINT_list']

    def PLANE_add(self, section_parameters=None):
        new_section = _plane3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PLANE_list.append(new_section)
        return new_section

    def POINT_add(self, section_parameters=None):
        new_section = _point42()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section

