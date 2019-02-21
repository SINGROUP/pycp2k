from pycp2k.inputsection import InputSection
from ._current1 import _current1


class _print31(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.CURRENT = _current1()
        self._name = "PRINT"
        self._subsections = {'CURRENT': 'CURRENT'}

