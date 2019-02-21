from pycp2k.inputsection import InputSection
from ._each344 import _each344


class _kinds1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Potential = None
        self.Basis_set = None
        self.Se_parameters = None
        self.EACH = _each344()
        self._name = "KINDS"
        self._keywords = {'Basis_set': 'BASIS_SET', 'Potential': 'POTENTIAL', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Se_parameters': 'SE_PARAMETERS', 'Filename': 'FILENAME'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

