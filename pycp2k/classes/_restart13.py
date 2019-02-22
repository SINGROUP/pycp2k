from pycp2k.inputsection import InputSection
from ._each396 import _each396


class _restart13(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Add_last = None
        self.Common_iteration_levels = None
        self.Filename = None
        self.Log_print_key = None
        self.Backup_copies = None
        self.EACH = _each396()
        self._name = "RESTART"
        self._keywords = {'Log_print_key': 'LOG_PRINT_KEY', 'Filename': 'FILENAME', 'Add_last': 'ADD_LAST', 'Common_iteration_levels': 'COMMON_ITERATION_LEVELS', 'Backup_copies': 'BACKUP_COPIES'}
        self._subsections = {'EACH': 'EACH'}
        self._attributes = ['Section_parameters']

