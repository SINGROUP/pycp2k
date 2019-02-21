from pycp2k.inputsection import InputSection
from ._ms_restart1 import _ms_restart1


class _print66(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.MS_RESTART = _ms_restart1()
        self._name = "PRINT"
        self._subsections = {'MS_RESTART': 'MS_RESTART'}

