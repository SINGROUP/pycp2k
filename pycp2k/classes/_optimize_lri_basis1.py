from pycp2k.inputsection import InputSection
from ._constrain_exponents1 import _constrain_exponents1


class _optimize_lri_basis1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Accuracy = None
        self.Max_fun = None
        self.Step_size = None
        self.Condition_weight = None
        self.Use_condition_number = None
        self.Geometric_sequence = None
        self.Degrees_of_freedom = None
        self.CONSTRAIN_EXPONENTS = _constrain_exponents1()
        self._name = "OPTIMIZE_LRI_BASIS"
        self._keywords = {'Use_condition_number': 'USE_CONDITION_NUMBER', 'Degrees_of_freedom': 'DEGREES_OF_FREEDOM', 'Accuracy': 'ACCURACY', 'Condition_weight': 'CONDITION_WEIGHT', 'Max_fun': 'MAX_FUN', 'Step_size': 'STEP_SIZE', 'Geometric_sequence': 'GEOMETRIC_SEQUENCE'}
        self._subsections = {'CONSTRAIN_EXPONENTS': 'CONSTRAIN_EXPONENTS'}

