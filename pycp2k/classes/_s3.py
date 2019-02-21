from pycp2k.inputsection import InputSection


class _s3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Default_keyword = None
        self._name = "S"
        self._default_keywords = {'Default_keyword': 'DEFAULT_KEYWORD'}
        self._attributes = ['Default_keyword']

