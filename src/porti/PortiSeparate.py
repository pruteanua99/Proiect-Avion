from .Aeroport import locParcare


class intGate(locParcare):

    def __init__(self, i) -> None:
        super().__init__(i)
        self.ceFelDePoarta = "International"


class domGate(locParcare):
    def __init__(self, i) -> None:
        super().__init__(i)
        self.ceFelDePoarta = "Domestic"


class Hangar(locParcare):

    def __init__(self, i) -> None:
        super().__init__(i)
        self.ceFelDePoarta = "Hangar"
