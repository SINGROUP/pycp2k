from pycp2k.inputsection import InputSection
from ._each251 import _each251


class _v_xc_cube1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Append = None
        self.EACH = _each251()
        self._name = "V_XC_CUBE"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Append': 'APPEND', 'Filename': 'FILENAME', 'Stride': 'STRIDE'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

