from pycp2k.inputsection import InputSection
from ._each166 import _each166


class _program_run_info20(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Condition_number = None
        self.EACH = _each166()
        self._name = "PROGRAM_RUN_INFO"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Condition_number': 'CONDITION_NUMBER'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

