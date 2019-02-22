from pycp2k.inputsection import InputSection


class _generic1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Mixing_function = None
        self.Variables = None
        self.Parameters = []
        self.Values = []
        self.Units = []
        self.Dx = None
        self.Error_limit = None
        self._name = "GENERIC"
        self._keywords = {'Variables': 'VARIABLES', 'Error_limit': 'ERROR_LIMIT', 'Mixing_function': 'MIXING_FUNCTION', 'Dx': 'DX'}
        self._repeated_keywords = {'Units': 'UNITS', 'Parameters': 'PARAMETERS', 'Values': 'VALUES'}

