from pycp2k.inputsection import InputSection
from ._diis_info1 import _diis_info1


class _diis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_sd_steps = None
        self.Max_steps = None
        self.N_diis = None
        self.Stepsize = None
        self.Max_stepsize = None
        self.Np_ls = None
        self.No_ls = None
        self.Check_diis = None
        self.DIIS_INFO = _diis_info1()
        self._name = "DIIS"
        self._keywords = {'Np_ls': 'NP_LS', 'Stepsize': 'STEPSIZE', 'Check_diis': 'CHECK_DIIS', 'Max_stepsize': 'MAX_STEPSIZE', 'No_ls': 'NO_LS', 'Max_steps': 'MAX_STEPS', 'N_diis': 'N_DIIS', 'Max_sd_steps': 'MAX_SD_STEPS'}
        self._subsections = {'DIIS_INFO': 'DIIS_INFO'}
        self._aliases = {'Ndiis': 'N_diis'}


    @property
    def Ndiis(self):
        """
        See documentation for N_diis
        """
        return self.N_diis

    @Ndiis.setter
    def Ndiis(self, value):
        self.N_diis = value
