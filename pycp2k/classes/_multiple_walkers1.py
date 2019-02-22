from pycp2k.inputsection import InputSection
from ._walkers_file_name1 import _walkers_file_name1


class _multiple_walkers1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Walker_id = None
        self.Number_of_walkers = None
        self.Walker_comm_frequency = None
        self.Walkers_status = None
        self.WALKERS_FILE_NAME = _walkers_file_name1()
        self._name = "MULTIPLE_WALKERS"
        self._keywords = {'Walkers_status': 'WALKERS_STATUS', 'Walker_id': 'WALKER_ID', 'Number_of_walkers': 'NUMBER_OF_WALKERS', 'Walker_comm_frequency': 'WALKER_COMM_FREQUENCY'}
        self._subsections = {'WALKERS_FILE_NAME': 'WALKERS_FILE_NAME'}
        self._attributes = ['Section_parameters']

