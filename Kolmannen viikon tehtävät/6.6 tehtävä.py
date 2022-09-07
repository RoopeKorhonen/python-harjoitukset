import math;

def pizzahinta(halkaisija, hinta):
    r = (halkaisija / 100) / 2
    koko_neliöinä = math.pi * r ** 2
    return hinta / koko_neliöinä
koko = float(input("Anna ensimmäisen pizzan halkasia"))
hinta = float(input("Anna ensimmäisen pizzan hinta"))
pizza1 = pizzahinta(koko, hinta)

koko = float(input("Anna toisen pizzan halkasia"))
hinta = float(input("Anna toisen pizzan hinta"))
pizza2 = pizzahinta(koko, hinta)
if pizza1 > pizza2:
    print("pizza 2 on halvempi")
else:
    print("pizza 1 halvempi")





