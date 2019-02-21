from pycp2k.inputsection import InputSection
from ._point4 import _point4


class _coordination1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms_from = []
        self.Points_from = self.Atoms_from
        self.Atoms_to = []
        self.Points_to = self.Atoms_to
        self.Atoms_to_b = []
        self.Points_to_b = self.Atoms_to_b
        self.Kinds_from = []
        self.Kinds_to = []
        self.Kinds_to_b = []
        self.R0 = None
        self.Nn = None
        self.Nd = None
        self.R0_b = None
        self.Nn_b = None
        self.Nd_b = None
        self.POINT_list = []
        self._name = "COORDINATION"
        self._keywords = {'Nn_b': 'NN_B', 'Nd_b': 'ND_B', 'Nd': 'ND', 'R0_b': 'R0_B', 'Nn': 'NN', 'R0': 'R0'}
        self._repeated_keywords = {'Kinds_to': 'KINDS_TO', 'Kinds_to_b': 'KINDS_TO_B', 'Atoms_from': 'ATOMS_FROM', 'Atoms_to': 'ATOMS_TO', 'Kinds_from': 'KINDS_FROM', 'Atoms_to_b': 'ATOMS_TO_B'}
        self._repeated_subsections = {'POINT': '_point4'}
        self._aliases = {'Expon_denominator_b': 'Nd_b', 'R_0_b': 'R0_b', 'Expon_denominator': 'Nd', 'Expon_numerator_b': 'Nn_b', 'R_0': 'R0', 'Expon_numerator': 'Nn'}
        self._repeated_aliases = {'Points_from': 'Atoms_from', 'Points_to': 'Atoms_to', 'Points_to_b': 'Atoms_to_b'}
        self._attributes = ['POINT_list']

    def POINT_add(self, section_parameters=None):
        new_section = _point4()
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

    @property
    def R_0_b(self):
        """
        See documentation for R0_b
        """
        return self.R0_b

    @property
    def Expon_numerator_b(self):
        """
        See documentation for Nn_b
        """
        return self.Nn_b

    @property
    def Expon_denominator_b(self):
        """
        See documentation for Nd_b
        """
        return self.Nd_b

    @R_0.setter
    def R_0(self, value):
        self.R0 = value

    @Expon_numerator.setter
    def Expon_numerator(self, value):
        self.Nn = value

    @Expon_denominator.setter
    def Expon_denominator(self, value):
        self.Nd = value

    @R_0_b.setter
    def R_0_b(self, value):
        self.R0_b = value

    @Expon_numerator_b.setter
    def Expon_numerator_b(self, value):
        self.Nn_b = value

    @Expon_denominator_b.setter
    def Expon_denominator_b(self, value):
        self.Nd_b = value
