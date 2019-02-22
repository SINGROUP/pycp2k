from pycp2k.inputsection import InputSection


class _pao_potential1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Maxl = None
        self.Beta = None
        self.Weight = None
        self.Max_projector = None
        self._name = "PAO_POTENTIAL"
        self._keywords = {'Max_projector': 'MAX_PROJECTOR', 'Weight': 'WEIGHT', 'Maxl': 'MAXL', 'Beta': 'BETA'}

