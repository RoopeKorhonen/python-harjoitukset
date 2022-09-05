lista = []
luku = None
while luku != "":
    luku = str(input("Anna luku tai lopeta painamalla Enter: "))
    if luku != "":
        lista.append(luku)
        res = [eval(i) for i in lista]
        if luku == "":
            break
res.sort(reverse=True)
f1 = res[0:5]
print(f"Suurimmat luvut ovat {f1}")




