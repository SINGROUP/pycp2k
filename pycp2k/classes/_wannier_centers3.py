from pycp2k.inputsection import InputSection
from ._each205 import _each205


class _wannier_centers3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Unit = None
        self.Ionspluscenters = None
        self.Format = None
        self.Charge_occup = None
        self.Charge_beta = None
        self.Charge_extended = None
        self.EACH = _each205()
        self._name = "WANNIER_CENTERS"
        self._keywords = {'Charge_extended': 'CHARGE_EXTENDED', 'Ionspluscenters': 'IONS+CENTERS', 'Charge_occup': 'CHARGE_OCCUP', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Format': 'FORMAT', 'Filename': 'FILENAME', 'Charge_beta': 'CHARGE_BETA', 'Unit': 'UNIT'}
        self._subsections = {'EACH': 'EACH'}
        self._aliases = {'Charge_o': 'Charge_occup', 'Charge_b': 'Charge_beta'}
        self._attributes = ['Section_parameters']


    @property
    def Charge_o(self):
        """
        See documentation for Charge_occup
        """
        return self.Charge_occup

    @property
    def Charge_b(self):
        """
        See documentation for Charge_beta
        """
        return self.Charge_beta

    @Charge_o.setter
    def Charge_o(self, value):
        self.Charge_occup = value

    @Charge_b.setter
    def Charge_b(self, value):
        self.Charge_beta = value
