from pycp2k.inputsection import InputSection
from ._interpolator2 import _interpolator2
from ._check_spline1 import _check_spline1
from ._program_run_info17 import _program_run_info17


class _multipole1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Rcut = None
        self.Ewald_precision = None
        self.Analytical_gterm = None
        self.Ngrids = None
        self.INTERPOLATOR = _interpolator2()
        self.CHECK_SPLINE = _check_spline1()
        self.PROGRAM_RUN_INFO = _program_run_info17()
        self._name = "MULTIPOLE"
        self._keywords = {'Analytical_gterm': 'ANALYTICAL_GTERM', 'Ngrids': 'NGRIDS', 'Ewald_precision': 'EWALD_PRECISION', 'Rcut': 'RCUT'}
        self._subsections = {'CHECK_SPLINE': 'CHECK_SPLINE', 'INTERPOLATOR': 'INTERPOLATOR', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

