from pycp2k.inputsection import InputSection


class _periodic14(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Number_of_shells = None
        self._name = "PERIODIC"
        self._keywords = {'Number_of_shells': 'NUMBER_OF_SHELLS'}

