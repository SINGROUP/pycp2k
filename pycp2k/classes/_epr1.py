from pycp2k.inputsection import InputSection
from ._print59 import _print59
from ._interpolator12 import _interpolator12


class _epr1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Restart_epr = None
        self.PRINT = _print59()
        self.INTERPOLATOR = _interpolator12()
        self._name = "EPR"
        self._keywords = {'Restart_epr': 'RESTART_EPR'}
        self._subsections = {'INTERPOLATOR': 'INTERPOLATOR', 'PRINT': 'PRINT'}
        self._attributes = ['Section_parameters']

