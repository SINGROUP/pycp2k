from pycp2k.inputsection import InputSection
from ._program_run_info12 import _program_run_info12
from ._dipole1 import _dipole1


class _print18(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info12()
        self.DIPOLE = _dipole1()
        self._name = "PRINT"
        self._subsections = {'DIPOLE': 'DIPOLE', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

