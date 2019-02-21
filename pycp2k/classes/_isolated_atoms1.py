from pycp2k.inputsection import InputSection


class _isolated_atoms1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.List = []
        self._name = "ISOLATED_ATOMS"
        self._repeated_keywords = {'List': 'LIST'}

