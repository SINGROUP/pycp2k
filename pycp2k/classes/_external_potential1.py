from pycp2k.inputsection import InputSection


class _external_potential1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms_list = []
        self.Function = None
        self.Parameters = []
        self.Values = []
        self.Units = []
        self.Dx = None
        self.Error_limit = None
        self._name = "EXTERNAL_POTENTIAL"
        self._keywords = {'Error_limit': 'ERROR_LIMIT', 'Dx': 'DX', 'Function': 'FUNCTION'}
        self._repeated_keywords = {'Units': 'UNITS', 'Atoms_list': 'ATOMS_LIST', 'Values': 'VALUES', 'Parameters': 'PARAMETERS'}

