from pycp2k.inputsection import InputSection
from ._coord3 import _coord3
from ._velocity4 import _velocity4
from ._mass6 import _mass6
from ._force3 import _force3


class _nose3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Length = None
        self.Yoshida = None
        self.Timecon = None
        self.Mts = None
        self.COORD = _coord3()
        self.VELOCITY = _velocity4()
        self.MASS = _mass6()
        self.FORCE = _force3()
        self._name = "NOSE"
        self._keywords = {'Yoshida': 'YOSHIDA', 'Length': 'LENGTH', 'Mts': 'MTS', 'Timecon': 'TIMECON'}
        self._subsections = {'VELOCITY': 'VELOCITY', 'COORD': 'COORD', 'FORCE': 'FORCE', 'MASS': 'MASS'}
        self._aliases = {'Mult_t_steps': 'Mts', 'Multiple_time_steps': 'Mts'}


    @property
    def Multiple_time_steps(self):
        """
        See documentation for Mts
        """
        return self.Mts

    @property
    def Mult_t_steps(self):
        """
        See documentation for Mts
        """
        return self.Mts

    @Multiple_time_steps.setter
    def Multiple_time_steps(self, value):
        self.Mts = value

    @Mult_t_steps.setter
    def Mult_t_steps(self, value):
        self.Mts = value
