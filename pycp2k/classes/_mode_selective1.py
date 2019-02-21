from pycp2k.inputsection import InputSection
from ._involved_atoms1 import _involved_atoms1
from ._print66 import _print66


class _mode_selective1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Frequency = None
        self.Range = None
        self.Lowest_frequency = None
        self.Atoms = None
        self.Eps_max_val = None
        self.Eps_norm = None
        self.Initial_guess = None
        self.Restart_file_name = None
        self.INVOLVED_ATOMS = _involved_atoms1()
        self.PRINT_list = []
        self._name = "MODE_SELECTIVE"
        self._keywords = {'Lowest_frequency': 'LOWEST_FREQUENCY', 'Atoms': 'ATOMS', 'Restart_file_name': 'RESTART_FILE_NAME', 'Initial_guess': 'INITIAL_GUESS', 'Frequency': 'FREQUENCY', 'Eps_norm': 'EPS_NORM', 'Eps_max_val': 'EPS_MAX_VAL', 'Range': 'RANGE'}
        self._subsections = {'INVOLVED_ATOMS': 'INVOLVED_ATOMS'}
        self._repeated_subsections = {'PRINT': '_print66'}
        self._attributes = ['PRINT_list']

    def PRINT_add(self, section_parameters=None):
        new_section = _print66()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.PRINT_list.append(new_section)
        return new_section

