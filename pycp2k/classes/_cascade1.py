from pycp2k.inputsection import InputSection
from ._atom_list1 import _atom_list1


class _cascade1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Energy = None
        self.ATOM_LIST = _atom_list1()
        self._name = "CASCADE"
        self._keywords = {'Energy': 'ENERGY'}
        self._subsections = {'ATOM_LIST': 'ATOM_LIST'}
        self._attributes = ['Section_parameters']

