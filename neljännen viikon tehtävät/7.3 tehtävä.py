lentoasemat = {}

def lentoasema():
    koodinlisäys=input("ICAO Koodi")
    nimenlisäys=input("Lentoaseman nimi")
    lentoasemat[koodinlisäys] = nimenlisäys

def kerroasema():
    kysyntä = input("Anna koodi: ")
    if kysyntä in lentoasemat:
        print(f"Lentoasema on {lentoasemat[kysyntä]}.")
    else:
        print("Ei ole lentoasemaa")


ensimmäinen = 1
print("1 - syötä uusi")
toinen = 2
print("2 - haku")
nolla = 0
print("0 - lopetus")
valinta = int(input("valitse"))
while valinta != nolla:
    if valinta == ensimmäinen:
        lentoasema()
    if valinta == toinen:
        kerroasema()
        if valinta == nolla:
            break
    valinta = int(input("valitse"))



