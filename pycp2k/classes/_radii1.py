from pycp2k.inputsection import InputSection
from ._each347 import _each347


class _radii1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Unit = None
        self.Core_charges_radii = None
        self.Pgf_radii = None
        self.Set_radii = None
        self.Kind_radii = None
        self.Core_charge_radii = None
        self.Ppl_radii = None
        self.Ppnl_radii = None
        self.Gapw_prj_radii = None
        self.EACH = _each347()
        self._name = "RADII"
        self._keywords = {'Pgf_radii': 'PGF_RADII', 'Core_charge_radii': 'CORE_CHARGE_RADII', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Gapw_prj_radii': 'GAPW_PRJ_RADII', 'Ppnl_radii': 'PPNL_RADII', 'Kind_radii': 'KIND_RADII', 'Set_radii': 'SET_RADII', 'Core_charges_radii': 'CORE_CHARGES_RADII', 'Filename': 'FILENAME', 'Ppl_radii': 'PPL_RADII', 'Unit': 'UNIT'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

