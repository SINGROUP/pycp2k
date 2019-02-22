from pycp2k.inputsection import InputSection


class _tf5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self._name = "TF"
        self._attributes = ['Section_parameters']

