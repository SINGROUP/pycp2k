from pycp2k.inputsection import InputSection
from ._each169 import _each169


class _iteration_info2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Time_cumul = None
        self.EACH = _each169()
        self._name = "ITERATION_INFO"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Time_cumul': 'TIME_CUMUL'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

