from pycp2k.inputsection import InputSection
from ._program_run_info34 import _program_run_info34
from ._restart11 import _restart11


class _print46(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info34()
        self.RESTART = _restart11()
        self._name = "PRINT"
        self._subsections = {'RESTART': 'RESTART', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

