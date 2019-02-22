from pycp2k.inputsection import InputSection


class _constrain_exponents1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Scale = None
        self.Fermi_exp = None
        self._name = "CONSTRAIN_EXPONENTS"
        self._keywords = {'Scale': 'SCALE', 'Fermi_exp': 'FERMI_EXP'}

