from pycp2k.inputsection import InputSection
from ._point51 import _point51


class _conditioned_distance3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms_distance = []
        self.Atoms_from = []
        self.Points_from = self.Atoms_from
        self.Atoms_to = []
        self.Points_to = self.Atoms_to
        self.Kinds_from = []
        self.Kinds_to = []
        self.R0 = None
        self.Nn = None
        self.Nd = None
        self.Lambda = None
        self.POINT_list = []
        self._name = "CONDITIONED_DISTANCE"
        self._keywords = {'Nd': 'ND', 'Nn': 'NN', 'Lambda': 'LAMBDA', 'R0': 'R0'}
        self._repeated_keywords = {'Atoms_from': 'ATOMS_FROM', 'Atoms_to': 'ATOMS_TO', 'Kinds_from': 'KINDS_FROM', 'Atoms_distance': 'ATOMS_DISTANCE', 'Kinds_to': 'KINDS_TO'}
        self._repeated_subsections = {'POINT': '_point51'}
        self._aliases = {'R_0': 'R0', 'Expon_denominator': 'Nd', 'Expon_numerator': 'Nn'}
        self._repeated_aliases = {'Points_from': 'Atoms_from', 'Points_to': 'Atoms_to'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point51()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.POINT_list.append(new_section)
        return new_section


    @property
    def R_0(self):
        """
        See documentation for R0
        """
        return self.R0

    @property
    def Expon_numerator(self):
        """
        See documentation for Nn
        """
        return self.Nn

    @property
    def Expon_denominator(self):
        """
        See documentation for Nd
        """
        return self.Nd

    @R_0.setter
    def R_0(self, value):
        self.R0 = value

    @Expon_numerator.setter
    def Expon_numerator(self, value):
        self.Nn = value

    @Expon_denominator.setter
    def Expon_denominator(self, value):
        self.Nd = value
