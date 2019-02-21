from pycp2k.inputsection import InputSection
from ._kpoint_set1 import _kpoint_set1


class _band_structure1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.File_name = None
        self.Added_mos = None
        self.KPOINT_SET_list = []
        self._name = "BAND_STRUCTURE"
        self._keywords = {'File_name': 'FILE_NAME', 'Added_mos': 'ADDED_MOS'}
        self._repeated_subsections = {'KPOINT_SET': '_kpoint_set1'}
        self._aliases = {'Added_bands': 'Added_mos'}
        self._attributes = ['KPOINT_SET_list']

    def KPOINT_SET_add(self, section_parameters=None):
        new_section = _kpoint_set1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.KPOINT_SET_list.append(new_section)
        return new_section


    @property
    def Added_bands(self):
        """
        See documentation for Added_mos
        """
        return self.Added_mos

    @Added_bands.setter
    def Added_bands(self, value):
        self.Added_mos = value
