import math
#tiedot
L = float(input("anna luotien määrä "))
N = float(input("anna naulojen määrä"))
LE = float(input("anna leivisköjen määrä"))
luoti = 13.3
naula = 32 * luoti
leiviskä = 20 * naula

#laskutoimet

g = (luoti * L + naula * N + leiviskä * LE)
kg = g // 1000
g2 = g % 1000


# tulostus

print(f"leiviskät {LE}")
print(f"naulat {N}")
print(f"luodit {L}")

print(f"Massa nykymittojen mukaan: {kg:.0f} kilogrammaa ja {g2:.2f} grammaa")







