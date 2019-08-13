import random


def generar_insulto(lista=[]):
    if not lista:
        f = open('insults', 'rt')
        for el in f:
            lista.append(el[:-1])

    return lista[random.randint(0, len(lista) - 1)], lista


if __name__ == '__main__':
    a, lista = generar_insulto()
    print(a)
