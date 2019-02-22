from pycp2k.inputsection import InputSection
from ._program_run_info25 import _program_run_info25
from ._restart10 import _restart10
from ._restart_history4 import _restart_history4
from ._current2 import _current2


class _print37(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.PROGRAM_RUN_INFO = _program_run_info25()
        self.RESTART = _restart10()
        self.RESTART_HISTORY = _restart_history4()
        self.CURRENT = _current2()
        self._name = "PRINT"
        self._subsections = {'CURRENT': 'CURRENT', 'RESTART': 'RESTART', 'RESTART_HISTORY': 'RESTART_HISTORY', 'PROGRAM_RUN_INFO': 'PROGRAM_RUN_INFO'}

