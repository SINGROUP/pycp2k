from pycp2k.inputsection import InputSection


class _external_potential2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Function = None
        self.Parameters = []
        self.Values = []
        self.Units = []
        self.Static = None
        self.Dx = None
        self.Error_limit = None
        self.Read_from_cube = None
        self.Scaling_factor = None
        self._name = "EXTERNAL_POTENTIAL"
        self._keywords = {'Scaling_factor': 'SCALING_FACTOR', 'Static': 'STATIC', 'Read_from_cube': 'READ_FROM_CUBE', 'Error_limit': 'ERROR_LIMIT', 'Dx': 'DX', 'Function': 'FUNCTION'}
        self._repeated_keywords = {'Units': 'UNITS', 'Parameters': 'PARAMETERS', 'Values': 'VALUES'}

