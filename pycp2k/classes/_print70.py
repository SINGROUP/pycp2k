from pycp2k.inputsection import InputSection
from ._each443 import _each443


class _print70(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Load_balance_info = None
        self.EACH = _each443()
        self._name = "PRINT"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Load_balance_info': 'LOAD_BALANCE_INFO'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

