from pycp2k.inputsection import InputSection
from ._mt1 import _mt1
from ._wavelet1 import _wavelet1
from ._multipole1 import _multipole1
from ._ewald1 import _ewald1
from ._implicit1 import _implicit1


class _poisson1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Poisson_solver = None
        self.Periodic = None
        self.MT = _mt1()
        self.WAVELET = _wavelet1()
        self.MULTIPOLE = _multipole1()
        self.EWALD = _ewald1()
        self.IMPLICIT = _implicit1()
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
