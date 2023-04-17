

class locParcare():
    nrReferinta: int = None
    Ocupat: bool = None

    def __init__(self, i) -> None:
        self.nrReferinta = i
        self.Ocupat = None

    def parcare_avion(self, avion) -> None:
        if self.Ocupat is None:
            self.Ocupat = avion
            print(f"Avionul cu numarul {avion.IdNum} a fost parcat la  {self.nrReferinta}.")
        else:
            print(f"Poarta {self.nrReferinta} este ocupata.")

    def afisareDate(self) -> None:
        print("Numar identificare: ", self.nrReferinta)
        print("Statusul de dispoibilitate este: ", self.Ocupat)
