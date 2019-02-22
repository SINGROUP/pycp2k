from pycp2k.inputsection import InputSection


class _dipole_moments1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Dipole_form = None
        self.Reference = None
        self.Reference_point = None
        self._name = "DIPOLE_MOMENTS"
        self._keywords = {'Reference': 'REFERENCE', 'Dipole_form': 'DIPOLE_FORM', 'Reference_point': 'REFERENCE_POINT'}

