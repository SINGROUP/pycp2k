from pycp2k.inputsection import InputSection
from ._mixing3 import _mixing3


class _diag_sub_scf3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Max_iter = None
        self.Eps_ene = None
        self.Eps_adapt_scf = None
        self.Eps_skip_sub_diag = None
        self.MIXING = _mixing3()
        self._name = "DIAG_SUB_SCF"
        self._keywords = {'Eps_ene': 'EPS_ENE', 'Eps_adapt_scf': 'EPS_ADAPT_SCF', 'Eps_skip_sub_diag': 'EPS_SKIP_SUB_DIAG', 'Max_iter': 'MAX_ITER'}
        self._subsections = {'MIXING': 'MIXING'}
        self._attributes = ['Section_parameters']

