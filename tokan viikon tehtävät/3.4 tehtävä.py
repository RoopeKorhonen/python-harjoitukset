
vuosiluku = int(input("Kerro vuosiluku "))
if vuosiluku % 4 == 0:
    if vuosiluku % 100==0 and vuosiluku % 400 == 0:
        print("vuosi on karkausvuosi")
else:
    print("vuosi ei ole karkausvuosi")
