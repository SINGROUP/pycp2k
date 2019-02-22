from pycp2k.inputsection import InputSection
from ._each345 import _each345


class _symmetry1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Molecule = None
        self.Eps_geo = None
        self.Standard_orientation = None
        self.Inertia = None
        self.Symmetry_elements = None
        self.All = None
        self.Rotation_matrices = None
        self.Check_symmetry = None
        self.EACH = _each345()
        self._name = "SYMMETRY"
        self._keywords = {'Check_symmetry': 'CHECK_SYMMETRY', 'Inertia': 'INERTIA', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Eps_geo': 'EPS_GEO', 'Molecule': 'MOLECULE', 'Standard_orientation': 'STANDARD_ORIENTATION', 'All': 'ALL', 'Filename': 'FILENAME', 'Rotation_matrices': 'ROTATION_MATRICES', 'Symmetry_elements': 'SYMMETRY_ELEMENTS'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

