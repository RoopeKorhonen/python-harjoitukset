#kysytään tiedot

kanta = float(input("kerro suorakulmion kanta "))

korkeus = float(input("kerro suorakulmion korkeus "))

#laskutoimitukset

A = kanta * korkeus
piiri = (kanta * 2) + (korkeus * 2)

#tulostukset
print(f"ala  ={A}")
print(f"piiri ={piiri}")


