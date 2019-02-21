from pycp2k.inputsection import InputSection
from ._worker_run_info1 import _worker_run_info1
from ._master_run_info1 import _master_run_info1
from ._communication_log1 import _communication_log1


class _print65(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.WORKER_RUN_INFO = _worker_run_info1()
        self.MASTER_RUN_INFO = _master_run_info1()
        self.COMMUNICATION_LOG = _communication_log1()
        self._name = "PRINT"
        self._subsections = {'MASTER_RUN_INFO': 'MASTER_RUN_INFO', 'WORKER_RUN_INFO': 'WORKER_RUN_INFO', 'COMMUNICATION_LOG': 'COMMUNICATION_LOG'}

