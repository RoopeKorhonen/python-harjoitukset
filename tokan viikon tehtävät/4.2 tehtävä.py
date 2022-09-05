# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
# niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa.
tuuma = 2.54
tuumienmäärä = int(input("tuumien määrä"))
while tuumienmäärä >= 0:
    print(tuuma*tuumienmäärä)
    tuumienmäärä = int(input("tuumien määrä"))
print("Ohjelma loppu")
    break