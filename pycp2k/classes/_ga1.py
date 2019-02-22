from pycp2k.inputsection import InputSection


class _ga1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ncells = None
        self._name = "GA"
        self._keywords = {'Ncells': 'NCELLS'}

