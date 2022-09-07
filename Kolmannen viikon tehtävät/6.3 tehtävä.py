def muutos(gallonit):
    gallon = 3.78541178
    litrat = gallonit * gallon
    return litrat

gallons = 0

while gallons >= 0:
    gallons = float(input("Anna gallonejen määrä"))
    muutos(gallons)
    litrat = muutos(gallons)
    print(litrat)