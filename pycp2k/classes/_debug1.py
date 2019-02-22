from pycp2k.inputsection import InputSection
from ._program_run_info3 import _program_run_info3


class _debug1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Debug_forces = None
        self.Debug_stress_tensor = None
        self.Dx = None
        self.Eps_no_error_check = None
        self.Stop_on_mismatch = None
        self.PROGRAM_RUN_INFO = _program_run_info3()
        self._name = "DEBUG"
        self._keywords = {'Debug_stress_tensor': 'DEBUG_STRESS_TENSOR', 'Stop_on_mismatch': 'STOP_ON_MISMATCH', 'Debug_forces': 'DEBUG_FORCES', 'Dx': 'DX', 'Eps_no_error_check': 'EPS_NO_ERROR_CHECK'}
        self._subsections = {'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

