from pycp2k.inputsection import InputSection


class _move_updates1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Iupvolume = None
        self.Iuptrans = None
        self.Iupcltrans = None
        self._name = "MOVE_UPDATES"
        self._keywords = {'Iupvolume': 'IUPVOLUME', 'Iuptrans': 'IUPTRANS', 'Iupcltrans': 'IUPCLTRANS'}

