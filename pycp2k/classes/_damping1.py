from pycp2k.inputsection import InputSection


class _damping1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atom = None
        self.Type = None
        self.Order = None
        self.Bij = None
        self.Cij = None
        self._name = "DAMPING"
        self._keywords = {'Atom': 'ATOM', 'Cij': 'CIJ', 'Order': 'ORDER', 'Type': 'TYPE', 'Bij': 'BIJ'}

