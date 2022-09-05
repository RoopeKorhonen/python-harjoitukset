import random
kuutioiden_määrä = int(input("Arpakuutioiden määrä"))
summa = 0
for x in range(kuutioiden_määrä):
    noppa = random.randint(1, 6)
    summa += noppa

print(summa)

