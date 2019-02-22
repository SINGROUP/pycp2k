from pycp2k.inputsection import InputSection
from ._training_set1 import _training_set1


class _machine_learning1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.Prior = None
        self.Descriptor = None
        self.Tolerance = None
        self.Gp_noise_var = None
        self.Gp_scale = None
        self.TRAINING_SET = _training_set1()
        self._name = "MACHINE_LEARNING"
        self._keywords = {'Descriptor': 'DESCRIPTOR', 'Method': 'METHOD', 'Gp_noise_var': 'GP_NOISE_VAR', 'Tolerance': 'TOLERANCE', 'Prior': 'PRIOR', 'Gp_scale': 'GP_SCALE'}
        self._subsections = {'TRAINING_SET': 'TRAINING_SET'}

