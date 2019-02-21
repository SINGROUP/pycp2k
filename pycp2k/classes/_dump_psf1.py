from pycp2k.inputsection import InputSection
from ._each330 import _each330


class _dump_psf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.EACH = _each330()
        self._name = "DUMP_PSF"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

