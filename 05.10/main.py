# cislo test 

print ("------------------------------------------------------------------------------")
       
cislo = int(input("Zadejte číslo: "))

if cislo > 0:
    print("kladné")
elif cislo < 0:
    print("záporné")
else: 
    print("nula")

if cislo <0:
    print("absolutní hodnota je: " + str(cislo * -1))
if cislo >0:
    print("absolutní hodnota je: " + str(cislo))

print ("------------------------------------------------------------------------------")
