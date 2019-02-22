from pycp2k.inputsection import InputSection


class _mixed2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Energy_function = None
        self.Variables = None
        self.Parameters = []
        self.Values = []
        self.Units = []
        self.Dx = None
        self.Error_limit = None
        self._name = "MIXED"
        self._keywords = {'Variables': 'VARIABLES', 'Error_limit': 'ERROR_LIMIT', 'Energy_function': 'ENERGY_FUNCTION', 'Dx': 'DX'}
        self._repeated_keywords = {'Units': 'UNITS', 'Parameters': 'PARAMETERS', 'Values': 'VALUES'}

