from pycp2k.inputsection import InputSection


class _acc1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Priority_buffers = None
        self.Posterior_buffers = None
        self.Priority_streams = None
        self.Posterior_streams = None
        self.Avoid_after_busy = None
        self.Min_flop_process = None
        self.Min_flop_sort = None
        self.Process_inhomogenous = None
        self.Binning_nbins = None
        self.Binning_binsize = None
        self._name = "ACC"
        self._keywords = {'Binning_nbins': 'BINNING_NBINS', 'Posterior_streams': 'POSTERIOR_STREAMS', 'Avoid_after_busy': 'AVOID_AFTER_BUSY', 'Binning_binsize': 'BINNING_BINSIZE', 'Priority_buffers': 'PRIORITY_BUFFERS', 'Posterior_buffers': 'POSTERIOR_BUFFERS', 'Process_inhomogenous': 'PROCESS_INHOMOGENOUS', 'Min_flop_sort': 'MIN_FLOP_SORT', 'Priority_streams': 'PRIORITY_STREAMS', 'Min_flop_process': 'MIN_FLOP_PROCESS'}

