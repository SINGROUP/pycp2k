from pycp2k.inputsection import InputSection
from ._coord9 import _coord9
from ._velocity9 import _velocity9


class _replica1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Collective = None
        self.Coord_file_name = None
        self.COORD = _coord9()
        self.VELOCITY = _velocity9()
        self._name = "REPLICA"
        self._keywords = {'Coord_file_name': 'COORD_FILE_NAME', 'Collective': 'COLLECTIVE'}
        self._subsections = {'VELOCITY': 'VELOCITY', 'COORD': 'COORD'}

