from pycp2k.inputsection import InputSection
from ._coord13 import _coord13


class _frame3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Coord_file_name = None
        self.COORD = _coord13()
        self._name = "FRAME"
        self._keywords = {'Coord_file_name': 'COORD_FILE_NAME'}
        self._subsections = {'COORD': 'COORD'}

