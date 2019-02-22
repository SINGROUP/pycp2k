from pycp2k.inputsection import InputSection


class _hcth5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Parameter_set = None
        self._name = "HCTH"
        self._keywords = {'Parameter_set': 'PARAMETER_SET'}
        self._attributes = ['Section_parameters']

