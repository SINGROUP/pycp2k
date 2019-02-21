from pycp2k.inputsection import InputSection


class _ext_lagrange_ss01(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Default_keyword = []
        self._name = "EXT_LAGRANGE_SS0"
        self._repeated_default_keywords = {'Default_keyword': 'DEFAULT_KEYWORD'}
        self._attributes = ['Default_keyword']

