from pycp2k.inputsection import InputSection
from ._plane4 import _plane4
from ._point59 import _point59


class _angle_plane_plane4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PLANE_list = []
        self.POINT_list = []
        self._name = "ANGLE_PLANE_PLANE"
        self._repeated_subsections = {'PLANE': '_plane4', 'POINT': '_point59'}
        self._attributes = ['PLANE_list', 'POINT_list']

    def PLANE_add(self, section_parameters=None):
        new_section = _plane4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PLANE_list.append(new_section)
        return new_section

    def POINT_add(self, section_parameters=None):
        new_section = _point59()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section

