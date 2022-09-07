import random
def noppa():
    numero = random.randint(1,6)
    return numero

while True:
    silmälukumuuttuja = noppa()
    print(silmälukumuuttuja)
    if silmälukumuuttuja == 6:
        break


