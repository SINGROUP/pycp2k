from pycp2k.inputsection import InputSection


class _genpot2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.Function = None
        self.Variables = None
        self.Parameters = []
        self.Values = []
        self.Units = []
        self.Rcut = None
        self.Rmin = None
        self.Rmax = None
        self._name = "GENPOT"
        self._keywords = {'Variables': 'VARIABLES', 'Atoms': 'ATOMS', 'Function': 'FUNCTION', 'Rcut': 'RCUT', 'Rmax': 'RMAX', 'Rmin': 'RMIN'}
        self._repeated_keywords = {'Units': 'UNITS', 'Parameters': 'PARAMETERS', 'Values': 'VALUES'}

