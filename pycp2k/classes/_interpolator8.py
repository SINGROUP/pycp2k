from pycp2k.inputsection import InputSection
from ._conv_info8 import _conv_info8
from ._spl_coeffs1 import _spl_coeffs1


class _interpolator8(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Kind = None
        self.Safe_computation = None
        self.Aint_precond = None
        self.Precond = None
        self.Eps_x = None
        self.Eps_r = None
        self.Max_iter = None
        self.CONV_INFO = _conv_info8()
        self.SPL_COEFFS = _spl_coeffs1()
        self._name = "INTERPOLATOR"
        self._keywords = {'Aint_precond': 'AINT_PRECOND', 'Kind': 'KIND', 'Eps_x': 'EPS_X', 'Safe_computation': 'SAFE_COMPUTATION', 'Precond': 'PRECOND', 'Eps_r': 'EPS_R', 'Max_iter': 'MAX_ITER'}
        self._subsections = {'CONV_INFO': 'CONV_INFO', 'SPL_COEFFS': 'SPL_COEFFS'}
        self._aliases = {'Maxiter': 'Max_iter'}


    @property
    def Maxiter(self):
        """
        See documentation for Max_iter
        """
        return self.Max_iter

    @Maxiter.setter
    def Maxiter(self, value):
        self.Max_iter = value
