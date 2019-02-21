from pycp2k.inputsection import InputSection


class _temp_control1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Temperature = None
        self.Temp_tol = None
        self.Temp_tol_steps = None
        self._name = "TEMP_CONTROL"
        self._keywords = {'Temp_tol_steps': 'TEMP_TOL_STEPS', 'Temperature': 'TEMPERATURE', 'Temp_tol': 'TEMP_TOL'}

