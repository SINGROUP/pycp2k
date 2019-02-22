from pycp2k.inputsection import InputSection


class _dielec_aa_cuboidal3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Dielectric_constant = None
        self.X_xtnt = None
        self.Y_xtnt = None
        self.Z_xtnt = None
        self.Smoothing_width = None
        self._name = "DIELEC_AA_CUBOIDAL"
        self._keywords = {'Z_xtnt': 'Z_XTNT', 'Dielectric_constant': 'DIELECTRIC_CONSTANT', 'Y_xtnt': 'Y_XTNT', 'Smoothing_width': 'SMOOTHING_WIDTH', 'X_xtnt': 'X_XTNT'}
        self._aliases = {'Zeta': 'Smoothing_width', 'Epsilon': 'Dielectric_constant'}


    @property
    def Epsilon(self):
        """
        See documentation for Dielectric_constant
        """
        return self.Dielectric_constant

    @property
    def Zeta(self):
        """
        See documentation for Smoothing_width
        """
        return self.Smoothing_width

    @Epsilon.setter
    def Epsilon(self, value):
        self.Dielectric_constant = value

    @Zeta.setter
    def Zeta(self, value):
        self.Smoothing_width = value
