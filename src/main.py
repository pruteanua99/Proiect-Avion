import datetime
from pentruBD.forConnection import airportBD as airBD
from main_auto import clear_console
from utility.Serializare import Serizalizare_v2
from avioane.TipAvion import AvionDomestic, AvionInternational
from porti.PortiSeparate import Hangar, domGate, intGate
from GUI.window import Visual
import time

import threading


def main():
    # region Setare
    listaAvioane = []
    listaObiecte = []
    portiDomestice = []
    x = 0
    for i in range(3):
        portiDomestice.append(domGate(i+1))
        x = x+1
    portiInternationale = []
    airbdd = airBD()
    global z
    portiInternationale.append(intGate(x+1))
    x += 1
    hangare = []
    hangare.append(Hangar(x+1))

    # endregion Setare
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
                    for index, poarta in enumerate(portiDomestice):
                        if poarta.Ocupat is None:
                            obj.listaElButon[0].changeRED()

                            print("-"*50 + "\n")
                            airplane = AvionDomestic()
                            poarta.parcare_avion(airplane)
                            airplane.Aterizare()
                            listaObiecte.append(airplane)
                            atribute = airplane.Transformare()
                            listaAvioane.append(atribute)
                            airbdd.historyRegister(airplane, poarta)
                            if airplane.Pista == "1":
                                obj.listaElPiste[0].changeRED()
                            if airplane.Pista == "2":
                                obj.listaElPiste[1].changeRED()
                            time.sleep(2)
                            if airplane.Pista == "1":
                                obj.listaElPiste[0].changeGREEN()
                            if airplane.Pista == "2":
                                obj.listaElPiste[1].changeGREEN()
                            obj.listaElPorti[index].changeRED()
                            obj.listaElButon[0].changeGREEN()
                            obj.lista_ref_NO[index] = airplane.IdNum
                            z = "000"
                            print("\n"+"S-a inregistrat! "+"\n")
                            input("Press Enter to cont1inue...")
                            break
                    if z == "1":
                        print("Nu sunt porti disponibile pentru zboruri domestice...")
                        input("Press enter...")
                    break
                if z == "2":
                    for index, poarta in enumerate(portiInternationale):
                        if poarta.Ocupat is None:
                            obj.listaElButon[0].changeRED()
                            airplane = AvionInternational()
                            poarta.parcare_avion(airplane)
                            airplane.Aterizare()
                            listaObiecte.append(airplane)
                            atribute = airplane.Transformare()
                            listaAvioane.append(atribute)
                            airbdd.historyRegister(airplane, poarta)
                            if airplane.Pista == "1":
                                obj.listaElPiste[0].changeRED()
                            if airplane.Pista == "2":
                                obj.listaElPiste[1].changeRED()
                            time.sleep(2)
                            if airplane.Pista == "1":
                                obj.listaElPiste[0].changeGREEN()
                            if airplane.Pista == "2":
                                obj.listaElPiste[1].changeGREEN()
                            obj.listaElPorti[3].changeRED()
                            obj.listaElButon[0].changeGREEN()
                            obj.lista_ref_NO[3] = airplane.IdNum
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
                obj.listaElButon[1].changeRED()
                print("Selectati aeronava care a parasit aeroportul:")
                i = 1
                for avion in listaObiecte:
                    print(i, " -> " + avion.IdNum)
                    i += 1
                while True:
                    z = int(input())
                    if int(z) <= len(listaObiecte) and z != 0:
                        ora_curenta = datetime.datetime.now().strftime("%H:%M:%S")
                        print("Aeronava cu numarul: ",
                              listaObiecte[z-1].IdNum, " a parasit aeroportul la ora: ", ora_curenta)
                        for index, poarta in enumerate(portiDomestice):
                            if poarta.Ocupat is not None and poarta.Ocupat.IdNum == listaObiecte[z-1].IdNum:
                                obj.listaElPorti[index].changeGREEN()
                                obj.lista_ref_NO[index] = None
                                poarta.Ocupat = None
                                break
                        for poarta in portiInternationale:
                            if poarta.Ocupat is not None and poarta.Ocupat.IdNum == listaObiecte[z-1].IdNum:
                                obj.listaElPorti[3].changeGREEN()
                                obj.lista_ref_NO[3] = None
                                poarta.Ocupat = None
                                break
                        for hangar in hangare:
                            if hangar.Ocupat is not None and hangar.Ocupat.IdNum == listaObiecte[z-1].IdNum:
                                if hangar.Ocupat.IdNum == listaObiecte[z-1].IdNum:
                                    obj.listaElHangar[0].changeGREEN()
                                    obj.lista_ref_NO[4] = None
                                    hangar.Ocupat = None
                                break
                        airbdd.plecareAvion(listaObiecte[z-1])
                        del listaObiecte[z-1]
                        del listaAvioane[z-1]
                        break
                print("Avioane ramase in aeroport: ")
                i = 1
                for avion in listaObiecte:
                    print(i, " -> " + avion.IdNum)
                    i += 1
                obj.listaElButon[1].changeGREEN()
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
                        print("Aeronava cu numarul: ",
                              listaObiecte[z-1].IdNum, " a fost trimisa in hangar  la ora: ", ora_curenta)
                        hangare[0].parcare_avion(listaObiecte[z-1])
                        obj.listaElPorti[z - 1].changeGREEN()
                        obj.lista_ref_NO[4] = listaObiecte[z-1].IdNum
                        obj.listaElHangar[0].changeRED()
                        for index, poarta in enumerate(portiDomestice):
                            if poarta.Ocupat is not None and poarta.Ocupat.IdNum == listaObiecte[z-1].IdNum:
                                obj.listaElPorti[index].changeGREEN()
                                obj.lista_ref_NO[index] = None
                                poarta.Ocupat = None
                                break
                        for poarta in portiInternationale:
                            if poarta.Ocupat is not None and poarta.Ocupat.IdNum == listaObiecte[z-1].IdNum:
                                obj.listaElPorti[3].changeGREEN()
                                obj.lista_ref_NO[3] = None
                                poarta.Ocupat = None
                                break
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


if __name__ == "__main__":
    obj = Visual()
    console_thread = threading.Thread(target=main)
    pygame_thread = threading.Thread(target=obj.run)

    console_thread.start()
    pygame_thread.start()

    console_thread.join()
    pygame_thread.join()
