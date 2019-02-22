from pycp2k.inputsection import InputSection


class _fragment1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Default_keyword = []
        self._name = "FRAGMENT"
        self._repeated_default_keywords = {'Default_keyword': 'DEFAULT_KEYWORD'}
        self._attributes = ['Section_parameters', 'Default_keyword']

