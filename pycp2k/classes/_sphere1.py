from pycp2k.inputsection import InputSection
from ._center1 import _center1


class _sphere1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Radius = None
        self.CENTER = _center1()
        self._name = "SPHERE"
        self._keywords = {'Radius': 'RADIUS'}
        self._subsections = {'CENTER': 'CENTER'}

