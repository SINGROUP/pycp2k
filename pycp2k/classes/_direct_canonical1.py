from pycp2k.inputsection import InputSection


class _direct_canonical1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Big_send = None
        self._name = "DIRECT_CANONICAL"
        self._keywords = {'Big_send': 'BIG_SEND'}

