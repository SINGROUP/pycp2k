from pycp2k.inputsection import InputSection


class _convergence_control2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Max_dr = None
        self.Max_force = None
        self.Rms_dr = None
        self.Rms_force = None
        self._name = "CONVERGENCE_CONTROL"
        self._keywords = {'Max_force': 'MAX_FORCE', 'Rms_dr': 'RMS_DR', 'Max_dr': 'MAX_DR', 'Rms_force': 'RMS_FORCE'}

