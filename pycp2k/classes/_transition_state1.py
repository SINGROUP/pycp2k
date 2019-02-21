from pycp2k.inputsection import InputSection
from ._dimer1 import _dimer1


class _transition_state1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.DIMER = _dimer1()
        self._name = "TRANSITION_STATE"
        self._keywords = {'Method': 'METHOD'}
        self._subsections = {'DIMER': 'DIMER'}

