from pycp2k.inputsection import InputSection
from ._mixed3 import _mixed3


class _u2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.MIXED = _mixed3()
        self._name = "U"
        self._subsections = {'MIXED': 'MIXED'}

