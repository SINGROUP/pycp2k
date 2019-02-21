from pycp2k.inputsection import InputSection


class _charge3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atom = None
        self.Charge = None
        self._name = "CHARGE"
        self._keywords = {'Atom': 'ATOM', 'Charge': 'CHARGE'}

