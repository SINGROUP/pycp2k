from pycp2k.inputsection import InputSection
from ._avbmc1 import _avbmc1
from ._move_probabilities1 import _move_probabilities1
from ._move_updates1 import _move_updates1
from ._max_displacements1 import _max_displacements1


class _mc1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Nstep = None
        self.Iprint = None
        self.Nmoves = None
        self.Nswapmoves = None
        self.Lbias = None
        self.Lstop = None
        self.Ldiscrete = None
        self.Rclus = None
        self.Restart = None
        self.Nvirial = None
        self.Ensemble = None
        self.Restart_file_name = None
        self.Moves_file_name = None
        self.Molecules_file_name = None
        self.Coordinate_file_name = None
        self.Energy_file_name = None
        self.Data_file_name = None
        self.Cell_file_name = None
        self.Max_disp_file_name = None
        self.Box2_file_name = None
        self.Pressure = None
        self.Temperature = None
        self.Virial_temps = None
        self.Discrete_step = None
        self.Eta = None
        self.Randomtoskip = None
        self.AVBMC = _avbmc1()
        self.MOVE_PROBABILITIES = _move_probabilities1()
        self.MOVE_UPDATES = _move_updates1()
        self.MAX_DISPLACEMENTS = _max_displacements1()
        self._name = "MC"
        self._keywords = {'Coordinate_file_name': 'COORDINATE_FILE_NAME', 'Cell_file_name': 'CELL_FILE_NAME', 'Restart_file_name': 'RESTART_FILE_NAME', 'Rclus': 'RCLUS', 'Lstop': 'LSTOP', 'Nvirial': 'NVIRIAL', 'Temperature': 'TEMPERATURE', 'Pressure': 'PRESSURE', 'Iprint': 'IPRINT', 'Discrete_step': 'DISCRETE_STEP', 'Data_file_name': 'DATA_FILE_NAME', 'Nstep': 'NSTEP', 'Nswapmoves': 'NSWAPMOVES', 'Moves_file_name': 'MOVES_FILE_NAME', 'Lbias': 'LBIAS', 'Virial_temps': 'VIRIAL_TEMPS', 'Energy_file_name': 'ENERGY_FILE_NAME', 'Nmoves': 'NMOVES', 'Randomtoskip': 'RANDOMTOSKIP', 'Max_disp_file_name': 'MAX_DISP_FILE_NAME', 'Box2_file_name': 'BOX2_FILE_NAME', 'Eta': 'ETA', 'Restart': 'RESTART', 'Ensemble': 'ENSEMBLE', 'Molecules_file_name': 'MOLECULES_FILE_NAME', 'Ldiscrete': 'LDISCRETE'}
        self._subsections = {'AVBMC': 'AVBMC', 'MOVE_UPDATES': 'MOVE_UPDATES', 'MOVE_PROBABILITIES': 'MOVE_PROBABILITIES', 'MAX_DISPLACEMENTS': 'MAX_DISPLACEMENTS'}

