from pycp2k.inputsection import InputSection


class _involved_atoms1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Range = None
        self.Involved_atoms = None
        self._name = "INVOLVED_ATOMS"
        self._keywords = {'Involved_atoms': 'INVOLVED_ATOMS', 'Range': 'RANGE'}

