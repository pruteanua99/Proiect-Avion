from utility.Decorator import Cached
import datetime


class Avion ():

    IdNum: str
    Model: str
    sursa: str
    destinatia: str
    tip_zbor: str

    def __init__(self):
        print("Aeronava adaugata in sistem. Introduceti datele:")
        self.IdNum = input("Numar Identificare aeronava: ")
        self.Model = input("Model aeronava: ")
        self.sursa = input("Sursa:  ")
        

    def Aterizare(self):

        print("-"*50 + "\n")
        print("Motivul aterizarii: ")
        print("1->Destinatie")
        print("2->Escala")
        print("3->Urgenta")

        x = input()
        if x == "1":
            self.motiv = "Destinatie"

        if x == "2":
            self.motiv = "Escala"

        if x == "3":
            self.motiv = "Urgenta"
        #self.OraAterizare = input("\nOra aterizarii:")
        print("-"*50 + "\n")
        print("Pista folosita (1, 2): ")
        x = input()
        if x == "1":
            self.Pista = "1"
        if x == "2":
            self.Pista = "2"

    @Cached
    def Transformare(self):
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return [{"IdNum: ": self.IdNum}, {"Model: ": self.Model}, {"Sursa: ": self.sursa}, {"Destinatia: ": self.destinatia}, {"Motiv aterizare: ": self.motiv}, {"Pista folosita la aterizare: ": self.Pista}, {"Ora aterizare: ": current_time }]
    

   