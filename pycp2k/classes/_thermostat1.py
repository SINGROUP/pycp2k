from pycp2k.inputsection import InputSection
from ._nose1 import _nose1
from ._csvr1 import _csvr1
from ._gle1 import _gle1
from ._ad_langevin1 import _ad_langevin1
from ._print6 import _print6


class _thermostat1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Type = None
        self.NOSE = _nose1()
        self.CSVR = _csvr1()
        self.GLE = _gle1()
        self.AD_LANGEVIN = _ad_langevin1()
        self.PRINT = _print6()
        self._name = "THERMOSTAT"
        self._keywords = {'Type': 'TYPE'}
        self._subsections = {'AD_LANGEVIN': 'AD_LANGEVIN', 'NOSE': 'NOSE', 'GLE': 'GLE', 'CSVR': 'CSVR', 'PRINT': 'PRINT'}

