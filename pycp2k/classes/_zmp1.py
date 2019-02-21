from pycp2k.inputsection import InputSection
from ._restart16 import _restart16


class _zmp1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.File_density = None
        self.Grid_tol = None
        self.Lambda = None
        self.Dm = None
        self.RESTART = _restart16()
        self._name = "ZMP"
        self._keywords = {'Grid_tol': 'GRID_TOL', 'Dm': 'DM', 'Lambda': 'LAMBDA', 'File_density': 'FILE_DENSITY'}
        self._subsections = {'RESTART': 'RESTART'}

