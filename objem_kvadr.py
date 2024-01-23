print("výpočet objemu kvadru")

a = input("zadej proměnou a: ")
b = input("zadej proměnou b: ")
c = input("zadej proměnou c: ")

a = int(a)
b = int(b)
c = int(c)

if a>0 and b>0 and c>0:
    vysledek = a*b*c
    print("vysledek je: ", vysledek)
else:
    print("zkus to znovu")