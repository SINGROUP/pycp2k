from pycp2k.inputsection import InputSection
from ._coord5 import _coord5
from ._velocity6 import _velocity6
from ._mass9 import _mass9
from ._force5 import _force5


class _nose5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Length = None
        self.Yoshida = None
        self.Timecon = None
        self.Mts = None
        self.COORD = _coord5()
        self.VELOCITY = _velocity6()
        self.MASS = _mass9()
        self.FORCE = _force5()
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
