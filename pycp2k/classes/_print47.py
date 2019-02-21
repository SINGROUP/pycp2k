from pycp2k.inputsection import InputSection
from ._neighbor_lists9 import _neighbor_lists9
from ._subcell5 import _subcell5


class _print47(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.NEIGHBOR_LISTS = _neighbor_lists9()
        self.SUBCELL = _subcell5()
        self._name = "PRINT"
        self._subsections = {'SUBCELL': 'SUBCELL', 'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS'}

