import os
import random
import threading
import time
from porti.PortiSeparate import Hangar, domGate, intGate
from GUI.window import Visual

# region Setare
listaAvioane = []
listaObiecte = []
portiDomestice = []
procese = []
x = 0
for i in range(3):
    portiDomestice.append(domGate(i+1))
    x = x+1

portiInternationale = []

portiInternationale.append(intGate(x+1))
x += 1
hangare = []
hangare.append(Hangar(x+1))
piste = [True, True]
# endregion Setare


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def aterizeaza(piste: list) -> None:
    piste_disponibile = [i for i in range(len(piste)) if piste[i] is True]
    if len(piste_disponibile) > 0:
        pista = piste_disponibile[0]
        piste[pista] = False
        obj.listaElPiste[pista].changeRED()
        print("S-a ocupat pista... se asteapta deblocarea...\n")
        time.sleep(3)
        piste[pista] = True
        obj.listaElPiste[pista].changeGREEN()
        print("Pista deblocata...")
        print("Avion aterizat!\n")
    else:
        time.sleep(6)
        aterizeaza(piste)


def decoleaza(portiDomestice: list) -> None:

    counter1 = 0
    for poarta in portiDomestice:
        if poarta.Ocupat is True:
            counter1 += 1
    cate1 = random.randint(1, counter1)
    print(f"Se elibereaza {cate1} porti...")
    time.sleep(3)

    for i in range(cate1):
        porti_de_eliberat = [i for i in range(
            len(portiDomestice)) if portiDomestice[i].Ocupat is True]
        if len(porti_de_eliberat) > 0:
            if len(porti_de_eliberat) == 1:
                obj.listaElPiste[0].changeRED()
                time.sleep(2)
                obj.listaElPiste[0].changeGREEN()
            elif len(porti_de_eliberat) == 2:
                obj.listaElPiste[0].changeRED()
                obj.listaElPiste[1].changeRED()
                time.sleep(2)
                obj.listaElPiste[0].changeGREEN()
                obj.listaElPiste[1].changeGREEN()
            # elif len(porti_de_eliberat) == 3:
            #     obj.listaElPiste[0].changeRED()
            #     obj.listaElPiste[1].changeRED()
            #     time.sleep(2)
            #     obj.listaElPiste[0].changeGREEN()
            #     obj.listaElPiste[1].changeGREEN()
            #     time.sleep(1)
            #     obj.listaElPiste[0].changeRED()
            #     time.sleep(2)
            #     obj.listaElPiste[0].changeGREEN()

            portiDomestice[porti_de_eliberat[0]].Ocupat = None
            obj.listaElPorti[porti_de_eliberat[0]].changeGREEN()
            print(f"Poarta {i+1} eliberata.")


def autoCreate(portiDomestice: list, piste: list, procese: list) -> None:

    pp = 0
    cate = random.randint(1, 5)
    print(f"{cate} avioane detectate pentru aterizare...")
    time.sleep(3)
    counter = 0
    for poarta in portiDomestice:
        if poarta.Ocupat is None:
            counter += 1

    if cate > counter:
        print(
            f"{cate-counter} avioane nu au loc de parcare pentru a ateriza... Restul incep aterizarea")
        time.sleep(3)
        for i in range(counter):
            obj.listaElButon[0].changeRED()
            thread = threading.Thread(target=aterizeaza, args=(piste,))
            procese.append(thread)
            thread.start()
    else:
        print("\nToate avioanele au loc de parcare. Se incepe aterizarea...")

        time.sleep(3)
        for i in range(cate):
            thread = threading.Thread(target=aterizeaza, args=(piste,))
            thread.start()
            procese.append(thread)
    for proces in procese:
        for index, poarta in enumerate(portiDomestice):
            if poarta.Ocupat is None:
                if index == 2:
                    time.sleep(3)
                poarta.Ocupat = True
                if len(procese) > 1 and pp == 0:
                    obj.listaElPorti[index+1].changeRED()
                    pp = 1
                obj.listaElPorti[index].changeRED()
                proces.join()
                break
    proces.join()
    print("Toate avioanele au aterizat!")
    obj.listaElButon[0].changeGREEN()
    print("Asteapta 3 secunde...")
    procese.clear()
    time.sleep(3)


def main():
    while True:

        clear_console()
        obj.listaElButon[0].changeRED()
        autoCreate(portiDomestice, piste, procese)
        obj.listaElButon[0].changeGREEN()
        print("\nDecolarea se incepe in 5 secunde: ")
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        obj.listaElButon[1].changeRED()
        decoleaza(portiDomestice)
        obj.listaElButon[1].changeGREEN()
        time.sleep(6)


if __name__ == "__main__":

    obj = Visual()
    console_thread = threading.Thread(target=main)
    pygame_thread = threading.Thread(target=obj.run)

    console_thread.start()
    pygame_thread.start()

    console_thread.join()
    pygame_thread.join()
