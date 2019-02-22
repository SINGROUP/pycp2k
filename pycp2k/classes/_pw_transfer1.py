from pycp2k.inputsection import InputSection


class _pw_transfer1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Grid = None
        self.N_loop = None
        self.Pw_grid = None
        self.Pw_grid_layout_all = None
        self.Debug = None
        self.Pw_grid_layout = None
        self.Pw_grid_blocked = None
        self._name = "PW_TRANSFER"
        self._keywords = {'Pw_grid_layout': 'PW_GRID_LAYOUT', 'N_loop': 'N_LOOP', 'Pw_grid': 'PW_GRID', 'Pw_grid_layout_all': 'PW_GRID_LAYOUT_ALL', 'Pw_grid_blocked': 'PW_GRID_BLOCKED', 'Grid': 'GRID', 'Debug': 'DEBUG'}

