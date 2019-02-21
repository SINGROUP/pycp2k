from pycp2k.inputsection import InputSection


class _spawned_hills_height1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Default_keyword = []
        self._name = "SPAWNED_HILLS_HEIGHT"
        self._repeated_default_keywords = {'Default_keyword': 'DEFAULT_KEYWORD'}
        self._attributes = ['Default_keyword']

