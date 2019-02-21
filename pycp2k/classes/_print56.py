from pycp2k.inputsection import InputSection
from ._k_matrix1 import _k_matrix1


class _print56(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.K_MATRIX = _k_matrix1()
        self._name = "PRINT"
        self._subsections = {'K_MATRIX': 'K_MATRIX'}

