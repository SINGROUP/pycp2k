from pycp2k.inputsection import InputSection


class _parameter1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Sk_file = []
        self.Param_file_path = None
        self.Param_file_name = None
        self.Dispersion_type = None
        self.Uff_force_field = None
        self.Dispersion_parameter_file = None
        self.Dispersion_radius = None
        self.Coordination_cutoff = None
        self.D3_scaling = None
        self.Hb_sr_param = None
        self._name = "PARAMETER"
        self._keywords = {'Uff_force_field': 'UFF_FORCE_FIELD', 'Dispersion_type': 'DISPERSION_TYPE', 'Hb_sr_param': 'HB_SR_PARAM', 'D3_scaling': 'D3_SCALING', 'Dispersion_parameter_file': 'DISPERSION_PARAMETER_FILE', 'Param_file_name': 'PARAM_FILE_NAME', 'Param_file_path': 'PARAM_FILE_PATH', 'Coordination_cutoff': 'COORDINATION_CUTOFF', 'Dispersion_radius': 'DISPERSION_RADIUS'}
        self._repeated_keywords = {'Sk_file': 'SK_FILE'}

