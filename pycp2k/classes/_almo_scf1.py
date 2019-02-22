from pycp2k.inputsection import InputSection
from ._almo_optimizer_diis1 import _almo_optimizer_diis1
from ._almo_optimizer_pcg1 import _almo_optimizer_pcg1
from ._xalmo_optimizer_pcg1 import _xalmo_optimizer_pcg1
from ._analysis1 import _analysis1


class _almo_scf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_filter = None
        self.Almo_scf_guess = None
        self.Almo_extrapolation_order = None
        self.Xalmo_extrapolation_order = None
        self.Almo_algorithm = None
        self.Delocalize_method = None
        self.Xalmo_r_cutoff_factor = None
        self.ALMO_OPTIMIZER_DIIS = _almo_optimizer_diis1()
        self.ALMO_OPTIMIZER_PCG = _almo_optimizer_pcg1()
        self.XALMO_OPTIMIZER_PCG = _xalmo_optimizer_pcg1()
        self.ANALYSIS = _analysis1()
        self._name = "ALMO_SCF"
        self._keywords = {'Eps_filter': 'EPS_FILTER', 'Xalmo_extrapolation_order': 'XALMO_EXTRAPOLATION_ORDER', 'Xalmo_r_cutoff_factor': 'XALMO_R_CUTOFF_FACTOR', 'Almo_scf_guess': 'ALMO_SCF_GUESS', 'Almo_algorithm': 'ALMO_ALGORITHM', 'Delocalize_method': 'DELOCALIZE_METHOD', 'Almo_extrapolation_order': 'ALMO_EXTRAPOLATION_ORDER'}
        self._subsections = {'ALMO_OPTIMIZER_PCG': 'ALMO_OPTIMIZER_PCG', 'XALMO_OPTIMIZER_PCG': 'XALMO_OPTIMIZER_PCG', 'ALMO_OPTIMIZER_DIIS': 'ALMO_OPTIMIZER_DIIS', 'ANALYSIS': 'ANALYSIS'}

