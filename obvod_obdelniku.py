print("výpočet obvodu obdelníku")

a = input("zadejte proměnou a: ")
b = input("zadejte proměnou b: ")

a = int(a)
b = int(b)

if a>0 and b>0:
    vysledek = 2*a+2*b
    print("výsledek je: ", vysledek)
else:
    print("zkus to znova")
