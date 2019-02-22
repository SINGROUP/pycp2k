from pycp2k.inputsection import InputSection


class _low_spin_roks1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Energy_scaling = None
        self.Spin_configuration = []
        self._name = "LOW_SPIN_ROKS"
        self._keywords = {'Energy_scaling': 'ENERGY_SCALING'}
        self._repeated_keywords = {'Spin_configuration': 'SPIN_CONFIGURATION'}

