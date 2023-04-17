import pickle


def Serizalizare_v2(lista: list, cale: str) -> None:

    with open(cale, 'wb') as f:
        pickle.dump(lista, f)


def Deserializare(cale: str) -> list:
    with open(cale, 'rb')as f:
        lista = pickle.load(f)
    return lista
