from pycp2k.inputsection import InputSection


class _mt2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Alpha = None
        self.Rel_cutoff = None
        self._name = "MT"
        self._keywords = {'Alpha': 'ALPHA', 'Rel_cutoff': 'REL_CUTOFF'}

