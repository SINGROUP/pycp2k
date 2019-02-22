from pycp2k.inputsection import InputSection
from ._each429 import _each429


class _response_basis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Delta_charge = None
        self.Derivatives = None
        self.EACH = _each429()
        self._name = "RESPONSE_BASIS"
        self._keywords = {'Delta_charge': 'DELTA_CHARGE', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Derivatives': 'DERIVATIVES'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

