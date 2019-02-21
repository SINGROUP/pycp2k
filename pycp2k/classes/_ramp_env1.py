from pycp2k.inputsection import InputSection


class _ramp_env1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Start_step_in = None
        self.End_step_in = None
        self.Start_step_out = None
        self.End_step_out = None
        self._name = "RAMP_ENV"
        self._keywords = {'End_step_out': 'END_STEP_OUT', 'Start_step_out': 'START_STEP_OUT', 'Start_step_in': 'START_STEP_IN', 'End_step_in': 'END_STEP_IN'}

