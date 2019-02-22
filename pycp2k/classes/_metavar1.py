from pycp2k.inputsection import InputSection
from ._wall1 import _wall1


class _metavar1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Lambda = None
        self.Mass = None
        self.Gamma = None
        self.Scale = None
        self.Colvar = None
        self.WALL_list = []
        self._name = "METAVAR"
        self._keywords = {'Gamma': 'GAMMA', 'Scale': 'SCALE', 'Colvar': 'COLVAR', 'Lambda': 'LAMBDA', 'Mass': 'MASS'}
        self._repeated_subsections = {'WALL': '_wall1'}
        self._aliases = {'Width': 'Scale'}
        self._attributes = ['WALL_list']

    def WALL_add(self, section_parameters=None):
        new_section = _wall1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.WALL_list.append(new_section)
        return new_section


    @property
    def Width(self):
        """
        See documentation for Scale
        """
        return self.Scale

    @Width.setter
    def Width(self, value):
        self.Scale = value
