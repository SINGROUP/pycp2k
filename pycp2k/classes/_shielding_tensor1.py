from pycp2k.inputsection import InputSection
from ._each364 import _each364


class _shielding_tensor1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Atoms_lu_bounds = None
        self.Atoms_list = []
        self.EACH = _each364()
        self._name = "SHIELDING_TENSOR"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Atoms_lu_bounds': 'ATOMS_LU_BOUNDS', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS'}
        self._repeated_keywords = {'Atoms_list': 'ATOMS_LIST'}
        self._subsections = {'EACH': 'EACH'}
        self._aliases = {'Atoms_lu': 'Atoms_lu_bounds'}
        self._attributes = ['Section_parameters']


    @property
    def Atoms_lu(self):
        """
        See documentation for Atoms_lu_bounds
        """
        return self.Atoms_lu_bounds

    @Atoms_lu.setter
    def Atoms_lu(self, value):
        self.Atoms_lu_bounds = value
