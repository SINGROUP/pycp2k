from pycp2k.inputsection import InputSection


class _history2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Energy_precision = None
        self.Fingerprint_precision = None
        self._name = "HISTORY"
        self._keywords = {'Energy_precision': 'ENERGY_PRECISION', 'Fingerprint_precision': 'FINGERPRINT_PRECISION'}

