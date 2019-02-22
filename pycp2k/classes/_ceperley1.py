from pycp2k.inputsection import InputSection
from ._m_sampling1 import _m_sampling1


class _ceperley1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Bisection = None
        self.Max_perm_cycle = None
        self.M_SAMPLING = _m_sampling1()
        self._name = "CEPERLEY"
        self._keywords = {'Bisection': 'BISECTION', 'Max_perm_cycle': 'MAX_PERM_CYCLE'}
        self._subsections = {'M_SAMPLING': 'M-SAMPLING'}

