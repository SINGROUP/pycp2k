from pycp2k.inputsection import InputSection
from ._each264 import _each264


class _energy_windows1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.N_windows = None
        self.Restrict_range = None
        self.Range = None
        self.Print_cubes = None
        self.Stride = None
        self.EACH = _each264()
        self._name = "ENERGY_WINDOWS"
        self._keywords = {'Stride': 'STRIDE', 'Restrict_range': 'RESTRICT_RANGE', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Print_cubes': 'PRINT_CUBES', 'Filename': 'FILENAME', 'Range': 'RANGE', 'N_windows': 'N_WINDOWS'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

