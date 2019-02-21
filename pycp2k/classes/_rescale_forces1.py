from pycp2k.inputsection import InputSection


class _rescale_forces1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_force = None
        self._name = "RESCALE_FORCES"
        self._keywords = {'Max_force': 'MAX_FORCE'}

