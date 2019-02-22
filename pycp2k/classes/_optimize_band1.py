from pycp2k.inputsection import InputSection
from ._md2 import _md2
from ._diis1 import _diis1


class _optimize_band1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Opt_type = None
        self.Optimize_end_points = None
        self.MD = _md2()
        self.DIIS = _diis1()
        self._name = "OPTIMIZE_BAND"
        self._keywords = {'Opt_type': 'OPT_TYPE', 'Optimize_end_points': 'OPTIMIZE_END_POINTS'}
        self._subsections = {'MD': 'MD', 'DIIS': 'DIIS'}

