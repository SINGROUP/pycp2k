from pycp2k.inputsection import InputSection
from ._program_run_info6 import _program_run_info6
from ._cell1 import _cell1


class _print4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info6()
        self.CELL = _cell1()
        self._name = "PRINT"
        self._subsections = {'CELL': 'CELL', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

