from pycp2k.inputsection import InputSection


class _sic2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Sic_scaling_a = None
        self.Sic_scaling_b = None
        self.Sic_method = None
        self.Orbital_set = None
        self._name = "SIC"
        self._keywords = {'Sic_method': 'SIC_METHOD', 'Orbital_set': 'ORBITAL_SET', 'Sic_scaling_b': 'SIC_SCALING_B', 'Sic_scaling_a': 'SIC_SCALING_A'}

