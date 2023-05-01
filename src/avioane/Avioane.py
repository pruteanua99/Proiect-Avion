from utility.Decorator import Cached



class Avion ():

    IdNum: int
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
        self.OraAterizare = input("\nOra aterizarii:")
        print("-"*50 + "\n")
        print("Pista folosita (1, 2): ")
        x = input()
        if x == "1":
            self.Pista = "1"
        if x == "2":
            self.Pista = "2"

    @Cached
    def Transformare(self):
        return [{"IdNum: ": self.IdNum}, {"Model: ": self.Model}, {"Sursa: ": self.sursa}, {"Destinatia: ": self.destinatia}, {"Motiv aterizare: ": self.motiv}, {"Pista folosita la aterizare: ": self.Pista}, {"Ora aterizare: ": self.OraAterizare}]
    

    # def insertAvionBD(self):
    #     conexion = conexiune()
    #     conn=conexion.getConnection()
    #     cursor = conn.cursor()
    #     sql="SELECT Avion_NrIdentificare from avioane where Avion_NrIdentificare = ?"
    #     val = (self.IdNum,)
    #     cursor.execute(sql, val)
    #     rand = cursor.fetchone()    
    #     if rand is not None:
    #         return False  #s-a gasit avionul in bd
    #     else:
    #         sql="INSERT INTO avioane(Avion_NrIdentificare,Model) values (?, ?)"
    #         val = (self.IdNum, self.Model)
    #         cursor.execute(sql, val)
    #         conn.commit()
    #         return True #nu s-a gasit avionul in bd