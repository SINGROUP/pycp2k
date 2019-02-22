from pycp2k.inputsection import InputSection


class _contact1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Bandwidth = None
        self.Start = None
        self.N_atoms = None
        self.Injection_sign = None
        self.Injecting_contact = None
        self._name = "CONTACT"
        self._keywords = {'Injection_sign': 'INJECTION_SIGN', 'Bandwidth': 'BANDWIDTH', 'N_atoms': 'N_ATOMS', 'Injecting_contact': 'INJECTING_CONTACT', 'Start': 'START'}

