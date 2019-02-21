from pycp2k.inputsection import InputSection
from ._each430 import _each430


class _geometrical_response_basis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Delta_charge = None
        self.Derivatives = None
        self.Quadrature = None
        self.Grid_points = None
        self.Num_gto_core = None
        self.Num_gto_extended = None
        self.Num_gto_polarization = None
        self.Extension_basis = None
        self.Geometrical_factor = None
        self.Geo_start_value = None
        self.Confinement = None
        self.Name_body = None
        self.EACH = _each430()
        self._name = "GEOMETRICAL_RESPONSE_BASIS"
        self._keywords = {'Num_gto_core': 'NUM_GTO_CORE', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Confinement': 'CONFINEMENT', 'Num_gto_polarization': 'NUM_GTO_POLARIZATION', 'Extension_basis': 'EXTENSION_BASIS', 'Geo_start_value': 'GEO_START_VALUE', 'Delta_charge': 'DELTA_CHARGE', 'Quadrature': 'QUADRATURE', 'Filename': 'FILENAME', 'Name_body': 'NAME_BODY', 'Num_gto_extended': 'NUM_GTO_EXTENDED', 'Geometrical_factor': 'GEOMETRICAL_FACTOR', 'Grid_points': 'GRID_POINTS', 'Derivatives': 'DERIVATIVES'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

