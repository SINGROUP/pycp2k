from pycp2k.inputsection import InputSection


class _siepmann1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self.B = None
        self.D = None
        self.E = None
        self.F = None
        self.Beta = None
        self.Rcut = None
        self.Allow_oh_formation = None
        self.Allow_h3o_formation = None
        self.Allow_o_formation = None
        self._name = "SIEPMANN"
        self._keywords = {'Allow_oh_formation': 'ALLOW_OH_FORMATION', 'Atoms': 'ATOMS', 'Allow_o_formation': 'ALLOW_O_FORMATION', 'Allow_h3o_formation': 'ALLOW_H3O_FORMATION', 'Rcut': 'RCUT', 'F': 'F', 'Beta': 'BETA', 'B': 'B', 'E': 'E', 'D': 'D'}

