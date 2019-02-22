from pycp2k.inputsection import InputSection
from ._curvy_steps1 import _curvy_steps1
from ._chebyshev1 import _chebyshev1
from ._rho_mixing1 import _rho_mixing1
from ._pexsi1 import _pexsi1
from ._pao1 import _pao1


class _ls_scf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ls_diis = None
        self.Ini_diis = None
        self.Max_diis = None
        self.Nmixing = None
        self.Eps_diis = None
        self.Max_scf = None
        self.Eps_scf = None
        self.Mixing_fraction = None
        self.Eps_filter = None
        self.Eps_lanczos = None
        self.Max_iter_lanczos = None
        self.Mu = None
        self.Fixed_mu = None
        self.Extrapolation_order = None
        self.S_preconditioner = None
        self.Purification_method = None
        self.Dynamic_threshold = None
        self.Non_monotonic = None
        self.Matrix_cluster_type = None
        self.Single_precision_matrices = None
        self.Restart_write = None
        self.Restart_read = None
        self.S_inversion = None
        self.Sign_sqrt_order = None
        self.Report_all_sparsities = None
        self.Perform_mu_scan = None
        self.Check_s_inv = None
        self.CURVY_STEPS = _curvy_steps1()
        self.CHEBYSHEV = _chebyshev1()
        self.RHO_MIXING = _rho_mixing1()
        self.PEXSI = _pexsi1()
        self.PAO = _pao1()
        self._name = "LS_SCF"
        self._keywords = {'Dynamic_threshold': 'DYNAMIC_THRESHOLD', 'Eps_diis': 'EPS_DIIS', 'Max_diis': 'MAX_DIIS', 'Max_scf': 'MAX_SCF', 'Purification_method': 'PURIFICATION_METHOD', 'Mixing_fraction': 'MIXING_FRACTION', 'Check_s_inv': 'CHECK_S_INV', 'Extrapolation_order': 'EXTRAPOLATION_ORDER', 'Sign_sqrt_order': 'SIGN_SQRT_ORDER', 'Perform_mu_scan': 'PERFORM_MU_SCAN', 'S_inversion': 'S_INVERSION', 'S_preconditioner': 'S_PRECONDITIONER', 'Ls_diis': 'LS_DIIS', 'Nmixing': 'NMIXING', 'Restart_read': 'RESTART_READ', 'Eps_scf': 'EPS_SCF', 'Ini_diis': 'INI_DIIS', 'Report_all_sparsities': 'REPORT_ALL_SPARSITIES', 'Mu': 'MU', 'Max_iter_lanczos': 'MAX_ITER_LANCZOS', 'Eps_filter': 'EPS_FILTER', 'Eps_lanczos': 'EPS_LANCZOS', 'Matrix_cluster_type': 'MATRIX_CLUSTER_TYPE', 'Fixed_mu': 'FIXED_MU', 'Single_precision_matrices': 'SINGLE_PRECISION_MATRICES', 'Non_monotonic': 'NON_MONOTONIC', 'Restart_write': 'RESTART_WRITE'}
        self._subsections = {'PAO': 'PAO', 'PEXSI': 'PEXSI', 'CHEBYSHEV': 'CHEBYSHEV', 'RHO_MIXING': 'RHO_MIXING', 'CURVY_STEPS': 'CURVY_STEPS'}

