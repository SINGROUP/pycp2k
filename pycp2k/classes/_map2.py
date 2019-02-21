from pycp2k.inputsection import InputSection
from ._each336 import _each336


class _map2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Range = []
        self.Grid_spacing = []
        self.EACH = _each336()
        self._name = "MAP"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS'}
        self._repeated_keywords = {'Grid_spacing': 'GRID_SPACING', 'Range': 'RANGE'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

