from pycp2k.inputsection import InputSection
from ._each260 import _each260


class _mao_analysis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Eps_filter = None
        self.Reference_basis = None
        self.Print_basis = None
        self.Eps_grad = None
        self.Eps_function = None
        self.Max_iter = None
        self.Neglect_abc = None
        self.Ab_threshold = None
        self.Abc_threshold = None
        self.Analyze_unassigned_charge = None
        self.EACH = _each260()
        self._name = "MAO_ANALYSIS"
        self._keywords = {'Print_basis': 'PRINT_BASIS', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Ab_threshold': 'AB_THRESHOLD', 'Analyze_unassigned_charge': 'ANALYZE_UNASSIGNED_CHARGE', 'Eps_filter': 'EPS_FILTER', 'Eps_function': 'EPS_FUNCTION', 'Neglect_abc': 'NEGLECT_ABC', 'Reference_basis': 'REFERENCE_BASIS', 'Eps_grad': 'EPS_GRAD', 'Filename': 'FILENAME', 'Abc_threshold': 'ABC_THRESHOLD', 'Max_iter': 'MAX_ITER'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

