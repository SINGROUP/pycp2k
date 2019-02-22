from pycp2k.inputsection import InputSection


class _screening10(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_schwarz = None
        self.Eps_schwarz_forces = None
        self.Screen_p_forces = None
        self.Screen_on_initial_p = None
        self.P_screen_correction_factor = None
        self._name = "SCREENING"
        self._keywords = {'Eps_schwarz_forces': 'EPS_SCHWARZ_FORCES', 'Screen_on_initial_p': 'SCREEN_ON_INITIAL_P', 'Eps_schwarz': 'EPS_SCHWARZ', 'P_screen_correction_factor': 'P_SCREEN_CORRECTION_FACTOR', 'Screen_p_forces': 'SCREEN_P_FORCES'}

