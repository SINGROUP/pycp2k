from pycp2k.inputsection import InputSection
from ._each266 import _each266


class _s_csr_write1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Threshold = None
        self.Upper_triangular = None
        self.EACH = _each266()
        self._name = "S_CSR_WRITE"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Upper_triangular': 'UPPER_TRIANGULAR', 'Threshold': 'THRESHOLD', 'Filename': 'FILENAME'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

