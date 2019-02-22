from pycp2k.inputsection import InputSection
from ._point52 import _point52


class _distance4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Axis = None
        self.POINT_list = []
        self._name = "DISTANCE"
        self._keywords = {'Atoms': 'ATOMS', 'Axis': 'AXIS'}
        self._repeated_subsections = {'POINT': '_point52'}
        self._aliases = {'Points': 'Atoms'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point52()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section


    @property
    def Points(self):
        """
        See documentation for Atoms
        """
        return self.Atoms

    @Points.setter
    def Points(self, value):
        self.Atoms = value
