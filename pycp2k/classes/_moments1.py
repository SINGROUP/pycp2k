from pycp2k.inputsection import InputSection
from ._each256 import _each256


class _moments1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Periodic = None
        self.Reference = None
        self.Reference_point = None
        self.Max_moment = None
        self.Magnetic = None
        self.EACH = _each256()
        self._name = "MOMENTS"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Reference_point': 'REFERENCE_POINT', 'Periodic': 'PERIODIC', 'Filename': 'FILENAME', 'Reference': 'REFERENCE', 'Magnetic': 'MAGNETIC', 'Max_moment': 'MAX_MOMENT'}
        self._subsections = {'EACH': 'EACH'}
        self._aliases = {'Ref': 'Reference', 'Ref_point': 'Reference_point'}
        self._attributes = ['Section_parameters']


    @property
    def Ref(self):
        """
        See documentation for Reference
        """
        return self.Reference

    @property
    def Ref_point(self):
        """
        See documentation for Reference_point
        """
        return self.Reference_point

    @Ref.setter
    def Ref(self, value):
        self.Reference = value

    @Ref_point.setter
    def Ref_point(self, value):
        self.Reference_point = value
