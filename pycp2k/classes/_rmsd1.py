from pycp2k.inputsection import InputSection
from ._frame1 import _frame1


class _rmsd1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Subset_type = None
        self.Align_frames = None
        self.Atoms = []
        self.Weights = []
        self.FRAME_list = []
        self._name = "RMSD"
        self._keywords = {'Subset_type': 'SUBSET_TYPE', 'Align_frames': 'ALIGN_FRAMES'}
        self._repeated_keywords = {'Atoms': 'ATOMS', 'Weights': 'WEIGHTS'}
        self._repeated_subsections = {'FRAME': '_frame1'}
        self._attributes = ['FRAME_list']

    def FRAME_add(self, section_parameters=None):
        new_section = _frame1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FRAME_list.append(new_section)
        return new_section

