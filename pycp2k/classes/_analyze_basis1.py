from pycp2k.inputsection import InputSection
from ._each433 import _each433


class _analyze_basis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Overlap_condition_number = None
        self.Completeness = None
        self.EACH = _each433()
        self._name = "ANALYZE_BASIS"
        self._keywords = {'Overlap_condition_number': 'OVERLAP_CONDITION_NUMBER', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Filename': 'FILENAME', 'Completeness': 'COMPLETENESS'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

