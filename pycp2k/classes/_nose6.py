from pycp2k.inputsection import InputSection
from ._coord7 import _coord7
from ._velocity8 import _velocity8


class _nose6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nnos = None
        self.COORD = _coord7()
        self.VELOCITY = _velocity8()
        self._name = "NOSE"
        self._keywords = {'Nnos': 'NNOS'}
        self._subsections = {'VELOCITY': 'VELOCITY', 'COORD': 'COORD'}

