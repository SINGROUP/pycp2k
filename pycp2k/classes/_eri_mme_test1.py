from pycp2k.inputsection import InputSection
from ._eri_mme1 import _eri_mme1


class _eri_mme_test1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Test_3c = None
        self.Test_2c = None
        self.Abc = None
        self.Min_npos = None
        self.Nrep = None
        self.Check_2c_accuracy = None
        self.Lmax = None
        self.Zet_min = None
        self.Zet_max = None
        self.Nzet = None
        self.Nsample_3c = None
        self.ERI_MME = _eri_mme1()
        self._name = "ERI_MME_TEST"
        self._keywords = {'Test_2c': 'TEST_2C', 'Abc': 'ABC', 'Lmax': 'LMAX', 'Nsample_3c': 'NSAMPLE_3C', 'Min_npos': 'MIN_NPOS', 'Test_3c': 'TEST_3C', 'Nzet': 'NZET', 'Zet_max': 'ZET_MAX', 'Nrep': 'NREP', 'Zet_min': 'ZET_MIN', 'Check_2c_accuracy': 'CHECK_2C_ACCURACY'}
        self._subsections = {'ERI_MME': 'ERI_MME'}
        self._attributes = ['Section_parameters']

