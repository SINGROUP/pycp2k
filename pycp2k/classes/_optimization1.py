from pycp2k.inputsection import InputSection


class _optimization1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Accuracy = None
        self.Step_size = None
        self.Max_fun = None
        self._name = "OPTIMIZATION"
        self._keywords = {'Accuracy': 'ACCURACY', 'Max_fun': 'MAX_FUN', 'Step_size': 'STEP_SIZE'}

