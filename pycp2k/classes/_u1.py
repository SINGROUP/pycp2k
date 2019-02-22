from pycp2k.inputsection import InputSection
from ._mixed2 import _mixed2


class _u1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.MIXED = _mixed2()
        self._name = "U"
        self._subsections = {'MIXED': 'MIXED'}

