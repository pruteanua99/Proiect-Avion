import os
import random
import threading
import time

from porti.PortiSeparate import Hangar, domGate, intGate


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
        print("S-a ocupat pista... se asteapta deblocarea...\n")
        time.sleep(3)
        piste[pista] = True
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
        porti_de_eliberat = [i for i in range(len(portiDomestice)) if portiDomestice[i].Ocupat is True]
        if len(porti_de_eliberat) > 0:
            portiDomestice[porti_de_eliberat[0]].Ocupat = None
            print(f"Poarta {i+1} eliberata.")


def autoCreate(portiDomestice: list, piste: list, procese: list) -> None:
    cate = random.randint(1, 6)
    print(f"{cate} avioane detectate pentru aterizare...")
    time.sleep(3)
    counter = 0
    for poarta in portiDomestice:
        if poarta.Ocupat is None:
            counter += 1

    if cate > counter:
        print(f"{cate-counter} avioane nu au loc de parcare pentru a ateriza... Restul incep aterizarea")
        time.sleep(3)
        for i in range(counter):
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
        for poarta in portiDomestice:
            if poarta.Ocupat is None:
                poarta.Ocupat = True
                proces.join()
                break
    proces.join()
    print("Toate avioanele au aterizat!")
    print("Asteapta 3 secunde...")
    procese.clear()
    time.sleep(3)


if __name__ == "__main__":
    while True:

        clear_console()
        autoCreate(portiDomestice, piste, procese)
        print("\nDecolarea se incepe in 5 secunde: ")
        for i in range(5, 0, -1):
            print(f"{i}...")
            time.sleep(1)

        decoleaza(portiDomestice)
        time.sleep(6)
