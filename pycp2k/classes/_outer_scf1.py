from pycp2k.inputsection import InputSection


class _outer_scf1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Type = None
        self.Optimizer = None
        self.Broyden_type = None
        self.Jacobian_type = None
        self.Jacobian_step = None
        self.Jacobian_freq = None
        self.Jacobian_restart = None
        self.Jacobian_vector = None
        self.Bisect_trust_count = None
        self.Eps_scf = None
        self.Diis_buffer_length = None
        self.Extrapolation_order = None
        self.Max_scf = None
        self.Max_ls = None
        self.Factor_ls = None
        self.Continue_ls = None
        self.Step_size = None
        self._name = "OUTER_SCF"
        self._keywords = {'Jacobian_step': 'JACOBIAN_STEP', 'Factor_ls': 'FACTOR_LS', 'Step_size': 'STEP_SIZE', 'Jacobian_restart': 'JACOBIAN_RESTART', 'Bisect_trust_count': 'BISECT_TRUST_COUNT', 'Jacobian_type': 'JACOBIAN_TYPE', 'Eps_scf': 'EPS_SCF', 'Continue_ls': 'CONTINUE_LS', 'Max_scf': 'MAX_SCF', 'Max_ls': 'MAX_LS', 'Jacobian_vector': 'JACOBIAN_VECTOR', 'Broyden_type': 'BROYDEN_TYPE', 'Optimizer': 'OPTIMIZER', 'Extrapolation_order': 'EXTRAPOLATION_ORDER', 'Jacobian_freq': 'JACOBIAN_FREQ', 'Type': 'TYPE', 'Diis_buffer_length': 'DIIS_BUFFER_LENGTH'}
        self._attributes = ['Section_parameters']

