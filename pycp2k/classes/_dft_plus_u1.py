from pycp2k.inputsection import InputSection
from ._enforce_occupation1 import _enforce_occupation1


class _dft_plus_u1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.L = None
        self.U_minus_j = None
        self.U_ramping = None
        self.Eps_u_ramping = None
        self.Init_u_ramping_each_scf = None
        self.ENFORCE_OCCUPATION = _enforce_occupation1()
        self._name = "DFT_PLUS_U"
        self._keywords = {'Eps_u_ramping': 'EPS_U_RAMPING', 'Init_u_ramping_each_scf': 'INIT_U_RAMPING_EACH_SCF', 'L': 'L', 'U_minus_j': 'U_MINUS_J', 'U_ramping': 'U_RAMPING'}
        self._subsections = {'ENFORCE_OCCUPATION': 'ENFORCE_OCCUPATION'}
        self._attributes = ['Section_parameters']

