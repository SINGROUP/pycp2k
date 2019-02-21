from pycp2k.inputsection import InputSection


class _exchange1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Cutoff = None
        self.Rc_taper = None
        self.Rc_range = None
        self._name = "EXCHANGE"
        self._keywords = {'Rc_range': 'RC_RANGE', 'Cutoff': 'CUTOFF', 'Rc_taper': 'RC_TAPER'}

