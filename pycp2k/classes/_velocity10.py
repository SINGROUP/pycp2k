from pycp2k.inputsection import InputSection


class _velocity10(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Pint_unit = None
        self.Default_keyword = []
        self._name = "VELOCITY"
        self._keywords = {'Pint_unit': 'PINT_UNIT'}
        self._repeated_default_keywords = {'Default_keyword': 'DEFAULT_KEYWORD'}
        self._attributes = ['Default_keyword']

