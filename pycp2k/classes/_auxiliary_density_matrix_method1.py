from pycp2k.inputsection import InputSection


class _auxiliary_density_matrix_method1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Admm_purification_method = None
        self.Method = None
        self.Exch_scaling_model = None
        self.Exch_correction_func = None
        self.Optx_a1 = None
        self.Optx_a2 = None
        self.Optx_gamma = None
        self.Block_list = []
        self.Eps_filter = None
        self._name = "AUXILIARY_DENSITY_MATRIX_METHOD"
        self._keywords = {'Admm_purification_method': 'ADMM_PURIFICATION_METHOD', 'Method': 'METHOD', 'Exch_correction_func': 'EXCH_CORRECTION_FUNC', 'Eps_filter': 'EPS_FILTER', 'Optx_a2': 'OPTX_A2', 'Optx_a1': 'OPTX_A1', 'Optx_gamma': 'OPTX_GAMMA', 'Exch_scaling_model': 'EXCH_SCALING_MODEL'}
        self._repeated_keywords = {'Block_list': 'BLOCK_LIST'}

