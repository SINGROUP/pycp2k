from pycp2k.inputsection import InputSection
from ._coord4 import _coord4
from ._velocity5 import _velocity5
from ._mass8 import _mass8
from ._force4 import _force4


class _nose4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Length = None
        self.Yoshida = None
        self.Timecon = None
        self.Mts = None
        self.COORD = _coord4()
        self.VELOCITY = _velocity5()
        self.MASS = _mass8()
        self.FORCE = _force4()
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
