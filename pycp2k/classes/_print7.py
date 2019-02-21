from pycp2k.inputsection import InputSection
from ._energy2 import _energy2


class _print7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.ENERGY = _energy2()
        self._name = "PRINT"
        self._subsections = {'ENERGY': 'ENERGY'}

