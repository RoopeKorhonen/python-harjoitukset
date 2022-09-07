x = [1, 6, 7, 8, 10]


def karsi_parittomat_luvut(lista):
    palautettava_lista = []
    for x in lista:
        if (x % 2) == 0:
            palautettava_lista.append(x)
    return palautettava_lista


muuttuja = karsi_parittomat_luvut(x)
print(x)
print(muuttuja)


