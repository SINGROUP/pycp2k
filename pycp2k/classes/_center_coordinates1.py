from pycp2k.inputsection import InputSection


class _center_coordinates1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Center_point = None
        self._name = "CENTER_COORDINATES"
        self._keywords = {'Center_point': 'CENTER_POINT'}
        self._attributes = ['Section_parameters']

