from pycp2k.inputsection import InputSection
from ._polar_matrix1 import _polar_matrix1


class _print60(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.POLAR_MATRIX = _polar_matrix1()
        self._name = "PRINT"
        self._subsections = {'POLAR_MATRIX': 'POLAR_MATRIX'}

