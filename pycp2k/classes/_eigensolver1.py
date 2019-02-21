from pycp2k.inputsection import InputSection


class _eigensolver1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.N = None
        self.N_loop = None
        self.Diag_method = None
        self.Eigenvalues = None
        self.Init_method = None
        self._name = "EIGENSOLVER"
        self._keywords = {'Eigenvalues': 'EIGENVALUES', 'Init_method': 'INIT_METHOD', 'N': 'N', 'N_loop': 'N_LOOP', 'Diag_method': 'DIAG_METHOD'}

