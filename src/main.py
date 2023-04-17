import datetime

from main_auto import clear_console
from utility.Serializare import Serizalizare_v2
from avioane.TipAvion import AvionDomestic, AvionInternational
from porti.PortiSeparate import Hangar, domGate, intGate



# region Setare
listaAvioane = []
listaObiecte = []
portiDomestice = []
x = 0
for i in range(3):
    portiDomestice.append(domGate(i+1))
    x = x+1

portiInternationale = []

portiInternationale.append(intGate(x+1))
x += 1
hangare = []
hangare.append(Hangar(x+1))
# endregion Setare
print("MODIFICAT")

while True:
    clear_console()

    print("-"*50 + "\n")
    print("Selectati actiunea dorita:")
    print("\n")
    print("1 -> Inregistrare aterizare")
    print("2 -> Inregistrare plecare")
    print("3 -> Afisare avioane in aeroport")
    print("4 - > Trimite avion la hangarul de reparatii")
    print("0 -> Terminare program")
    x = input()
    #  region Aterizare
    if x == "1":
        while True:
            print("-"*50 + "\n")
            print("Selectati tipul zborului: 1-> Domestic    2 -> International")
            z = input()
            if z == "1":
                for poarta in portiDomestice:
                    if poarta.Ocupat is None:
                        print("-"*50 + "\n")
                        airplane = AvionDomestic()
                        poarta.parcare_avion(airplane)
                        airplane.Aterizare()
                        listaObiecte.append(airplane)
                        atribute = airplane.Transformare()
                        listaAvioane.append(atribute)
                        z = "000"
                        print("\n"+"S-a inregistrat! "+"\n")
                        input("Press Enter to cont1inue...")
                    break
                if z == "1":
                    print("Nu sunt porti disponibile pentru zboruri domestice...")
                    input("Press enter...")
                break
            if z == "2":
                for poarta in portiInternationale:
                    if poarta.Ocupat is None:
                        airplane = AvionInternational()
                        poarta.parcare_avion(airplane)
                        airplane.Aterizare()
                        listaObiecte.append(airplane)
                        atribute = airplane.Transformare()
                        listaAvioane.append(atribute)
                        z = "000"
                        print("\n"+"S-a inregistrat! "+"\n")
                        input("Press Enter to cont1inue...")
                        break
                if z == "2":
                    print("Poarta pentru zboruri internationale este ocupata...")
                    input("Enter...")
                break
    # endregion Aterizare
    # region Plecare
    if x == "2":
        if len(listaObiecte) == 0:
            print("Nu sunt avioane in aeroport...")
            input("Apasa enter pentru a continua.")

        else:
            print("Selectati aeronava care a parasit aeroportul:")
            i = 1
            for avion in listaObiecte:
                print(i, " -> " + avion.IdNum)
                i += 1
            while True:
                z = int(input())
                if int(z) <= len(listaObiecte) and z != 0:
                    ora_curenta = datetime.datetime.now().strftime("%H:%M:%S")
                    print("Aeronava cu numarul: ", listaObiecte[z-1].IdNum, " a parasit aeroportul la ora: ", ora_curenta)
                    for poarta in portiDomestice:
                        if poarta.Ocupat is not None and poarta.Ocupat.IdNum == listaObiecte[z-1].IdNum:
                            poarta.Ocupat = None
                            break
                    for poarta in portiInternationale:
                        if poarta.Ocupat is not None and poarta.Ocupat.IdNum == listaObiecte[z-1].IdNum:
                            poarta.Ocupat = None
                            break
                    for hangar in hangare:
                        if hangar.Ocupat is not None and hangar.Ocupat.IdNum == listaObiecte[z-1].IdNum:
                            if hangar.Ocupat.IdNum == listaObiecte[z-1].IdNum:
                                hangar.Ocupat = None
                            break
                    del listaObiecte[z-1]
                    del listaAvioane[z-1]
                    break

            print("Avioane ramase in aeroport: ")
            i = 1
            for avion in listaObiecte:
                print(i, " -> " + avion.IdNum)
                i += 1
            input("Apasa enter pentru a continua...")
    # endregion Plecare
    # region Avioare Avioane in Aeroport
    if x == "3":
        print("Ati selectat afisare avioane disponibile..")
        for dictionar in listaAvioane:
            print(dictionar)
            print("\n"*2)
        input("Enter...")
    # endregion Avioare Avioane in Aeroport
    # region La reparatii
    if x == "4":
        if hangare[0].Ocupat is not None:
            print("Hangarul este ocupat... Asteptati terminarea celui curent.")
            input("Apasa enter...")
        else:
            print("Selecteaza aeronava pe care vreti sa o trimiteti la hangar: ")
            i = 1
            for avion in listaObiecte:
                print(i, " -> " + avion.IdNum)
                i += 1
            while True:
                z = int(input())
                if int(z) <= len(listaObiecte) and z != 0:
                    ora_curenta = datetime.datetime.now().strftime("%H:%M:%S")
                    print("Aeronava cu numarul: ", listaObiecte[z-1].IdNum, " a fost trimisa in hangar  la ora: ", ora_curenta)
                    hangare[0].parcare_avion(listaObiecte[z-1])
                    input("Apasa enter...")
                    break
    # endregion La reparatii
    # region inchidere program
    if x == "0":
        while True:
            print("Ati selectat iesirea din program. Sunteti sigur (y/n):")
            x = str(input())
            if x == "y" or x == "Y":
                Serizalizare_v2(listaAvioane, "avion.pickle")
                exit(0)
            elif x == "n" or x == "N":
                break
    # endregion

