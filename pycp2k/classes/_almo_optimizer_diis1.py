from pycp2k.inputsection import InputSection


class _almo_optimizer_diis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_iter = None
        self.Eps_error = None
        self.N_diis = None
        self._name = "ALMO_OPTIMIZER_DIIS"
        self._keywords = {'N_diis': 'N_DIIS', 'Eps_error': 'EPS_ERROR', 'Max_iter': 'MAX_ITER'}

