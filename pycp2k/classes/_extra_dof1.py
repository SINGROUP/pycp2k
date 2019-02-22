from pycp2k.inputsection import InputSection


class _extra_dof1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Default_keyword = None
        self._name = "EXTRA_DOF"
        self._default_keywords = {'Default_keyword': 'DEFAULT_KEYWORD'}
        self._attributes = ['Default_keyword']

