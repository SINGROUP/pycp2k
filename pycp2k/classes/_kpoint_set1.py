from pycp2k.inputsection import InputSection


class _kpoint_set1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Special_point = []
        self.Npoints = None
        self.Units = None
        self._name = "KPOINT_SET"
        self._keywords = {'Units': 'UNITS', 'Npoints': 'NPOINTS'}
        self._repeated_keywords = {'Special_point': 'SPECIAL_POINT'}

