from pycp2k.inputsection import InputSection
from ._each244 import _each244


class _e_density_cube1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Stride = None
        self.Total_density = None
        self.Append = None
        self.Xrd_interface = None
        self.Ngauss = None
        self.EACH = _each244()
        self._name = "E_DENSITY_CUBE"
        self._keywords = {'Total_density': 'TOTAL_DENSITY', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Ngauss': 'NGAUSS', 'Append': 'APPEND', 'Filename': 'FILENAME', 'Xrd_interface': 'XRD_INTERFACE', 'Stride': 'STRIDE'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

