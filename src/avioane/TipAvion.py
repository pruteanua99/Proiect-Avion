from .Avioane import Avion


class AvionInternational (Avion):
    def __init__(self):
        super().__init__()
        self.destinatia = input("Destinatia: ")
        self.tip_zbor = "International"


class AvionDomestic (Avion):
    def __init__(self):
        super().__init__()
        self.destinatia = "Sprintvale"
        self.tip_zbor = "Domestic"


class intAvTest():
    
    def __init__(self):
        pass
