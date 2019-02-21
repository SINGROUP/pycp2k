from pycp2k.inputsection import InputSection


class _quartic1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Direction = None
        self.K = None
        self._name = "QUARTIC"
        self._keywords = {'Direction': 'DIRECTION', 'K': 'K'}

