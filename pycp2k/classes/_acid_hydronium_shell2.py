from pycp2k.inputsection import InputSection


class _acid_hydronium_shell2(InputSection):
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
        self.Poo = None
        self.Qoo = None
        self.Roo = None
        self.Pm = None
        self.Qm = None
        self.Nh = None
        self.Pcut = None
        self.Qcut = None
        self.Nc = None
        self.Lambda = None
        self.Lambda = None
        self._name = "ACID_HYDRONIUM_SHELL"
        self._keywords = {'Qm': 'QM', 'Poo': 'POO', 'Qwoh': 'QWOH', 'Roo': 'ROO', 'Pwoh': 'PWOH', 'Lambda': 'LAMBDA', 'Paoh': 'PAOH', 'Qoo': 'QOO', 'Nh': 'NH', 'Qaoh': 'QAOH', 'Nc': 'NC', 'Rwoh': 'RWOH', 'Pcut': 'PCUT', 'Qcut': 'QCUT', 'Pm': 'PM', 'Raoh': 'RAOH'}
        self._repeated_keywords = {'Oxygens_acid': 'OXYGENS_ACID', 'Hydrogens': 'HYDROGENS', 'Oxygens_water': 'OXYGENS_WATER'}

