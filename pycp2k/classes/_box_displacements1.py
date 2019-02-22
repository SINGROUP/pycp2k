from pycp2k.inputsection import InputSection


class _box_displacements1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Rmvolume = None
        self.Rmcltrans = None
        self._name = "BOX_DISPLACEMENTS"
        self._keywords = {'Rmcltrans': 'RMCLTRANS', 'Rmvolume': 'RMVOLUME'}

