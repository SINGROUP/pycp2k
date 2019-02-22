from pycp2k.inputsection import InputSection
from ._each255 import _each255


class _wannier901(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Seed_name = None
        self.Mp_grid = None
        self.Added_mos = None
        self.Exclude_bands = []
        self.Wannier_functions = []
        self.EACH = _each255()
        self._name = "WANNIER90"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Mp_grid': 'MP_GRID', 'Filename': 'FILENAME', 'Added_mos': 'ADDED_MOS', 'Seed_name': 'SEED_NAME'}
        self._repeated_keywords = {'Wannier_functions': 'WANNIER_FUNCTIONS', 'Exclude_bands': 'EXCLUDE_BANDS'}
        self._subsections = {'EACH': 'EACH'}
        self._aliases = {'Added_bands': 'Added_mos'}
        self._attributes = ['Section_parameters']


    @property
    def Added_bands(self):
        """
        See documentation for Added_mos
        """
        return self.Added_mos

    @Added_bands.setter
    def Added_bands(self, value):
        self.Added_mos = value
