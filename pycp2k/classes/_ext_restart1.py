from pycp2k.inputsection import InputSection


class _ext_restart1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Restart_file_name = None
        self.Binary_restart_file_name = None
        self.Restart_default = None
        self.Restart_counters = None
        self.Restart_pos = None
        self.Restart_vel = None
        self.Restart_randomg = None
        self.Restart_shell_pos = None
        self.Restart_core_pos = None
        self.Restart_optimize_input_variables = None
        self.Restart_shell_velocity = None
        self.Restart_core_velocity = None
        self.Restart_barostat = None
        self.Restart_barostat_thermostat = None
        self.Restart_shell_thermostat = None
        self.Restart_thermostat = None
        self.Restart_temperature_annealing = None
        self.Restart_cell = None
        self.Restart_metadynamics = None
        self.Restart_walkers = None
        self.Restart_band = None
        self.Restart_qmmm = None
        self.Restart_constraint = None
        self.Restart_bsse = None
        self.Restart_dimer = None
        self.Restart_averages = None
        self.Restart_rtp = None
        self.Custom_path = []
        self.Restart_pint_pos = None
        self.Restart_pint_vel = None
        self.Restart_pint_nose = None
        self.Restart_pint_gle = None
        self.Restart_helium_pos = None
        self.Restart_helium_permutation = None
        self.Restart_helium_force = None
        self.Restart_helium_rng = None
        self.Restart_helium_densities = None
        self.Restart_helium_averages = None
        self._name = "EXT_RESTART"
        self._keywords = {'Restart_helium_rng': 'RESTART_HELIUM_RNG', 'Restart_optimize_input_variables': 'RESTART_OPTIMIZE_INPUT_VARIABLES', 'Restart_file_name': 'RESTART_FILE_NAME', 'Restart_counters': 'RESTART_COUNTERS', 'Restart_helium_permutation': 'RESTART_HELIUM_PERMUTATION', 'Restart_constraint': 'RESTART_CONSTRAINT', 'Restart_pos': 'RESTART_POS', 'Restart_vel': 'RESTART_VEL', 'Restart_pint_nose': 'RESTART_PINT_NOSE', 'Restart_pint_vel': 'RESTART_PINT_VEL', 'Restart_randomg': 'RESTART_RANDOMG', 'Restart_shell_pos': 'RESTART_SHELL_POS', 'Restart_qmmm': 'RESTART_QMMM', 'Restart_default': 'RESTART_DEFAULT', 'Restart_helium_densities': 'RESTART_HELIUM_DENSITIES', 'Restart_averages': 'RESTART_AVERAGES', 'Restart_helium_pos': 'RESTART_HELIUM_POS', 'Restart_rtp': 'RESTART_RTP', 'Restart_metadynamics': 'RESTART_METADYNAMICS', 'Restart_walkers': 'RESTART_WALKERS', 'Restart_temperature_annealing': 'RESTART_TEMPERATURE_ANNEALING', 'Restart_band': 'RESTART_BAND', 'Restart_cell': 'RESTART_CELL', 'Restart_dimer': 'RESTART_DIMER', 'Restart_core_velocity': 'RESTART_CORE_VELOCITY', 'Restart_shell_velocity': 'RESTART_SHELL_VELOCITY', 'Restart_bsse': 'RESTART_BSSE', 'Restart_core_pos': 'RESTART_CORE_POS', 'Restart_pint_gle': 'RESTART_PINT_GLE', 'Restart_barostat_thermostat': 'RESTART_BAROSTAT_THERMOSTAT', 'Restart_pint_pos': 'RESTART_PINT_POS', 'Restart_shell_thermostat': 'RESTART_SHELL_THERMOSTAT', 'Binary_restart_file_name': 'BINARY_RESTART_FILE_NAME', 'Restart_helium_force': 'RESTART_HELIUM_FORCE', 'Restart_helium_averages': 'RESTART_HELIUM_AVERAGES', 'Restart_barostat': 'RESTART_BAROSTAT', 'Restart_thermostat': 'RESTART_THERMOSTAT'}
        self._repeated_keywords = {'Custom_path': 'CUSTOM_PATH'}
        self._aliases = {'Binary_restart_file': 'Binary_restart_file_name', 'External_file': 'Restart_file_name'}


    @property
    def External_file(self):
        """
        See documentation for Restart_file_name
        """
        return self.Restart_file_name

    @property
    def Binary_restart_file(self):
        """
        See documentation for Binary_restart_file_name
        """
        return self.Binary_restart_file_name

    @External_file.setter
    def External_file(self, value):
        self.Restart_file_name = value

    @Binary_restart_file.setter
    def Binary_restart_file(self, value):
        self.Binary_restart_file_name = value
