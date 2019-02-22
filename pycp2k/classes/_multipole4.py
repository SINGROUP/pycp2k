from pycp2k.inputsection import InputSection
from ._interpolator7 import _interpolator7
from ._check_spline4 import _check_spline4
from ._program_run_info31 import _program_run_info31


class _multipole4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Rcut = None
        self.Ewald_precision = None
        self.Analytical_gterm = None
        self.Ngrids = None
        self.INTERPOLATOR = _interpolator7()
        self.CHECK_SPLINE = _check_spline4()
        self.PROGRAM_RUN_INFO = _program_run_info31()
        self._name = "MULTIPOLE"
        self._keywords = {'Analytical_gterm': 'ANALYTICAL_GTERM', 'Ngrids': 'NGRIDS', 'Ewald_precision': 'EWALD_PRECISION', 'Rcut': 'RCUT'}
        self._subsections = {'CHECK_SPLINE': 'CHECK_SPLINE', 'INTERPOLATOR': 'INTERPOLATOR', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

