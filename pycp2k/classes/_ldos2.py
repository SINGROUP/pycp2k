from pycp2k.inputsection import InputSection


class _ldos2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Components = None
        self.List = []
        self._name = "LDOS"
        self._keywords = {'Components': 'COMPONENTS'}
        self._repeated_keywords = {'List': 'LIST'}

