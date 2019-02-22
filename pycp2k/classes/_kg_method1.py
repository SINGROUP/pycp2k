from pycp2k.inputsection import InputSection
from ._print23 import _print23
from ._energy_correction1 import _energy_correction1


class _kg_method1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Coloring_method = None
        self.Tnadd_method = None
        self.PRINT = _print23()
        self.ENERGY_CORRECTION = _energy_correction1()
        self._name = "KG_METHOD"
        self._keywords = {'Coloring_method': 'COLORING_METHOD', 'Tnadd_method': 'TNADD_METHOD'}
        self._subsections = {'ENERGY_CORRECTION': 'ENERGY_CORRECTION', 'PRINT': 'PRINT'}

