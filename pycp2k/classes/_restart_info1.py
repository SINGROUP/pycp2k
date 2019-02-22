from pycp2k.inputsection import InputSection


class _restart_info1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Indices = []
        self.Labels = []
        self._name = "RESTART_INFO"
        self._repeated_keywords = {'Indices': 'INDICES', 'Labels': 'LABELS'}

