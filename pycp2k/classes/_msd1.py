from pycp2k.inputsection import InputSection
from ._define_region5 import _define_region5


class _msd1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Ref0_filename = None
        self.Msd_per_kind = None
        self.Msd_per_molkind = None
        self.Msd_per_region = None
        self.Displaced_atom = None
        self.Displacement_tol = None
        self.DEFINE_REGION_list = []
        self._name = "MSD"
        self._keywords = {'Displacement_tol': 'DISPLACEMENT_TOL', 'Displaced_atom': 'DISPLACED_ATOM', 'Ref0_filename': 'REF0_FILENAME', 'Msd_per_kind': 'MSD_PER_KIND', 'Msd_per_region': 'MSD_PER_REGION', 'Msd_per_molkind': 'MSD_PER_MOLKIND'}
        self._repeated_subsections = {'DEFINE_REGION': '_define_region5'}
        self._attributes = ['Section_parameters', 'DEFINE_REGION_list']

    def DEFINE_REGION_add(self, section_parameters=None):
        new_section = _define_region5()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.DEFINE_REGION_list.append(new_section)
        return new_section

