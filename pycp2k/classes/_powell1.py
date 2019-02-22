from pycp2k.inputsection import InputSection


class _powell1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Accuracy = None
        self.Step_size = None
        self.Max_fun = None
        self.Max_init = None
        self.Weight_pot_virtual = None
        self.Weight_pot_semicore = None
        self.Weight_pot_valence = None
        self.Weight_pot_node = None
        self.Weight_delta_energy = None
        self.Weight_electron_configuration = None
        self.Weight_method = None
        self.Target_pot_virtual = None
        self.Target_pot_valence = None
        self.Target_pot_semicore = None
        self.Target_delta_energy = None
        self.Target_psir0 = None
        self.Weight_psir0 = None
        self.Rcov_multiplication = None
        self.Semicore_level = None
        self._name = "POWELL"
        self._keywords = {'Max_init': 'MAX_INIT', 'Target_delta_energy': 'TARGET_DELTA_ENERGY', 'Accuracy': 'ACCURACY', 'Weight_psir0': 'WEIGHT_PSIR0', 'Weight_method': 'WEIGHT_METHOD', 'Target_psir0': 'TARGET_PSIR0', 'Target_pot_virtual': 'TARGET_POT_VIRTUAL', 'Weight_electron_configuration': 'WEIGHT_ELECTRON_CONFIGURATION', 'Weight_delta_energy': 'WEIGHT_DELTA_ENERGY', 'Step_size': 'STEP_SIZE', 'Target_pot_semicore': 'TARGET_POT_SEMICORE', 'Weight_pot_node': 'WEIGHT_POT_NODE', 'Semicore_level': 'SEMICORE_LEVEL', 'Target_pot_valence': 'TARGET_POT_VALENCE', 'Weight_pot_valence': 'WEIGHT_POT_VALENCE', 'Weight_pot_virtual': 'WEIGHT_POT_VIRTUAL', 'Max_fun': 'MAX_FUN', 'Weight_pot_semicore': 'WEIGHT_POT_SEMICORE', 'Rcov_multiplication': 'RCOV_MULTIPLICATION'}

