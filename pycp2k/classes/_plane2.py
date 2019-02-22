from pycp2k.inputsection import InputSection


class _plane2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Def_type = None
        self.Atoms = None
        self.Normal_vector = None
        self._name = "PLANE"
        self._keywords = {'Def_type': 'DEF_TYPE', 'Atoms': 'ATOMS', 'Normal_vector': 'NORMAL_VECTOR'}

