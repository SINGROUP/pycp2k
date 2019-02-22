from pycp2k.inputsection import InputSection
from ._num2pnt2 import _num2pnt2
from ._gold2 import _gold2


class _line_search2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self._2PNT = _num2pnt2()
        self.GOLD = _gold2()
        self._name = "LINE_SEARCH"
        self._keywords = {'Type': 'TYPE'}
        self._subsections = {'GOLD': 'GOLD', '_2PNT': '2PNT'}

