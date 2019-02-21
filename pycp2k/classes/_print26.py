from pycp2k.inputsection import InputSection
from ._neighbor_lists3 import _neighbor_lists3
from ._subcell1 import _subcell1
from ._ewald_info1 import _ewald_info1


class _print26(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.NEIGHBOR_LISTS = _neighbor_lists3()
        self.SUBCELL = _subcell1()
        self.EWALD_INFO = _ewald_info1()
        self._name = "PRINT"
        self._subsections = {'EWALD_INFO': 'EWALD_INFO', 'SUBCELL': 'SUBCELL', 'NEIGHBOR_LISTS': 'NEIGHBOR_LISTS'}

