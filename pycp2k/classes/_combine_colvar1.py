from pycp2k.inputsection import InputSection
from ._colvar4 import _colvar4


class _combine_colvar1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Function = None
        self.Variables = None
        self.Parameters = []
        self.Values = []
        self.Dx = None
        self.Error_limit = None
        self.COLVAR_list = []
        self._name = "COMBINE_COLVAR"
        self._keywords = {'Variables': 'VARIABLES', 'Error_limit': 'ERROR_LIMIT', 'Dx': 'DX', 'Function': 'FUNCTION'}
        self._repeated_keywords = {'Parameters': 'PARAMETERS', 'Values': 'VALUES'}
        self._repeated_subsections = {'COLVAR': '_colvar4'}
        self._attributes = ['COLVAR_list']

    def COLVAR_add(self, section_parameters=None):
        new_section = _colvar4()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.COLVAR_list.append(new_section)
        return new_section

