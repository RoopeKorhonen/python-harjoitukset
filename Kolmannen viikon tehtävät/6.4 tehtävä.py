lista = []
lukujenmäärä = int(input("Montako kokonaislukua haluat summata"))
def kysynumerot(lukujenmäärät):

    for x in range(lukujenmäärät):
        luku = int(input("Anna luku "))
        lista.append(luku)


kysynumerot(lukujenmäärä)
yhteensä = sum(lista)
print(yhteensä)
