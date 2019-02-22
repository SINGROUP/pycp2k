from pycp2k.inputsection import InputSection
from ._rs_grid1 import _rs_grid1


class _rs_pw_transfer1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Grid = None
        self.Halo_size = None
        self.N_loop = None
        self.Rs2pw = None
        self.RS_GRID_list = []
        self._name = "RS_PW_TRANSFER"
        self._keywords = {'Rs2pw': 'RS2PW', 'Grid': 'GRID', 'N_loop': 'N_LOOP', 'Halo_size': 'HALO_SIZE'}
        self._repeated_subsections = {'RS_GRID': '_rs_grid1'}
        self._attributes = ['RS_GRID_list']

    def RS_GRID_add(self, section_parameters=None):
        new_section = _rs_grid1()
        if section_parameters is not None:
            if hasattr(new_section, 'Section_parameters'):
                new_section.Section_parameters = section_parameters
        self.RS_GRID_list.append(new_section)
        return new_section

