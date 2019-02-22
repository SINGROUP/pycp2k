from pycp2k.inputsection import InputSection


class _sphere_sampling1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.X_low = None
        self.X_hi = None
        self.Y_low = None
        self.Y_hi = None
        self.Z_low = None
        self.Z_hi = None
        self.Auto_vdw_radii_table = None
        self.Auto_rmax_scale = None
        self.Auto_rmin_scale = None
        self.Rmax = None
        self.Rmin = None
        self.Rmax_kind = []
        self.Rmin_kind = []
        self._name = "SPHERE_SAMPLING"
        self._keywords = {'Z_hi': 'Z_HI', 'Auto_rmin_scale': 'AUTO_RMIN_SCALE', 'X_hi': 'X_HI', 'Y_hi': 'Y_HI', 'Rmax': 'RMAX', 'Auto_vdw_radii_table': 'AUTO_VDW_RADII_TABLE', 'Auto_rmax_scale': 'AUTO_RMAX_SCALE', 'Z_low': 'Z_LOW', 'Y_low': 'Y_LOW', 'Rmin': 'RMIN', 'X_low': 'X_LOW'}
        self._repeated_keywords = {'Rmax_kind': 'RMAX_KIND', 'Rmin_kind': 'RMIN_KIND'}

