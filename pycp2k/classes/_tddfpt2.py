from pycp2k.inputsection import InputSection
from ._dipole_moments1 import _dipole_moments1
from ._mgrid2 import _mgrid2
from ._print63 import _print63


class _tddfpt2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Nstates = None
        self.Max_iter = None
        self.Max_kv = None
        self.Nproc_state = None
        self.Convergence = None
        self.Min_amplitude = None
        self.Orthogonal_eps = None
        self.Restart = None
        self.Rks_triplets = None
        self.Wfn_restart_file_name = None
        self.DIPOLE_MOMENTS = _dipole_moments1()
        self.MGRID = _mgrid2()
        self.PRINT = _print63()
        self._name = "TDDFPT"
        self._keywords = {'Nproc_state': 'NPROC_STATE', 'Min_amplitude': 'MIN_AMPLITUDE', 'Nstates': 'NSTATES', 'Restart': 'RESTART', 'Rks_triplets': 'RKS_TRIPLETS', 'Orthogonal_eps': 'ORTHOGONAL_EPS', 'Max_kv': 'MAX_KV', 'Max_iter': 'MAX_ITER', 'Wfn_restart_file_name': 'WFN_RESTART_FILE_NAME', 'Convergence': 'CONVERGENCE'}
        self._subsections = {'MGRID': 'MGRID', 'PRINT': 'PRINT', 'DIPOLE_MOMENTS': 'DIPOLE_MOMENTS'}
        self._aliases = {'Restart_file_name': 'Wfn_restart_file_name'}
        self._attributes = ['Section_parameters']


    @property
    def Restart_file_name(self):
        """
        See documentation for Wfn_restart_file_name
        """
        return self.Wfn_restart_file_name

    @Restart_file_name.setter
    def Restart_file_name(self, value):
        self.Wfn_restart_file_name = value
