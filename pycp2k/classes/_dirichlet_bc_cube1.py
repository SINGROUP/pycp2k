from pycp2k.inputsection import InputSection
from ._each249 import _each249


class _dirichlet_bc_cube1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Tile_cubes = None
        self.Stride = None
        self.Append = None
        self.EACH = _each249()
        self._name = "DIRICHLET_BC_CUBE"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Tile_cubes': 'TILE_CUBES', 'Append': 'APPEND', 'Filename': 'FILENAME', 'Stride': 'STRIDE'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

