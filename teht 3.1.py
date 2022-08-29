# kahvin osot
# jos rahaa_taskussa>=5
# osta latte
# jos ei mutta rahaa taskussa >=3
# osta normi latte
# muuten
#  lähde pois

rahaa_taskussa = int(input("Paljon sinulla on rahaa? "))
maistuuko_kahvi = input("Maistuuko kahvi? ")
laten_hinta = 5
kahvin_hinta = 3
teen_hinta = 2

if laten_hinta <= rahaa_taskussa and maistuuko_kahvi == "joo":
    print("Ostan laten")
    print("juon laten")
    rahaa_taskussa = rahaa_taskussa - laten_hinta
elif rahaa_taskussa >= kahvin_hinta and maistuuko_kahvi == "joo":
    print("osta normikahvi")
    rahaa_taskussa = rahaa_taskussa - kahvin_hinta
elif rahaa_taskussa >= teen_hinta:
    print("otan teen")
    rahaa_taskussa = rahaa_taskussa - teen_hinta
else:
    print("Lähden kotiin")

if rahaa_taskussa == 0:
    print("Rahat loppu")
else:
    print(f"Sinulla on vielä {rahaa_taskussa} euroa taskussa.")