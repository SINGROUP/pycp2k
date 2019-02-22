from pycp2k.inputsection import InputSection
from ._each428 import _each428


class _fit_kgpot1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Num_gaussian = None
        self.Num_polynom = None
        self.EACH = _each428()
        self._name = "FIT_KGPOT"
        self._keywords = {'Num_polynom': 'NUM_POLYNOM', 'Log_print_key': 'LOG_PRINT_KEY', 'Num_gaussian': 'NUM_GAUSSIAN', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Add_last': 'ADD_LAST', 'Filename': 'FILENAME'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

