from pycp2k.inputsection import InputSection


class _ci_neb1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nsteps_it = None
        self._name = "CI_NEB"
        self._keywords = {'Nsteps_it': 'NSTEPS_IT'}

