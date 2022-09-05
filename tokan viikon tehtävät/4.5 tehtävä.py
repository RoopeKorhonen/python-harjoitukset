käyttäjätunnus = "python"
salasana = "rules"
index = 0
kirjautuminen = False

userNameInput = input('Anna Käyttäjätunnus: ')
passwordInput = input('Anna salasana: ')
index += 1
if userNameInput == käyttäjätunnus and passwordInput == salasana :
    kirjautuminen = True

    while kirjautuminen == False and index < 5:
        käyttäjätunnus = input('Anna käyttäjätunnus ')
        salasana = input('Anna salasana: ')
        index += 1
        if käyttäjätunnus == python and salasana == rules:
            kirjautuminen = True
    if kirjautuminen == True:
        print("tervetuloa")
    else:
        print("pääsy evätty")





