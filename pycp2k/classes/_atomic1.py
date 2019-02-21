from pycp2k.inputsection import InputSection


class _atomic1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Energy = None
        self.Pressure = None
        self._name = "ATOMIC"
        self._keywords = {'Pressure': 'PRESSURE', 'Energy': 'ENERGY'}

