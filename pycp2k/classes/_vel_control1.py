from pycp2k.inputsection import InputSection


class _vel_control1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Annealing = None
        self.Proj_velocity_verlet = None
        self.Sd_like = None
        self._name = "VEL_CONTROL"
        self._keywords = {'Proj_velocity_verlet': 'PROJ_VELOCITY_VERLET', 'Sd_like': 'SD_LIKE', 'Annealing': 'ANNEALING'}

