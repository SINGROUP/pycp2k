from pycp2k.inputsection import InputSection


class _basis2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Default_keyword = []
        self._name = "BASIS"
        self._repeated_default_keywords = {'Default_keyword': 'DEFAULT_KEYWORD'}
        self._attributes = ['Section_parameters', 'Default_keyword']

