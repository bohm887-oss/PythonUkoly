import random
tajne_cislo=random.randint(1, 10)
pokusy=0

tip=0
while tip!=tajne_cislo and pokusy<5:
    
    tip=int(input("Tipni si cislo od 1 do 10: "))
    pokusy+=1
    if tip<tajne_cislo:
        print("Tvoje cislo je mensi nez tajne cislo")
    elif tip>tajne_cislo:
        print("Tvoje cislo je vetsi nez tajne cislo")
    else:
        print("Uhadl jsi tajne cislo po", pokusy, "pokupech")

if pokusy==5 and tip!=tajne_cislo:
    print("Neuhadl jsi tajne cislo, bylo to", tajne_cislo)


