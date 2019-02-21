from pycp2k.inputsection import InputSection
from ._variable1 import _variable1
from ._force_matching1 import _force_matching1
from ._history1 import _history1
from ._restart15 import _restart15


class _optimize_input1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.Accuracy = None
        self.Step_size = None
        self.Max_fun = None
        self.Iter_start_val = None
        self.Randomize_variables = None
        self.VARIABLE_list = []
        self.FORCE_MATCHING_list = []
        self.HISTORY = _history1()
        self.RESTART = _restart15()
        self._name = "OPTIMIZE_INPUT"
        self._keywords = {'Method': 'METHOD', 'Accuracy': 'ACCURACY', 'Max_fun': 'MAX_FUN', 'Randomize_variables': 'RANDOMIZE_VARIABLES', 'Step_size': 'STEP_SIZE', 'Iter_start_val': 'ITER_START_VAL'}
        self._subsections = {'HISTORY': 'HISTORY', 'RESTART': 'RESTART'}
        self._repeated_subsections = {'VARIABLE': '_variable1', 'FORCE_MATCHING': '_force_matching1'}
        self._attributes = ['VARIABLE_list', 'FORCE_MATCHING_list']

    def VARIABLE_add(self, section_parameters=None):
        new_section = _variable1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.VARIABLE_list.append(new_section)
        return new_section

    def FORCE_MATCHING_add(self, section_parameters=None):
        new_section = _force_matching1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FORCE_MATCHING_list.append(new_section)
        return new_section

