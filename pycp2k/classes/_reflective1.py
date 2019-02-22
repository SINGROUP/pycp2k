from pycp2k.inputsection import InputSection


class _reflective1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Direction = None
        self._name = "REFLECTIVE"
        self._keywords = {'Direction': 'DIRECTION'}

