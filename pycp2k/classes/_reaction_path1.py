from pycp2k.inputsection import InputSection
from ._colvar2 import _colvar2
from ._frame3 import _frame3
from ._map1 import _map1


class _reaction_path1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Distances_rmsd = None
        self.Rmsd = None
        self.Subset_type = None
        self.Align_frames = None
        self.Atoms = []
        self.Function = []
        self.Variable = None
        self.Lambda = None
        self.Step_size = None
        self.Range = None
        self.COLVAR_list = []
        self.FRAME_list = []
        self.MAP = _map1()
        self._name = "REACTION_PATH"
        self._keywords = {'Rmsd': 'RMSD', 'Range': 'RANGE', 'Step_size': 'STEP_SIZE', 'Variable': 'VARIABLE', 'Subset_type': 'SUBSET_TYPE', 'Align_frames': 'ALIGN_FRAMES', 'Distances_rmsd': 'DISTANCES_RMSD', 'Lambda': 'LAMBDA'}
        self._repeated_keywords = {'Atoms': 'ATOMS', 'Function': 'FUNCTION'}
        self._subsections = {'MAP': 'MAP'}
        self._repeated_subsections = {'FRAME': '_frame3', 'COLVAR': '_colvar2'}
        self._attributes = ['COLVAR_list', 'FRAME_list']

    def FRAME_add(self, section_parameters=None):
        new_section = _frame3()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.FRAME_list.append(new_section)
        return new_section

    def COLVAR_add(self, section_parameters=None):
        new_section = _colvar2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.COLVAR_list.append(new_section)
        return new_section

