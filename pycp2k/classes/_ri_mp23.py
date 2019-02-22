from pycp2k.inputsection import InputSection


class _ri_mp23(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Block_size = None
        self.Eps_canonical = None
        self.Free_hfx_buffer = None
        self._name = "RI_MP2"
        self._keywords = {'Block_size': 'BLOCK_SIZE', 'Free_hfx_buffer': 'FREE_HFX_BUFFER', 'Eps_canonical': 'EPS_CANONICAL'}
        self._aliases = {'Message_size': 'Block_size'}


    @property
    def Message_size(self):
        """
        See documentation for Block_size
        """
        return self.Block_size

    @Message_size.setter
    def Message_size(self, value):
        self.Block_size = value
