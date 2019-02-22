from pycp2k.inputsection import InputSection


class _curvy_steps1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Line_search = None
        self.N_bch_history = None
        self.Min_hessian_shift = None
        self.Filter_factor = None
        self.Filter_factor_scale = None
        self.Min_filter = None
        self._name = "CURVY_STEPS"
        self._keywords = {'Line_search': 'LINE_SEARCH', 'Filter_factor_scale': 'FILTER_FACTOR_SCALE', 'N_bch_history': 'N_BCH_HISTORY', 'Min_hessian_shift': 'MIN_HESSIAN_SHIFT', 'Min_filter': 'MIN_FILTER', 'Filter_factor': 'FILTER_FACTOR'}

