from pycp2k.inputsection import InputSection
from ._point36 import _point36


class _angle4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.POINT_list = []
        self._name = "ANGLE"
        self._keywords = {'Atoms': 'ATOMS'}
        self._repeated_subsections = {'POINT': '_point36'}
        self._aliases = {'Points': 'Atoms'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point36()
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
