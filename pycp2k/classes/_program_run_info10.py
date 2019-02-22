from pycp2k.inputsection import InputSection
from ._each76 import _each76


class _program_run_info10(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Initial_configuration_info = None
        self.EACH = _each76()
        self._name = "PROGRAM_RUN_INFO"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Initial_configuration_info': 'INITIAL_CONFIGURATION_INFO'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

