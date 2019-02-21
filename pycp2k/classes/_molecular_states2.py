from pycp2k.inputsection import InputSection
from ._each210 import _each210
from ._cubes3 import _cubes3


class _molecular_states2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Cube_eval_range = None
        self.Mark_states = []
        self.EACH = _each210()
        self.CUBES = _cubes3()
        self._name = "MOLECULAR_STATES"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Cube_eval_range': 'CUBE_EVAL_RANGE'}
        self._repeated_keywords = {'Mark_states': 'MARK_STATES'}
        self._subsections = {'CUBES': 'CUBES', 'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

