from pycp2k.inputsection import InputSection
from ._subcell4 import _subcell4
from ._neighbor_lists7 import _neighbor_lists7


class _print42(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.SUBCELL = _subcell4()
        self.NEIGHBOR_LISTS = _neighbor_lists7()
        self._name = "PRINT"
        self._subsections = {'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS', 'SUBCELL': 'SUBCELL'}

