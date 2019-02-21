from pycp2k.inputsection import InputSection
from ._each136 import _each136


class _neighbor_lists3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Unit = None
        self.EACH = _each136()
        self._name = "NEIGHBOR_LISTS"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Unit': 'UNIT'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

