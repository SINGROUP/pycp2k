from pycp2k.inputsection import InputSection


class _worm1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Centroid_move_drmax = None
        self.Centroid_move_freq = None
        self.Staging_move_l = None
        self.Staging_move_rep = None
        self.Open_close_move_c = None
        self.Open_close_move_lmax = None
        self.Head_tail_move_lmax = None
        self.Swap_move_lmax = None
        self.G_sector_move_rep = None
        self.G_sector_move = None
        self.Write = None
        self.Atom = []
        self.Coord = []
        self._name = "WORM"
        self._keywords = {'Centroid_move_freq': 'CENTROID_MOVE_FREQ', 'Open_close_move_lmax': 'OPEN_CLOSE_MOVE_LMAX', 'G_sector_move_rep': 'G-SECTOR_MOVE_REP', 'Staging_move_rep': 'STAGING_MOVE_REP', 'Write': 'WRITE', 'Staging_move_l': 'STAGING_MOVE_L', 'Swap_move_lmax': 'SWAP_MOVE_LMAX', 'Open_close_move_c': 'OPEN_CLOSE_MOVE_C', 'Centroid_move_drmax': 'CENTROID_MOVE_DRMAX', 'Head_tail_move_lmax': 'HEAD_TAIL_MOVE_LMAX', 'G_sector_move': 'G-SECTOR_MOVE'}
        self._repeated_keywords = {'Atom': 'ATOM', 'Coord': 'COORD'}

