from pycp2k.inputsection import InputSection
from ._print37 import _print37


class _real_time_propagation1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_iter = None
        self.Eps_iter = None
        self.Aspc_order = None
        self.Mat_exp = None
        self.Density_propagation = None
        self.Sc_check_start = None
        self.Exp_accuracy = None
        self.Propagator = None
        self.Initial_wfn = None
        self.Apply_delta_pulse = None
        self.Periodic = None
        self.Delta_pulse_direction = None
        self.Delta_pulse_scale = None
        self.Hfx_balance_in_core = None
        self.Mcweeny_max_iter = None
        self.Accuracy_refinement = None
        self.Mcweeny_eps = None
        self.PRINT = _print37()
        self._name = "REAL_TIME_PROPAGATION"
        self._keywords = {'Hfx_balance_in_core': 'HFX_BALANCE_IN_CORE', 'Mcweeny_eps': 'MCWEENY_EPS', 'Propagator': 'PROPAGATOR', 'Mcweeny_max_iter': 'MCWEENY_MAX_ITER', 'Sc_check_start': 'SC_CHECK_START', 'Initial_wfn': 'INITIAL_WFN', 'Mat_exp': 'MAT_EXP', 'Density_propagation': 'DENSITY_PROPAGATION', 'Delta_pulse_direction': 'DELTA_PULSE_DIRECTION', 'Apply_delta_pulse': 'APPLY_DELTA_PULSE', 'Delta_pulse_scale': 'DELTA_PULSE_SCALE', 'Exp_accuracy': 'EXP_ACCURACY', 'Accuracy_refinement': 'ACCURACY_REFINEMENT', 'Periodic': 'PERIODIC', 'Aspc_order': 'ASPC_ORDER', 'Eps_iter': 'EPS_ITER', 'Max_iter': 'MAX_ITER'}
        self._subsections = {'PRINT': 'PRINT'}

