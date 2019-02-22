from pycp2k.inputsection import InputSection


class _aa_cylindrical2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.V_d = None
        self.Oscillating_fraction = None
        self.Frequency = None
        self.Phase = None
        self.Parallel_axis = None
        self.Xtnt = None
        self.Base_center = None
        self.Base_radius = None
        self.N_sides = None
        self.Apx_type = None
        self.N_prtn = None
        self.Thickness = None
        self.Smoothing_width = None
        self.Delta_alpha = None
        self._name = "AA_CYLINDRICAL"
        self._keywords = {'N_sides': 'N_SIDES', 'Xtnt': 'XTNT', 'Base_radius': 'BASE_RADIUS', 'Base_center': 'BASE_CENTER', 'Parallel_axis': 'PARALLEL_AXIS', 'Frequency': 'FREQUENCY', 'Apx_type': 'APX_TYPE', 'Phase': 'PHASE', 'Thickness': 'THICKNESS', 'V_d': 'V_D', 'N_prtn': 'N_PRTN', 'Delta_alpha': 'DELTA_ALPHA', 'Oscillating_fraction': 'OSCILLATING_FRACTION', 'Smoothing_width': 'SMOOTHING_WIDTH'}
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
