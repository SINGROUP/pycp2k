from pycp2k.inputsection import InputSection


class _init1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Levy_pos_sample = None
        self.Levy_correlated = None
        self.Levy_temp_factor = None
        self.Levy_seed = None
        self.Thermostat_seed = None
        self.Randomize_pos = None
        self.Centroid_speed = None
        self.Velocity_quench = None
        self.Velocity_scale = None
        self._name = "INIT"
        self._keywords = {'Levy_pos_sample': 'LEVY_POS_SAMPLE', 'Levy_seed': 'LEVY_SEED', 'Randomize_pos': 'RANDOMIZE_POS', 'Velocity_quench': 'VELOCITY_QUENCH', 'Centroid_speed': 'CENTROID_SPEED', 'Thermostat_seed': 'THERMOSTAT_SEED', 'Levy_correlated': 'LEVY_CORRELATED', 'Levy_temp_factor': 'LEVY_TEMP_FACTOR', 'Velocity_scale': 'VELOCITY_SCALE'}

