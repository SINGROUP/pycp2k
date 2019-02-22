from pycp2k.inputsection import InputSection


class _define_region6(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.List = []
        self.Temperature = None
        self.Temp_tol = None
        self.Do_langevin = None
        self.Noisy_gamma_region = None
        self._name = "DEFINE_REGION"
        self._keywords = {'Do_langevin': 'DO_LANGEVIN', 'Noisy_gamma_region': 'NOISY_GAMMA_REGION', 'Temperature': 'TEMPERATURE', 'Temp_tol': 'TEMP_TOL'}
        self._repeated_keywords = {'List': 'LIST'}

