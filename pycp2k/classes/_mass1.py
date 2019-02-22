from pycp2k.inputsection import InputSection


class _mass1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Default_keyword = None
        self._name = "MASS"
        self._default_keywords = {'Default_keyword': 'DEFAULT_KEYWORD'}
        self._attributes = ['Default_keyword']

