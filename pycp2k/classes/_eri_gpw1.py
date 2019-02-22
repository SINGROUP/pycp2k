from pycp2k.inputsection import InputSection


class _eri_gpw1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Eps_grid = None
        self.Cutoff = None
        self.Rel_cutoff = None
        self.Store_wfn = None
        self.Print_level = None
        self._name = "ERI_GPW"
        self._keywords = {'Eps_grid': 'EPS_GRID', 'Rel_cutoff': 'REL_CUTOFF', 'Cutoff': 'CUTOFF', 'Print_level': 'PRINT_LEVEL', 'Store_wfn': 'STORE_WFN'}
        self._aliases = {'Store_wavefunction': 'Store_wfn', 'Relative_cutoff': 'Rel_cutoff', 'Iolevel': 'Print_level'}


    @property
    def Relative_cutoff(self):
        """
        See documentation for Rel_cutoff
        """
        return self.Rel_cutoff

    @property
    def Store_wavefunction(self):
        """
        See documentation for Store_wfn
        """
        return self.Store_wfn

    @property
    def Iolevel(self):
        """
        See documentation for Print_level
        """
        return self.Print_level

    @Relative_cutoff.setter
    def Relative_cutoff(self, value):
        self.Rel_cutoff = value

    @Store_wavefunction.setter
    def Store_wavefunction(self, value):
        self.Store_wfn = value

    @Iolevel.setter
    def Iolevel(self, value):
        self.Print_level = value
