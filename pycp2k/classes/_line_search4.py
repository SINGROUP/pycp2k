from pycp2k.inputsection import InputSection
from ._num2pnt4 import _num2pnt4
from ._gold4 import _gold4


class _line_search4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self._2PNT = _num2pnt4()
        self.GOLD = _gold4()
        self._name = "LINE_SEARCH"
        self._keywords = {'Type': 'TYPE'}
        self._subsections = {'GOLD': 'GOLD', '_2PNT': '2PNT'}

