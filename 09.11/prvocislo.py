print ("test prvočisla")
cislo = int(input ("Zadej číslo: "))

je_prvocislo = True
if cislo < 2:
    je_prvocislo = False
elif cislo %  2 ==0:
    je_prvocislo = False
else:
    delitel = 3
    while delitel < cislo:
        if cislo % delitel == 0:
            je_prvocislo = False
            break
        delitel += 2
