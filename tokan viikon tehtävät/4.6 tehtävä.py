import random
sisällä = 0
piste = 0
määrä = int(input("anna arvottavien pisteiden määrä"))
while piste <= määrä:
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
    if x^2+y^2<=1:
        sisällä += 1
    piste += 1
pi = 4* sisällä / määrä
print(f"Pii:n likiarvo on: {pi}")


