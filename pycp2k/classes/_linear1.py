from pycp2k.inputsection import InputSection


class _linear1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Lambda = None
        self._name = "LINEAR"
        self._keywords = {'Lambda': 'LAMBDA'}

