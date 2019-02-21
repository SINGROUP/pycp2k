from pycp2k.inputsection import InputSection
from ._point53 import _point53


class _angle5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.POINT_list = []
        self._name = "ANGLE"
        self._keywords = {'Atoms': 'ATOMS'}
        self._repeated_subsections = {'POINT': '_point53'}
        self._aliases = {'Points': 'Atoms'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point53()
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
