from pycp2k.inputsection import InputSection
from ._mixed4 import _mixed4


class _u3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.MIXED = _mixed4()
        self._name = "U"
        self._subsections = {'MIXED': 'MIXED'}

