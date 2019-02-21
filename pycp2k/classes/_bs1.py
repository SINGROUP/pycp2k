from pycp2k.inputsection import InputSection
from ._alpha1 import _alpha1
from ._beta1 import _beta1


class _bs1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.ALPHA = _alpha1()
        self.BETA = _beta1()
        self._name = "BS"
        self._subsections = {'BETA': 'BETA', 'ALPHA': 'ALPHA'}
        self._attributes = ['Section_parameters']

