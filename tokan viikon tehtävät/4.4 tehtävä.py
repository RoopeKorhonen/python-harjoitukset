import random
randomNumber = random.randint(1, 10)
userInput = int(input('Ohjelma on arponut luvun välillä 1-10, yritä arvata oikea luku: '))
while userInput != randomNumber:
    if userInput < randomNumber:
        print("Liian pieni arvaus")
    else:
        print("Liian suuri arvaus")
    userInput = int(input('Ohjelma on arponut luvun välillä 1-10, yritä arvata oikea luku: '))
print('Oikein.')



