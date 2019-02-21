from pycp2k.inputsection import InputSection
from ._each261 import _each261
from ._minbas_cube1 import _minbas_cube1
from ._mos_molden3 import _mos_molden3


class _minbas_analysis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Eps_filter = None
        self.Full_orthogonalization = None
        self.Bond_order = None
        self.EACH = _each261()
        self.MINBAS_CUBE = _minbas_cube1()
        self.MOS_MOLDEN = _mos_molden3()
        self._name = "MINBAS_ANALYSIS"
        self._keywords = {'Bond_order': 'BOND_ORDER', 'Eps_filter': 'EPS_FILTER', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Full_orthogonalization': 'FULL_ORTHOGONALIZATION', 'Filename': 'FILENAME'}
        self._subsections = {'MINBAS_CUBE': 'MINBAS_CUBE', 'MOS_MOLDEN': 'MOS_MOLDEN', 'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

