from pycp2k.inputsection import InputSection
from ._mt2 import _mt2
from ._wavelet2 import _wavelet2
from ._multipole2 import _multipole2
from ._ewald2 import _ewald2
from ._implicit2 import _implicit2


class _poisson2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Poisson_solver = None
        self.Periodic = None
        self.MT = _mt2()
        self.WAVELET = _wavelet2()
        self.MULTIPOLE = _multipole2()
        self.EWALD = _ewald2()
        self.IMPLICIT = _implicit2()
        self._name = "POISSON"
        self._keywords = {'Periodic': 'PERIODIC', 'Poisson_solver': 'POISSON_SOLVER'}
        self._subsections = {'MULTIPOLE': 'MULTIPOLE', 'MT': 'MT', 'WAVELET': 'WAVELET', 'EWALD': 'EWALD', 'IMPLICIT': 'IMPLICIT'}
        self._aliases = {'Psolver': 'Poisson_solver', 'Poisson': 'Poisson_solver'}


    @property
    def Poisson(self):
        """
        See documentation for Poisson_solver
        """
        return self.Poisson_solver

    @property
    def Psolver(self):
        """
        See documentation for Poisson_solver
        """
        return self.Poisson_solver

    @Poisson.setter
    def Poisson(self, value):
        self.Poisson_solver = value

    @Psolver.setter
    def Psolver(self, value):
        self.Poisson_solver = value
