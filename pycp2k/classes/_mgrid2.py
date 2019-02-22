from pycp2k.inputsection import InputSection


class _mgrid2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Ngrids = None
        self.Cutoff = None
        self.Progression_factor = None
        self.Commensurate = None
        self.Realspace = None
        self.Rel_cutoff = None
        self.Multigrid_set = None
        self.Skip_load_balance_distributed = None
        self.Multigrid_cutoff = None
        self._name = "MGRID"
        self._keywords = {'Rel_cutoff': 'REL_CUTOFF', 'Commensurate': 'COMMENSURATE', 'Skip_load_balance_distributed': 'SKIP_LOAD_BALANCE_DISTRIBUTED', 'Multigrid_cutoff': 'MULTIGRID_CUTOFF', 'Realspace': 'REALSPACE', 'Ngrids': 'NGRIDS', 'Multigrid_set': 'MULTIGRID_SET', 'Progression_factor': 'PROGRESSION_FACTOR', 'Cutoff': 'CUTOFF'}
        self._aliases = {'Cutoff_list': 'Multigrid_cutoff', 'Relative_cutoff': 'Rel_cutoff'}


    @property
    def Relative_cutoff(self):
        """
        See documentation for Rel_cutoff
        """
        return self.Rel_cutoff

    @property
    def Cutoff_list(self):
        """
        See documentation for Multigrid_cutoff
        """
        return self.Multigrid_cutoff

    @Relative_cutoff.setter
    def Relative_cutoff(self, value):
        self.Rel_cutoff = value

    @Cutoff_list.setter
    def Cutoff_list(self, value):
        self.Multigrid_cutoff = value
