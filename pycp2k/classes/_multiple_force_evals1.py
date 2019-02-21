from pycp2k.inputsection import InputSection


class _multiple_force_evals1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Force_eval_order = None
        self.Multiple_subsys = None
        self._name = "MULTIPLE_FORCE_EVALS"
        self._keywords = {'Multiple_subsys': 'MULTIPLE_SUBSYS', 'Force_eval_order': 'FORCE_EVAL_ORDER'}

