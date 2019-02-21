from pycp2k.inputsection import InputSection
from ._interpolator4 import _interpolator4
from ._check_spline2 import _check_spline2
from ._program_run_info27 import _program_run_info27


class _multipole2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Rcut = None
        self.Ewald_precision = None
        self.Analytical_gterm = None
        self.Ngrids = None
        self.INTERPOLATOR = _interpolator4()
        self.CHECK_SPLINE = _check_spline2()
        self.PROGRAM_RUN_INFO = _program_run_info27()
        self._name = "MULTIPOLE"
        self._keywords = {'Analytical_gterm': 'ANALYTICAL_GTERM', 'Ngrids': 'NGRIDS', 'Ewald_precision': 'EWALD_PRECISION', 'Rcut': 'RCUT'}
        self._subsections = {'CHECK_SPLINE': 'CHECK_SPLINE', 'INTERPOLATOR': 'INTERPOLATOR', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

