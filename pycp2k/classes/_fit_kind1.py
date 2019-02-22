from pycp2k.inputsection import InputSection
from ._constrain_exponents2 import _constrain_exponents2
from ._derived_basis_sets1 import _derived_basis_sets1


class _fit_kind1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Basis_set = None
        self.Initial_degrees_of_freedom = None
        self.Switch_coeff_state = []
        self.Switch_contraction_state = []
        self.Switch_exp_state = []
        self.Switch_set_state = []
        self.CONSTRAIN_EXPONENTS_list = []
        self.DERIVED_BASIS_SETS_list = []
        self._name = "FIT_KIND"
        self._keywords = {'Basis_set': 'BASIS_SET', 'Initial_degrees_of_freedom': 'INITIAL_DEGREES_OF_FREEDOM'}
        self._repeated_keywords = {'Switch_contraction_state': 'SWITCH_CONTRACTION_STATE', 'Switch_exp_state': 'SWITCH_EXP_STATE', 'Switch_coeff_state': 'SWITCH_COEFF_STATE', 'Switch_set_state': 'SWITCH_SET_STATE'}
        self._repeated_subsections = {'DERIVED_BASIS_SETS': '_derived_basis_sets1', 'CONSTRAIN_EXPONENTS': '_constrain_exponents2'}
        self._attributes = ['Section_parameters', 'CONSTRAIN_EXPONENTS_list', 'DERIVED_BASIS_SETS_list']

    def DERIVED_BASIS_SETS_add(self, section_parameters=None):
        new_section = _derived_basis_sets1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DERIVED_BASIS_SETS_list.append(new_section)
        return new_section

    def CONSTRAIN_EXPONENTS_add(self, section_parameters=None):
        new_section = _constrain_exponents2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.CONSTRAIN_EXPONENTS_list.append(new_section)
        return new_section

