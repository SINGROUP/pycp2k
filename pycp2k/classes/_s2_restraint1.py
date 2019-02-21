from pycp2k.inputsection import InputSection


class _s2_restraint1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Strength = None
        self.Target = None
        self.Functional_form = None
        self._name = "S2_RESTRAINT"
        self._keywords = {'Functional_form': 'FUNCTIONAL_FORM', 'Strength': 'STRENGTH', 'Target': 'TARGET'}

