from pycp2k.inputsection import InputSection


class _pao_descriptor1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Beta = None
        self.Screening = None
        self.Weight = None
        self._name = "PAO_DESCRIPTOR"
        self._keywords = {'Screening': 'SCREENING', 'Weight': 'WEIGHT', 'Beta': 'BETA'}

