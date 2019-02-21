from pycp2k.inputsection import InputSection
from ._each115 import _each115


class _dos1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.N_gridpoints = None
        self.EACH = _each115()
        self._name = "DOS"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'N_gridpoints': 'N_GRIDPOINTS'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

