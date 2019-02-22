from pycp2k.inputsection import InputSection
from ._print17 import _print17


class _mixed_cdft1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Lambda = None
        self.Force_states = None
        self.Coupling = None
        self.Dlb = None
        self.Metric = None
        self.Wfn_overlap = None
        self.Lowdin = None
        self.Ci = None
        self.Nonorthogonal_coupling = None
        self.Scale_with_occupation_numbers = None
        self.Wfn_restart_file_name = None
        self.Eps_svd = None
        self.Eps_occupied = None
        self.Load_scale = None
        self.More_work = None
        self.Very_overloaded = None
        self.PRINT = _print17()
        self._name = "MIXED_CDFT"
        self._keywords = {'Ci': 'CI', 'Coupling': 'COUPLING', 'Nonorthogonal_coupling': 'NONORTHOGONAL_COUPLING', 'Scale_with_occupation_numbers': 'SCALE_WITH_OCCUPATION_NUMBERS', 'Force_states': 'FORCE_STATES', 'Lowdin': 'LOWDIN', 'Eps_occupied': 'EPS_OCCUPIED', 'Load_scale': 'LOAD_SCALE', 'Wfn_overlap': 'WFN_OVERLAP', 'Very_overloaded': 'VERY_OVERLOADED', 'More_work': 'MORE_WORK', 'Dlb': 'DLB', 'Wfn_restart_file_name': 'WFN_RESTART_FILE_NAME', 'Lambda': 'LAMBDA', 'Metric': 'METRIC', 'Eps_svd': 'EPS_SVD'}
        self._subsections = {'PRINT': 'PRINT'}
        self._aliases = {'Configuration_interaction': 'Ci', 'Coupling_metric': 'Metric', 'Nonortho_coupling': 'Nonorthogonal_coupling'}


    @property
    def Coupling_metric(self):
        """
        See documentation for Metric
        """
        return self.Metric

    @property
    def Configuration_interaction(self):
        """
        See documentation for Ci
        """
        return self.Ci

    @property
    def Nonortho_coupling(self):
        """
        See documentation for Nonorthogonal_coupling
        """
        return self.Nonorthogonal_coupling

    @Coupling_metric.setter
    def Coupling_metric(self, value):
        self.Metric = value

    @Configuration_interaction.setter
    def Configuration_interaction(self, value):
        self.Ci = value

    @Nonortho_coupling.setter
    def Nonortho_coupling(self, value):
        self.Nonorthogonal_coupling = value
