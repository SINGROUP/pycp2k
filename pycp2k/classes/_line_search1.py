from pycp2k.inputsection import InputSection
from ._num2pnt1 import _num2pnt1
from ._gold1 import _gold1


class _line_search1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self._2PNT = _num2pnt1()
        self.GOLD = _gold1()
        self._name = "LINE_SEARCH"
        self._keywords = {'Type': 'TYPE'}
        self._subsections = {'GOLD': 'GOLD', '_2PNT': '2PNT'}

