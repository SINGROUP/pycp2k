from pycp2k.inputsection import InputSection
from ._each342 import _each342


class _topology_info1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Xtl_info = None
        self.Cif_info = None
        self.Pdb_info = None
        self.Xyz_info = None
        self.Psf_info = None
        self.Amber_info = None
        self.G96_info = None
        self.Crd_info = None
        self.Gtop_info = None
        self.Util_info = None
        self.Generate_info = None
        self.EACH = _each342()
        self._name = "TOPOLOGY_INFO"
        self._keywords = {'Cif_info': 'CIF_INFO', 'Xtl_info': 'XTL_INFO', 'Log_print_key': 'LOG_PRINT_KEY', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Pdb_info': 'PDB_INFO', 'Gtop_info': 'GTOP_INFO', 'Psf_info': 'PSF_INFO', 'Crd_info': 'CRD_INFO', 'Amber_info': 'AMBER_INFO', 'Xyz_info': 'XYZ_INFO', 'Filename': 'FILENAME', 'Util_info': 'UTIL_INFO', 'Generate_info': 'GENERATE_INFO', 'G96_info': 'G96_INFO'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

