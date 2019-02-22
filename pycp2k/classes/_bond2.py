from pycp2k.inputsection import InputSection


class _bond2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Atoms = []
        self._name = "BOND"
        self._repeated_keywords = {'Atoms': 'ATOMS'}
        self._attributes = ['Section_parameters']
