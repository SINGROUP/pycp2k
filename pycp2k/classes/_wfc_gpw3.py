from pycp2k.inputsection import InputSection


class _wfc_gpw3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_grid = None
        self.Eps_filter = None
        self.Cutoff = None
        self.Rel_cutoff = None
        self.Multipole_two_cent_int = None
        self.Print_level = None
        self.Eps_pgf_orb_s = None
        self.Do_cholesky_subgroups = None
        self.Size_cholesky_subgroup = None
        self._name = "WFC_GPW"
        self._keywords = {'Eps_filter': 'EPS_FILTER', 'Print_level': 'PRINT_LEVEL', 'Rel_cutoff': 'REL_CUTOFF', 'Eps_pgf_orb_s': 'EPS_PGF_ORB_S', 'Cutoff': 'CUTOFF', 'Eps_grid': 'EPS_GRID', 'Size_cholesky_subgroup': 'SIZE_CHOLESKY_SUBGROUP', 'Do_cholesky_subgroups': 'DO_CHOLESKY_SUBGROUPS', 'Multipole_two_cent_int': 'MULTIPOLE_TWO_CENT_INT'}
        self._aliases = {'Relative_cutoff': 'Rel_cutoff', 'Iolevel': 'Print_level', 'Size_cs': 'Size_cholesky_subgroup', 'Dcs': 'Do_cholesky_subgroups'}


    @property
    def Relative_cutoff(self):
        """
        See documentation for Rel_cutoff
        """
        return self.Rel_cutoff

    @property
    def Iolevel(self):
        """
        See documentation for Print_level
        """
        return self.Print_level

    @property
    def Dcs(self):
        """
        See documentation for Do_cholesky_subgroups
        """
        return self.Do_cholesky_subgroups

    @property
    def Size_cs(self):
        """
        See documentation for Size_cholesky_subgroup
        """
        return self.Size_cholesky_subgroup

    @Relative_cutoff.setter
    def Relative_cutoff(self, value):
        self.Rel_cutoff = value

    @Iolevel.setter
    def Iolevel(self, value):
        self.Print_level = value

    @Dcs.setter
    def Dcs(self, value):
        self.Do_cholesky_subgroups = value

    @Size_cs.setter
    def Size_cs(self, value):
        self.Size_cholesky_subgroup = value
