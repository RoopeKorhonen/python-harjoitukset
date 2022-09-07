import random
def noppa(tahkot):
    numero = random.randint(1,tahkot)
    return numero

tahkotmäärä = int(input("Anna maksimi silmäluku"))
while True:
    silmälukumuuttuja = noppa(tahkotmäärä)
    print(silmälukumuuttuja)
    if silmälukumuuttuja == tahkotmäärä:
        break