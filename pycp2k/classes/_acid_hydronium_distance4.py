from pycp2k.inputsection import InputSection


class _acid_hydronium_distance4(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Oxygens_water = []
        self.Oxygens_acid = []
        self.Hydrogens = []
        self.Pwoh = None
        self.Qwoh = None
        self.Rwoh = None
        self.Paoh = None
        self.Qaoh = None
        self.Raoh = None
        self.Pcut = None
        self.Qcut = None
        self.Nc = None
        self.Lambda = None
        self.Lambda = None
        self._name = "ACID_HYDRONIUM_DISTANCE"
        self._keywords = {'Paoh': 'PAOH', 'Qaoh': 'QAOH', 'Nc': 'NC', 'Qwoh': 'QWOH', 'Lambda': 'LAMBDA', 'Rwoh': 'RWOH', 'Pcut': 'PCUT', 'Qcut': 'QCUT', 'Pwoh': 'PWOH', 'Raoh': 'RAOH'}
        self._repeated_keywords = {'Oxygens_acid': 'OXYGENS_ACID', 'Hydrogens': 'HYDROGENS', 'Oxygens_water': 'OXYGENS_WATER'}

