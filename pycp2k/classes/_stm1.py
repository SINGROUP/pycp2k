from pycp2k.inputsection import InputSection
from ._each226 import _each226


class _stm1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Nlumo = None
        self.Bias = None
        self.Th_torb = []
        self.Ref_energy = None
        self.Append = None
        self.EACH = _each226()
        self._name = "STM"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Bias': 'BIAS', 'Append': 'APPEND', 'Filename': 'FILENAME', 'Nlumo': 'NLUMO', 'Stride': 'STRIDE', 'Ref_energy': 'REF_ENERGY'}
        self._repeated_keywords = {'Th_torb': 'TH_TORB'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

