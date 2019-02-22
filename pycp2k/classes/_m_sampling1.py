from pycp2k.inputsection import InputSection


class _m_sampling1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Distribution_type = None
        self.M_value = None
        self.M_ratio = None
        self._name = "M-SAMPLING"
        self._keywords = {'Distribution_type': 'DISTRIBUTION-TYPE', 'M_value': 'M-VALUE', 'M_ratio': 'M-RATIO'}

