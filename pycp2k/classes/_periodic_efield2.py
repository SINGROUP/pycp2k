from pycp2k.inputsection import InputSection


class _periodic_efield2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Intensity = None
        self.Polarisation = None
        self.Displacement_field = None
        self.D_filter = None
        self._name = "PERIODIC_EFIELD"
        self._keywords = {'Polarisation': 'POLARISATION', 'Intensity': 'INTENSITY', 'D_filter': 'D_FILTER', 'Displacement_field': 'DISPLACEMENT_FIELD'}

