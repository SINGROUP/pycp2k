from pycp2k.inputsection import InputSection
from ._each271 import _each271


class _hyperfine_coupling_tensor1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Interaction_radius = None
        self.EACH = _each271()
        self._name = "HYPERFINE_COUPLING_TENSOR"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Interaction_radius': 'INTERACTION_RADIUS'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

