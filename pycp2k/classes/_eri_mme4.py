from pycp2k.inputsection import InputSection
from ._eri_mme_info4 import _eri_mme_info4
from ._cutoff_calib4 import _cutoff_calib4


class _eri_mme4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.N_minimax = None
        self.Cutoff = None
        self.Sum_precision = None
        self.Do_calibrate_cutoff = None
        self.Print_calib = None
        self.Debug = None
        self.Debug_tolerance = None
        self.Debug_nsum_max = None
        self.ERI_MME_INFO = _eri_mme_info4()
        self.CUTOFF_CALIB = _cutoff_calib4()
        self._name = "ERI_MME"
        self._keywords = {'N_minimax': 'N_MINIMAX', 'Debug_nsum_max': 'DEBUG_NSUM_MAX', 'Debug_tolerance': 'DEBUG_TOLERANCE', 'Cutoff': 'CUTOFF', 'Sum_precision': 'SUM_PRECISION', 'Do_calibrate_cutoff': 'DO_CALIBRATE_CUTOFF', 'Debug': 'DEBUG', 'Print_calib': 'PRINT_CALIB'}
        self._subsections = {'CUTOFF_CALIB': 'CUTOFF_CALIB', 'ERI_MME_INFO': 'ERI_MME_INFO'}

