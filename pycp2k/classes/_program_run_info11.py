from pycp2k.inputsection import InputSection
from ._each98 import _each98


class _program_run_info11(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Mo_overlap_matrix = None
        self.Mo_overlap_eigenvalues = None
        self.EACH = _each98()
        self._name = "PROGRAM_RUN_INFO"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Mo_overlap_eigenvalues': 'MO_OVERLAP_EIGENVALUES', 'Mo_overlap_matrix': 'MO_OVERLAP_MATRIX'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

