from pycp2k.inputsection import InputSection
from ._each392 import _each392


class _fit_charge1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Type_of_density = None
        self.EACH = _each392()
        self._name = "FIT_CHARGE"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Type_of_density': 'TYPE_OF_DENSITY'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

