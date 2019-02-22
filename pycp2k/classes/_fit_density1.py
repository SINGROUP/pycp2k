from pycp2k.inputsection import InputSection
from ._each427 import _each427


class _fit_density1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Num_gto = None
        self.EACH = _each427()
        self._name = "FIT_DENSITY"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Num_gto': 'NUM_GTO'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

