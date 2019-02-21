from pycp2k.inputsection import InputSection
from ._each369 import _each369
from ._xc4 import _xc4


class _g_tensor1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Gapw_max_alpha = None
        self.Soo_rho_hard = None
        self.EACH = _each369()
        self.XC = _xc4()
        self._name = "G_TENSOR"
        self._keywords = {'Gapw_max_alpha': 'GAPW_MAX_ALPHA', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Log_print_key': 'LOG_PRINT_KEY', 'Soo_rho_hard': 'SOO_RHO_HARD'}
        self._subsections = {'XC': 'XC', 'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

