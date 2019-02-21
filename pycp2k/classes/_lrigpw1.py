from pycp2k.inputsection import InputSection


class _lrigpw1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Lri_overlap_matrix = None
        self.Max_condition_num = None
        self.Eps_o3_int = None
        self.Debug_lri_integrals = None
        self.Exact_1c_terms = None
        self.Distant_pair_approximation = None
        self.Distant_pair_method = None
        self.Distant_pair_radii = None
        self.Shg_lri_integrals = None
        self.Ri_sinv = None
        self._name = "LRIGPW"
        self._keywords = {'Shg_lri_integrals': 'SHG_LRI_INTEGRALS', 'Ri_sinv': 'RI_SINV', 'Distant_pair_approximation': 'DISTANT_PAIR_APPROXIMATION', 'Eps_o3_int': 'EPS_O3_INT', 'Debug_lri_integrals': 'DEBUG_LRI_INTEGRALS', 'Max_condition_num': 'MAX_CONDITION_NUM', 'Distant_pair_method': 'DISTANT_PAIR_METHOD', 'Lri_overlap_matrix': 'LRI_OVERLAP_MATRIX', 'Distant_pair_radii': 'DISTANT_PAIR_RADII', 'Exact_1c_terms': 'EXACT_1C_TERMS'}

