from pycp2k.inputsection import InputSection
from ._pair_potential4 import _pair_potential4
from ._non_local4 import _non_local4


class _vdw_potential4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Potential_type = None
        self.PAIR_POTENTIAL_list = []
        self.NON_LOCAL_list = []
        self._name = "VDW_POTENTIAL"
        self._keywords = {'Potential_type': 'POTENTIAL_TYPE'}
        self._repeated_subsections = {'PAIR_POTENTIAL': '_pair_potential4', 'NON_LOCAL': '_non_local4'}
        self._aliases = {'Dispersion_functional': 'Potential_type'}
        self._attributes = ['PAIR_POTENTIAL_list', 'NON_LOCAL_list']

    def PAIR_POTENTIAL_add(self, section_parameters=None):
        new_section = _pair_potential4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PAIR_POTENTIAL_list.append(new_section)
        return new_section

    def NON_LOCAL_add(self, section_parameters=None):
        new_section = _non_local4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.NON_LOCAL_list.append(new_section)
        return new_section


    @property
    def Dispersion_functional(self):
        """
        See documentation for Potential_type
        """
        return self.Potential_type

    @Dispersion_functional.setter
    def Dispersion_functional(self, value):
        self.Potential_type = value
