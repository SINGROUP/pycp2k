from pycp2k.inputsection import InputSection
from ._eri_mme5 import _eri_mme5


class _image_charge1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Mm_atom_list = []
        self.Width = None
        self.Ext_potential = None
        self.Determ_coeff = None
        self.Restart_image_matrix = None
        self.Image_restart_file_name = None
        self.Image_matrix_method = None
        self.ERI_MME = _eri_mme5()
        self._name = "IMAGE_CHARGE"
        self._keywords = {'Image_restart_file_name': 'IMAGE_RESTART_FILE_NAME', 'Ext_potential': 'EXT_POTENTIAL', 'Width': 'WIDTH', 'Determ_coeff': 'DETERM_COEFF', 'Restart_image_matrix': 'RESTART_IMAGE_MATRIX', 'Image_matrix_method': 'IMAGE_MATRIX_METHOD'}
        self._repeated_keywords = {'Mm_atom_list': 'MM_ATOM_LIST'}
        self._subsections = {'ERI_MME': 'ERI_MME'}

