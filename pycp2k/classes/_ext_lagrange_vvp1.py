from pycp2k.inputsection import InputSection


class _ext_lagrange_vvp1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Default_keyword = []
        self._name = "EXT_LAGRANGE_VVP"
        self._repeated_default_keywords = {'Default_keyword': 'DEFAULT_KEYWORD'}
        self._attributes = ['Default_keyword']

