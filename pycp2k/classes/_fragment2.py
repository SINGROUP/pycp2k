from pycp2k.inputsection import InputSection


class _fragment2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Map = None
        self.Default_keyword = None
        self._name = "FRAGMENT"
        self._keywords = {'Map': 'MAP'}
        self._default_keywords = {'Default_keyword': 'DEFAULT_KEYWORD'}
        self._attributes = ['Section_parameters', 'Default_keyword']

