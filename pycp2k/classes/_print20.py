from pycp2k.inputsection import InputSection
from ._run_info1 import _run_info1
from ._atom_info1 import _atom_info1
from ._fock_gap1 import _fock_gap1
from ._fock_eigenvalues1 import _fock_eigenvalues1
from ._ml_variance1 import _ml_variance1
from ._ml_training_data1 import _ml_training_data1
from ._opt_info1 import _opt_info1
from ._restart7 import _restart7


class _print20(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.RUN_INFO = _run_info1()
        self.ATOM_INFO = _atom_info1()
        self.FOCK_GAP = _fock_gap1()
        self.FOCK_EIGENVALUES = _fock_eigenvalues1()
        self.ML_VARIANCE = _ml_variance1()
        self.ML_TRAINING_DATA = _ml_training_data1()
        self.OPT_INFO = _opt_info1()
        self.RESTART = _restart7()
        self._name = "PRINT"
        self._subsections = {'FOCK_EIGENVALUES': 'FOCK_EIGENVALUES', 'ML_TRAINING_DATA': 'ML_TRAINING_DATA', 'ATOM_INFO': 'ATOM_INFO', 'RUN_INFO': 'RUN_INFO', 'FOCK_GAP': 'FOCK_GAP', 'ML_VARIANCE': 'ML_VARIANCE', 'OPT_INFO': 'OPT_INFO', 'RESTART': 'RESTART'}

