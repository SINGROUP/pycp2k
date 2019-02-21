from pycp2k.inputsection import InputSection


class _dummy_atoms1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Atoms = None
        self._name = "DUMMY_ATOMS"
        self._keywords = {'Atoms': 'ATOMS'}

