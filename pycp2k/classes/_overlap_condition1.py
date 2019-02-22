from pycp2k.inputsection import InputSection
from ._each243 import _each243


class _overlap_condition1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Num1_norm = None
        self.Diagonalization = None
        self.Arnoldi = None
        self.EACH = _each243()
        self._name = "OVERLAP_CONDITION"
        self._keywords = {'Num1_norm': '1-NORM', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Diagonalization': 'DIAGONALIZATION', 'Arnoldi': 'ARNOLDI', 'Filename': 'FILENAME'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

