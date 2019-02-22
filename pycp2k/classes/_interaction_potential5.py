from pycp2k.inputsection import InputSection


class _interaction_potential5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Potential_type = None
        self.Omega = None
        self.Scale_coulomb = None
        self.Scale_longrange = None
        self.Scale_gaussian = None
        self.Cutoff_radius = None
        self.T_c_g_data = None
        self._name = "INTERACTION_POTENTIAL"
        self._keywords = {'T_c_g_data': 'T_C_G_DATA', 'Omega': 'OMEGA', 'Scale_coulomb': 'SCALE_COULOMB', 'Scale_gaussian': 'SCALE_GAUSSIAN', 'Cutoff_radius': 'CUTOFF_RADIUS', 'Scale_longrange': 'SCALE_LONGRANGE', 'Potential_type': 'POTENTIAL_TYPE'}

