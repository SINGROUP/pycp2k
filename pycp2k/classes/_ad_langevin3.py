from pycp2k.inputsection import InputSection
from ._chi3 import _chi3
from ._mass7 import _mass7


class _ad_langevin3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Timecon_nh = None
        self.Timecon_langevin = None
        self.CHI = _chi3()
        self.MASS = _mass7()
        self._name = "AD_LANGEVIN"
        self._keywords = {'Timecon_langevin': 'TIMECON_LANGEVIN', 'Timecon_nh': 'TIMECON_NH'}
        self._subsections = {'CHI': 'CHI', 'MASS': 'MASS'}

