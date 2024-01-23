print("výpočet objemu obd")

a = input("zadej proměnou a: ")
b = input("zadej proměnou b: ")

a = int(a)
b = int(b)

if a>0 and b>0:
    vysledek = a*b
    print("vysledek je: ", vysledek)
else:
    print("zkus to znovu")
