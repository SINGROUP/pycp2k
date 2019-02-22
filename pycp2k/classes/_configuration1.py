from pycp2k.inputsection import InputSection


class _configuration1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Glb_conf = None
        self.Sub_conf = None
        self.Multiplicity = None
        self.Charge = None
        self._name = "CONFIGURATION"
        self._keywords = {'Glb_conf': 'GLB_CONF', 'Multiplicity': 'MULTIPLICITY', 'Sub_conf': 'SUB_CONF', 'Charge': 'CHARGE'}
        self._aliases = {'Multip': 'Multiplicity'}


    @property
    def Multip(self):
        """
        See documentation for Multiplicity
        """
        return self.Multiplicity

    @Multip.setter
    def Multip(self, value):
        self.Multiplicity = value
