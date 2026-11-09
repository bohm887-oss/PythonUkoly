import random


tajne_cislo = random.randint(1, 20)
pokusy = 0
max_pokusu = 5
tip = 0

print("Myslím si číslo od 1 do 20.")


while tip != tajne_cislo and pokusy < max_pokusu:
    
    tip = int(input("Tipni si číslo od 1 do 20: "))
    
   
    if tip < 1 or tip > 20:
        print("Zadal jsi číslo mimo rozsah (1–20)!")
        continue  # Přeskočí zbytek cyklu a nepočítá tento pokus
    
   
    pokusy += 1
    

    if tip < tajne_cislo:
        print("Moje číslo je VĚTŠÍ!")
    elif tip > tajne_cislo:
        print("Moje číslo je MENŠÍ!")
    else:
        print(f"Gratuluji! Uhodl jsi číslo {tajne_cislo} na {pokusy}. pokus.")


if pokusy == max_pokusu and tip != tajne_cislo:
    print(f"Bohužel ti došly pokusy! Tajné číslo bylo {tajne_cislo}.")