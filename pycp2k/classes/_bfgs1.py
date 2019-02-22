from pycp2k.inputsection import InputSection
from ._restart1 import _restart1


class _bfgs1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Trust_radius = None
        self.Use_model_hessian = None
        self.Use_rat_fun_opt = None
        self.Restart_hessian = None
        self.Restart_file_name = None
        self.RESTART = _restart1()
        self._name = "BFGS"
        self._keywords = {'Use_model_hessian': 'USE_MODEL_HESSIAN', 'Trust_radius': 'TRUST_RADIUS', 'Restart_hessian': 'RESTART_HESSIAN', 'Use_rat_fun_opt': 'USE_RAT_FUN_OPT', 'Restart_file_name': 'RESTART_FILE_NAME'}
        self._subsections = {'RESTART': 'RESTART'}

