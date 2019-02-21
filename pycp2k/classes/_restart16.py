from pycp2k.inputsection import InputSection


class _restart16(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.File_restart = None
        self._name = "RESTART"
        self._keywords = {'File_restart': 'FILE_RESTART'}

