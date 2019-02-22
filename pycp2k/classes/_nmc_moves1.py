from pycp2k.inputsection import InputSection
from ._move_type2 import _move_type2


class _nmc_moves1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nr_nmc_steps = None
        self.Nmc_file_name = None
        self.Prob = None
        self.Init_acc_prob = None
        self.MOVE_TYPE_list = []
        self._name = "NMC_MOVES"
        self._keywords = {'Nr_nmc_steps': 'NR_NMC_STEPS', 'Init_acc_prob': 'INIT_ACC_PROB', 'Nmc_file_name': 'NMC_FILE_NAME', 'Prob': 'PROB'}
        self._repeated_subsections = {'MOVE_TYPE': '_move_type2'}
        self._attributes = ['MOVE_TYPE_list']

    def MOVE_TYPE_add(self, section_parameters=None):
        new_section = _move_type2()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.MOVE_TYPE_list.append(new_section)
        return new_section

