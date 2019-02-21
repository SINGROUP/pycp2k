from pycp2k.inputsection import InputSection


class _krylov1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nkrylov = None
        self.Nblock = None
        self.Eps_krylov = None
        self.Eps_std_diag = None
        self.Check_mos_conv = None
        self._name = "KRYLOV"
        self._keywords = {'Nblock': 'NBLOCK', 'Eps_krylov': 'EPS_KRYLOV', 'Nkrylov': 'NKRYLOV', 'Check_mos_conv': 'CHECK_MOS_CONV', 'Eps_std_diag': 'EPS_STD_DIAG'}

