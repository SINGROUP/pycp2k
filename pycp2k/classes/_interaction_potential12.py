from pycp2k.inputsection import InputSection


class _interaction_potential12(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Potential_type = None
        self.Truncation_radius = None
        self.Tshpsc_data = None
        self._name = "INTERACTION_POTENTIAL"
        self._keywords = {'Truncation_radius': 'TRUNCATION_RADIUS', 'Tshpsc_data': 'TSHPSC_DATA', 'Potential_type': 'POTENTIAL_TYPE'}

