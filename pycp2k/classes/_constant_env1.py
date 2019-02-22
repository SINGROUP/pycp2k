from pycp2k.inputsection import InputSection


class _constant_env1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Start_step = None
        self.End_step = None
        self._name = "CONSTANT_ENV"
        self._keywords = {'End_step': 'END_STEP', 'Start_step': 'START_STEP'}

