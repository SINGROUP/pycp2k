from pycp2k.inputsection import InputSection


class _restraint7(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Restraint_target = None
        self.Restraint_strength = None
        self._name = "RESTRAINT"
        self._keywords = {'Restraint_strength': 'RESTRAINT_STRENGTH', 'Restraint_target': 'RESTRAINT_TARGET'}

