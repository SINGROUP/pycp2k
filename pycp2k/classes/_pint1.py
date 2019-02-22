from pycp2k.inputsection import InputSection
from ._normalmode1 import _normalmode1
from ._staging1 import _staging1
from ._beads1 import _beads1
from ._nose6 import _nose6
from ._gle4 import _gle4
from ._pile1 import _pile1
from ._piglet1 import _piglet1
from ._init1 import _init1
from ._helium1 import _helium1
from ._print15 import _print15


class _pint1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.P = None
        self.Proc_per_replica = None
        self.Num_steps = None
        self.Max_step = None
        self.Iteration = None
        self.Temp = None
        self.T_tol = None
        self.Dt = None
        self.Harm_int = None
        self.Nrespa = None
        self.Transformation = None
        self.Propagator = None
        self.Fix_centroid_pos = None
        self.NORMALMODE = _normalmode1()
        self.STAGING = _staging1()
        self.BEADS = _beads1()
        self.NOSE = _nose6()
        self.GLE = _gle4()
        self.PILE = _pile1()
        self.PIGLET = _piglet1()
        self.INIT = _init1()
        self.HELIUM = _helium1()
        self.PRINT = _print15()
        self._name = "PINT"
        self._keywords = {'Fix_centroid_pos': 'FIX_CENTROID_POS', 'Propagator': 'PROPAGATOR', 'Nrespa': 'NRESPA', 'Harm_int': 'HARM_INT', 'Temp': 'TEMP', 'T_tol': 'T_TOL', 'Num_steps': 'NUM_STEPS', 'P': 'P', 'Max_step': 'MAX_STEP', 'Iteration': 'ITERATION', 'Transformation': 'TRANSFORMATION', 'Dt': 'DT', 'Proc_per_replica': 'PROC_PER_REPLICA'}
        self._subsections = {'PIGLET': 'PIGLET', 'NOSE': 'NOSE', 'GLE': 'GLE', 'HELIUM': 'HELIUM', 'PRINT': 'PRINT', 'STAGING': 'STAGING', 'BEADS': 'BEADS', 'INIT': 'INIT', 'PILE': 'PILE', 'NORMALMODE': 'NORMALMODE'}
        self._aliases = {'Temp_to': 'T_tol'}


    @property
    def Temp_to(self):
        """
        See documentation for T_tol
        """
        return self.T_tol

    @Temp_to.setter
    def Temp_to(self, value):
        self.T_tol = value
