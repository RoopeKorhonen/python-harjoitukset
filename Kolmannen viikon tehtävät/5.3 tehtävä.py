kokonaisluku = int(input("Anna kokonaisluku"))
jako = 2
while jako < kokonaisluku:
    if kokonaisluku % jako == 0:
        print("Ei ole alkuluku")
        break
    jako += 1
else:
    print("Kokonaisluku on alkuluku")


