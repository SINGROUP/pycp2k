from pycp2k.inputsection import InputSection


class _coupling1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Coupling_parameter = None
        self._name = "COUPLING"
        self._keywords = {'Coupling_parameter': 'COUPLING_PARAMETER'}

