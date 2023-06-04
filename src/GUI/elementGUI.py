
class element:
    def __init__(self, pozitie_inaltime, pozitie_latime, lungime, latime, culoare):
        self.pozitie_inaltime = pozitie_inaltime
        self.pozitie_latime = pozitie_latime
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def changeRED(self):
        self.culoare = (255, 0, 0)

    def changeGREEN(self):
        self.culoare = (0, 255, 0)
