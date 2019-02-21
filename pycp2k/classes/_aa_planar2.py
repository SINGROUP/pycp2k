from pycp2k.inputsection import InputSection


class _aa_planar2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.V_d = None
        self.Oscillating_fraction = None
        self.Frequency = None
        self.Phase = None
        self.Parallel_plane = None
        self.Intercept = None
        self.X_xtnt = None
        self.Y_xtnt = None
        self.Z_xtnt = None
        self.N_prtn = None
        self.Thickness = None
        self.Smoothing_width = None
        self.Periodic_region = None
        self._name = "AA_PLANAR"
        self._keywords = {'Phase': 'PHASE', 'Z_xtnt': 'Z_XTNT', 'X_xtnt': 'X_XTNT', 'Frequency': 'FREQUENCY', 'Intercept': 'INTERCEPT', 'Y_xtnt': 'Y_XTNT', 'Thickness': 'THICKNESS', 'Oscillating_fraction': 'OSCILLATING_FRACTION', 'V_d': 'V_D', 'N_prtn': 'N_PRTN', 'Parallel_plane': 'PARALLEL_PLANE', 'Periodic_region': 'PERIODIC_REGION', 'Smoothing_width': 'SMOOTHING_WIDTH'}
        self._aliases = {'Sigma': 'Smoothing_width'}


    @property
    def Sigma(self):
        """
        See documentation for Smoothing_width
        """
        return self.Smoothing_width

    @Sigma.setter
    def Sigma(self, value):
        self.Smoothing_width = value
