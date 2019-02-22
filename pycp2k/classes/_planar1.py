from pycp2k.inputsection import InputSection


class _planar1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.V_d = None
        self.Oscillating_fraction = None
        self.Frequency = None
        self.Phase = None
        self.A = None
        self.B = None
        self.C = None
        self.N_prtn = None
        self.Thickness = None
        self.Smoothing_width = None
        self._name = "PLANAR"
        self._keywords = {'Frequency': 'FREQUENCY', 'V_d': 'V_D', 'N_prtn': 'N_PRTN', 'A': 'A', 'B': 'B', 'Oscillating_fraction': 'OSCILLATING_FRACTION', 'Smoothing_width': 'SMOOTHING_WIDTH', 'C': 'C', 'Phase': 'PHASE', 'Thickness': 'THICKNESS'}
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
