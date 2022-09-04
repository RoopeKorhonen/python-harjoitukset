lukuja = input("Anna lukuja")
alinluku = 0
ylinluku = 0
indexi = 0
while lukuja != "":

    number = int(lukuja)
    if alinluku == 0:
        if indexi == 0:
            alinluku = number

    if ylinluku == 0:
        ylinluku = number

    if number < alinluku:
        alinluku = number

    if number > ylinluku:
        ylinluku = number

    indexi += 1

    lukuja = input("Anna lukuja")
print("alinluku on" + str(alinluku))
print("ylinluku on" + str(ylinluku))