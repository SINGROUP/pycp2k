from pycp2k.inputsection import InputSection
from ._program_run_info9 import _program_run_info9
from ._temperature_colvar1 import _temperature_colvar1
from ._colvar1 import _colvar1
from ._hills1 import _hills1


class _print13(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info9()
        self.TEMPERATURE_COLVAR = _temperature_colvar1()
        self.COLVAR = _colvar1()
        self.HILLS = _hills1()
        self._name = "PRINT"
        self._subsections = {'TEMPERATURE_COLVAR': 'TEMPERATURE_COLVAR', 'HILLS': 'HILLS', 'COLVAR': 'COLVAR', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

