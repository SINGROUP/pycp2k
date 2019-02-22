from pycp2k.inputsection import InputSection


class _shell2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Core_charge = None
        self.Shell_charge = None
        self.Mass_fraction = None
        self.K2_spring = None
        self.K4_spring = None
        self.Max_distance = None
        self.Shell_cutoff = None
        self._name = "SHELL"
        self._keywords = {'K2_spring': 'K2_SPRING', 'Mass_fraction': 'MASS_FRACTION', 'K4_spring': 'K4_SPRING', 'Shell_charge': 'SHELL_CHARGE', 'Shell_cutoff': 'SHELL_CUTOFF', 'Max_distance': 'MAX_DISTANCE', 'Core_charge': 'CORE_CHARGE'}
        self._aliases = {'Core': 'Core_charge', 'Mass': 'Mass_fraction', 'Spring': 'K2_spring', 'Shell': 'Shell_charge', 'K2': 'K2_spring', 'K4': 'K4_spring'}
        self._attributes = ['Section_parameters']


    @property
    def Core(self):
        """
        See documentation for Core_charge
        """
        return self.Core_charge

    @property
    def Shell(self):
        """
        See documentation for Shell_charge
        """
        return self.Shell_charge

    @property
    def Mass(self):
        """
        See documentation for Mass_fraction
        """
        return self.Mass_fraction

    @property
    def K2(self):
        """
        See documentation for K2_spring
        """
        return self.K2_spring

    @property
    def Spring(self):
        """
        See documentation for K2_spring
        """
        return self.K2_spring

    @property
    def K4(self):
        """
        See documentation for K4_spring
        """
        return self.K4_spring

    @Core.setter
    def Core(self, value):
        self.Core_charge = value

    @Shell.setter
    def Shell(self, value):
        self.Shell_charge = value

    @Mass.setter
    def Mass(self, value):
        self.Mass_fraction = value

    @K2.setter
    def K2(self, value):
        self.K2_spring = value

    @Spring.setter
    def Spring(self, value):
        self.K2_spring = value

    @K4.setter
    def K4(self, value):
        self.K4_spring = value
