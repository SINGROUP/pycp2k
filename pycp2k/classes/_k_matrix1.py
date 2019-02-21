from pycp2k.inputsection import InputSection
from ._each366 import _each366


class _k_matrix1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Atoms_list = []
        self.EACH = _each366()
        self._name = "K_MATRIX"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS'}
        self._repeated_keywords = {'Atoms_list': 'ATOMS_LIST'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

