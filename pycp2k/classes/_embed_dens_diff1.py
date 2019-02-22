from pycp2k.inputsection import InputSection
from ._each142 import _each142


class _embed_dens_diff1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.EACH = _each142()
        self._name = "EMBED_DENS_DIFF"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Stride': 'STRIDE'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

