from pycp2k.inputsection import InputSection


class _move_type2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Section_parameters = None
        self.Size = None
        self.Prob = None
        self.Init_acc_prob = None
        self.Atoms = []
        self._name = "MOVE_TYPE"
        self._keywords = {'Prob': 'PROB', 'Init_acc_prob': 'INIT_ACC_PROB', 'Size': 'SIZE'}
        self._repeated_keywords = {'Atoms': 'ATOMS'}
        self._attributes = ['Section_parameters']

