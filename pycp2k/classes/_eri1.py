from pycp2k.inputsection import InputSection


class _eri1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.Operator = None
        self.Operator_parameter = None
        self.Periodicity = None
        self.Cutoff_radius = None
        self.Eps_integral = None
        self._name = "ERI"
        self._keywords = {'Method': 'METHOD', 'Operator_parameter': 'OPERATOR_PARAMETER', 'Periodicity': 'PERIODICITY', 'Cutoff_radius': 'CUTOFF_RADIUS', 'Operator': 'OPERATOR', 'Eps_integral': 'EPS_INTEGRAL'}

