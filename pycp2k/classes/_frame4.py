from pycp2k.inputsection import InputSection
from ._coord14 import _coord14


class _frame4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Coord_file_name = None
        self.COORD = _coord14()
        self._name = "FRAME"
        self._keywords = {'Coord_file_name': 'COORD_FILE_NAME'}
        self._subsections = {'COORD': 'COORD'}

