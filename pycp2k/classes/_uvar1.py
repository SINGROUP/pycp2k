from pycp2k.inputsection import InputSection


class _uvar1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Colvar = None
        self._name = "UVAR"
        self._keywords = {'Colvar': 'COLVAR'}

