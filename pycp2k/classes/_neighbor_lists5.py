from pycp2k.inputsection import InputSection


class _neighbor_lists5(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Verlet_skin = None
        self.Neighbor_lists_from_scratch = None
        self.Geo_check = None
        self._name = "NEIGHBOR_LISTS"
        self._keywords = {'Geo_check': 'GEO_CHECK', 'Verlet_skin': 'VERLET_SKIN', 'Neighbor_lists_from_scratch': 'NEIGHBOR_LISTS_FROM_SCRATCH'}

