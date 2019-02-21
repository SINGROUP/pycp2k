from pycp2k.inputsection import InputSection


class _respa1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Frequency = None
        self._name = "RESPA"
        self._keywords = {'Frequency': 'FREQUENCY'}

