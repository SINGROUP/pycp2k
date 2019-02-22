from pycp2k.inputsection import InputSection
from ._chi1 import _chi1
from ._mass3 import _mass3


class _ad_langevin1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Timecon_nh = None
        self.Timecon_langevin = None
        self.CHI = _chi1()
        self.MASS = _mass3()
        self._name = "AD_LANGEVIN"
        self._keywords = {'Timecon_langevin': 'TIMECON_LANGEVIN', 'Timecon_nh': 'TIMECON_NH'}
        self._subsections = {'CHI': 'CHI', 'MASS': 'MASS'}

