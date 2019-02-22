from pycp2k.inputsection import InputSection


class _gold3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Initial_step = None
        self.Brack_limit = None
        self.Brent_tol = None
        self.Brent_max_iter = None
        self._name = "GOLD"
        self._keywords = {'Brack_limit': 'BRACK_LIMIT', 'Initial_step': 'INITIAL_STEP', 'Brent_tol': 'BRENT_TOL', 'Brent_max_iter': 'BRENT_MAX_ITER'}

