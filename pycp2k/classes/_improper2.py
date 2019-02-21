from pycp2k.inputsection import InputSection


class _improper2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Atoms = []
        self._name = "IMPROPER"
        self._repeated_keywords = {'Atoms': 'ATOMS'}
        self._attributes = ['Section_parameters']

