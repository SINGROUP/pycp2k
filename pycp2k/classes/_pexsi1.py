from pycp2k.inputsection import InputSection


class _pexsi1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Temperature = None
        self.Gap = None
        self.Num_pole = None
        self.Is_inertia_count = None
        self.Max_pexsi_iter = None
        self.Mu_min_0 = None
        self.Mu_max_0 = None
        self.Mu_inertia_tolerance = None
        self.Mu_inertia_expansion = None
        self.Mu_pexsi_safe_guard = None
        self.Num_electron_pexsi_tolerance = None
        self.Num_electron_initial_tolerance = None
        self.Ordering = None
        self.Row_ordering = None
        self.Np_symb_fact = None
        self.Verbosity = None
        self.Min_ranks_per_pole = None
        self.Csr_screening = None
        self._name = "PEXSI"
        self._keywords = {'Ordering': 'ORDERING', 'Mu_inertia_tolerance': 'MU_INERTIA_TOLERANCE', 'Gap': 'GAP', 'Num_pole': 'NUM_POLE', 'Mu_min_0': 'MU_MIN_0', 'Num_electron_initial_tolerance': 'NUM_ELECTRON_INITIAL_TOLERANCE', 'Row_ordering': 'ROW_ORDERING', 'Np_symb_fact': 'NP_SYMB_FACT', 'Max_pexsi_iter': 'MAX_PEXSI_ITER', 'Mu_inertia_expansion': 'MU_INERTIA_EXPANSION', 'Temperature': 'TEMPERATURE', 'Mu_pexsi_safe_guard': 'MU_PEXSI_SAFE_GUARD', 'Csr_screening': 'CSR_SCREENING', 'Verbosity': 'VERBOSITY', 'Mu_max_0': 'MU_MAX_0', 'Is_inertia_count': 'IS_INERTIA_COUNT', 'Num_electron_pexsi_tolerance': 'NUM_ELECTRON_PEXSI_TOLERANCE', 'Min_ranks_per_pole': 'MIN_RANKS_PER_POLE'}

