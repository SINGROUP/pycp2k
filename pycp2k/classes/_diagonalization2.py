from pycp2k.inputsection import InputSection
from ._ot4 import _ot4
from ._krylov2 import _krylov2
from ._diag_sub_scf3 import _diag_sub_scf3
from ._davidson3 import _davidson3
from ._filter_matrix3 import _filter_matrix3


class _diagonalization2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Algorithm = None
        self.Jacobi_threshold = None
        self.Eps_jacobi = None
        self.Eps_adapt = None
        self.Max_iter = None
        self.Eps_iter = None
        self.OT = _ot4()
        self.KRYLOV = _krylov2()
        self.DIAG_SUB_SCF = _diag_sub_scf3()
        self.DAVIDSON = _davidson3()
        self.FILTER_MATRIX = _filter_matrix3()
        self._name = "DIAGONALIZATION"
        self._keywords = {'Eps_adapt': 'EPS_ADAPT', 'Jacobi_threshold': 'JACOBI_THRESHOLD', 'Algorithm': 'ALGORITHM', 'Eps_jacobi': 'EPS_JACOBI', 'Eps_iter': 'EPS_ITER', 'Max_iter': 'MAX_ITER'}
        self._subsections = {'FILTER_MATRIX': 'FILTER_MATRIX', 'DIAG_SUB_SCF': 'DIAG_SUB_SCF', 'DAVIDSON': 'DAVIDSON', 'KRYLOV': 'KRYLOV', 'OT': 'OT'}
        self._attributes = ['Section_parameters']

