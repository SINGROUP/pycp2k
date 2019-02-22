from pycp2k.inputsection import InputSection
from ._mt3 import _mt3
from ._wavelet3 import _wavelet3
from ._multipole4 import _multipole4
from ._ewald3 import _ewald3
from ._implicit3 import _implicit3


class _poisson3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Poisson_solver = None
        self.Periodic = None
        self.MT = _mt3()
        self.WAVELET = _wavelet3()
        self.MULTIPOLE = _multipole4()
        self.EWALD = _ewald3()
        self.IMPLICIT = _implicit3()
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
