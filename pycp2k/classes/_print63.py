from pycp2k.inputsection import InputSection
from ._guess_vectors1 import _guess_vectors1
from ._iteration_info4 import _iteration_info4
from ._detailed_energy3 import _detailed_energy3
from ._restart13 import _restart13


class _print63(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.GUESS_VECTORS = _guess_vectors1()
        self.ITERATION_INFO = _iteration_info4()
        self.DETAILED_ENERGY = _detailed_energy3()
        self.RESTART = _restart13()
        self._name = "PRINT"
        self._subsections = {'RESTART': 'RESTART', 'GUESS_VECTORS': 'GUESS_VECTORS', 'DETAILED_ENERGY': 'DETAILED_ENERGY', 'ITERATION_INFO': 'ITERATION_INFO'}

