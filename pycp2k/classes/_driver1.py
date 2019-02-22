from pycp2k.inputsection import InputSection


class _driver1(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Unix = None
        self.Port = None
        self.Host = None
        self.Sleep_time = None
        self._name = "DRIVER"
        self._keywords = {'Host': 'HOST', 'Sleep_time': 'SLEEP_TIME', 'Port': 'PORT', 'Unix': 'UNIX'}

