from pycp2k.inputsection import InputSection
from ._print53 import _print53


class _localize4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Max_iter = None
        self.Max_crazy_angle = None
        self.Crazy_scale = None
        self.Crazy_use_diag = None
        self.Use_history = None
        self.Eps_occupation = None
        self.Out_iter_each = None
        self.Eps_localization = None
        self.Min_or_max = None
        self.Method = None
        self.Jacobi_fallback = None
        self.Restart = None
        self.Lochomo_restart_file_name = None
        self.Loclumo_restart_file_name = None
        self.Operator = None
        self.List = []
        self.List_unoccupied = []
        self.States = None
        self.Energy_range = None
        self.PRINT = _print53()
        self._name = "LOCALIZE"
        self._keywords = {'Method': 'METHOD', 'States': 'STATES', 'Loclumo_restart_file_name': 'LOCLUMO_RESTART_FILE_NAME', 'Energy_range': 'ENERGY_RANGE', 'Use_history': 'USE_HISTORY', 'Lochomo_restart_file_name': 'LOCHOMO_RESTART_FILE_NAME', 'Max_iter': 'MAX_ITER', 'Eps_localization': 'EPS_LOCALIZATION', 'Crazy_scale': 'CRAZY_SCALE', 'Max_crazy_angle': 'MAX_CRAZY_ANGLE', 'Crazy_use_diag': 'CRAZY_USE_DIAG', 'Operator': 'OPERATOR', 'Restart': 'RESTART', 'Out_iter_each': 'OUT_ITER_EACH', 'Eps_occupation': 'EPS_OCCUPATION', 'Jacobi_fallback': 'JACOBI_FALLBACK', 'Min_or_max': 'MIN_OR_MAX'}
        self._repeated_keywords = {'List_unoccupied': 'LIST_UNOCCUPIED', 'List': 'LIST'}
        self._subsections = {'PRINT': 'PRINT'}
        self._attributes = ['Section_parameters']

