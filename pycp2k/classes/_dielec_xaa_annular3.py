from pycp2k.inputsection import InputSection


class _dielec_xaa_annular3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Dielectric_constant = None
        self.X_xtnt = None
        self.Base_center = None
        self.Base_radii = None
        self.Smoothing_width = None
        self._name = "DIELEC_XAA_ANNULAR"
        self._keywords = {'Base_radii': 'BASE_RADII', 'Dielectric_constant': 'DIELECTRIC_CONSTANT', 'Base_center': 'BASE_CENTER', 'Smoothing_width': 'SMOOTHING_WIDTH', 'X_xtnt': 'X_XTNT'}
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
