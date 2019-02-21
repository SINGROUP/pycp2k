from pycp2k.inputsection import InputSection


class _screening3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Rc_taper = None
        self.Rc_range = None
        self._name = "SCREENING"
        self._keywords = {'Rc_range': 'RC_RANGE', 'Rc_taper': 'RC_TAPER'}

