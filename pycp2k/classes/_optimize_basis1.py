from pycp2k.inputsection import InputSection
from ._fit_kind1 import _fit_kind1
from ._training_files1 import _training_files1
from ._optimization1 import _optimization1


class _optimize_basis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Basis_template_file = None
        self.Basis_work_file = None
        self.Basis_output_file = None
        self.Write_frequency = None
        self.Use_condition_number = None
        self.Basis_combinations = []
        self.Residuum_weight = []
        self.Condition_weight = []
        self.Group_partition = []
        self.FIT_KIND_list = []
        self.TRAINING_FILES_list = []
        self.OPTIMIZATION = _optimization1()
        self._name = "OPTIMIZE_BASIS"
        self._keywords = {'Use_condition_number': 'USE_CONDITION_NUMBER', 'Basis_template_file': 'BASIS_TEMPLATE_FILE', 'Write_frequency': 'WRITE_FREQUENCY', 'Basis_work_file': 'BASIS_WORK_FILE', 'Basis_output_file': 'BASIS_OUTPUT_FILE'}
        self._repeated_keywords = {'Basis_combinations': 'BASIS_COMBINATIONS', 'Condition_weight': 'CONDITION_WEIGHT', 'Group_partition': 'GROUP_PARTITION', 'Residuum_weight': 'RESIDUUM_WEIGHT'}
        self._subsections = {'OPTIMIZATION': 'OPTIMIZATION'}
        self._repeated_subsections = {'FIT_KIND': '_fit_kind1', 'TRAINING_FILES': '_training_files1'}
        self._attributes = ['FIT_KIND_list', 'TRAINING_FILES_list']

    def FIT_KIND_add(self, section_parameters=None):
        new_section = _fit_kind1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FIT_KIND_list.append(new_section)
        return new_section

    def TRAINING_FILES_add(self, section_parameters=None):
        new_section = _training_files1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.TRAINING_FILES_list.append(new_section)
        return new_section

