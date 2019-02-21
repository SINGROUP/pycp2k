from pycp2k.inputsection import InputSection
from ._print_dftd5 import _print_dftd5


class _pair_potential5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.R_cutoff = None
        self.Type = None
        self.Parameter_file_name = None
        self.Reference_functional = None
        self.Scaling = None
        self.Exp_pre = None
        self.Eps_cn = None
        self.D3_scaling = None
        self.D3bj_scaling = None
        self.Calculate_c9_term = None
        self.Reference_c9_term = None
        self.Long_range_correction = None
        self.Short_range_correction = None
        self.Verbose_output = None
        self.D3_exclude_kind = None
        self.Kind_coordination_numbers = []
        self.Atom_coordination_numbers = []
        self.Atomparm = []
        self.PRINT_DFTD = _print_dftd5()
        self._name = "PAIR_POTENTIAL"
        self._keywords = {'Reference_functional': 'REFERENCE_FUNCTIONAL', 'Exp_pre': 'EXP_PRE', 'Short_range_correction': 'SHORT_RANGE_CORRECTION', 'Scaling': 'SCALING', 'Eps_cn': 'EPS_CN', 'Long_range_correction': 'LONG_RANGE_CORRECTION', 'D3bj_scaling': 'D3BJ_SCALING', 'R_cutoff': 'R_CUTOFF', 'Parameter_file_name': 'PARAMETER_FILE_NAME', 'D3_exclude_kind': 'D3_EXCLUDE_KIND', 'Calculate_c9_term': 'CALCULATE_C9_TERM', 'Reference_c9_term': 'REFERENCE_C9_TERM', 'D3_scaling': 'D3_SCALING', 'Type': 'TYPE', 'Verbose_output': 'VERBOSE_OUTPUT'}
        self._repeated_keywords = {'Atomparm': 'ATOMPARM', 'Atom_coordination_numbers': 'ATOM_COORDINATION_NUMBERS', 'Kind_coordination_numbers': 'KIND_COORDINATION_NUMBERS'}
        self._subsections = {'PRINT_DFTD': 'PRINT_DFTD'}

