from pycp2k.inputsection import InputSection
from ._each268 import _each268
from ._interpolator3 import _interpolator3


class _electric_field_gradient1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Interpolation = None
        self.Gspace_smoothing = None
        self.Debug = None
        self.EACH = _each268()
        self.INTERPOLATOR = _interpolator3()
        self._name = "ELECTRIC_FIELD_GRADIENT"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Interpolation': 'INTERPOLATION', 'Filename': 'FILENAME', 'Gspace_smoothing': 'GSPACE_SMOOTHING', 'Debug': 'DEBUG'}
        self._subsections = {'INTERPOLATOR': 'INTERPOLATOR', 'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

