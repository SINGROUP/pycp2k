from pycp2k.inputsection import InputSection


class _relativistic1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.Dkh_order = None
        self.Zora_type = None
        self.Transformation = None
        self.Z_cutoff = None
        self.Potential = None
        self._name = "RELATIVISTIC"
        self._keywords = {'Dkh_order': 'DKH_ORDER', 'Method': 'METHOD', 'Potential': 'POTENTIAL', 'Zora_type': 'ZORA_TYPE', 'Transformation': 'TRANSFORMATION', 'Z_cutoff': 'Z_CUTOFF'}

