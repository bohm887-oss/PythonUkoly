# kalkulačka spropitného
# 30.9/main.py
# ********************************

print("Vítejte v kalkulačce spropitného!")
print("-------------------------------------------------------------------------------")

celkova_cena = float(input("Zadejte celkovou cenu účtu: "))
spropitne = int(input("Zadejte procento spropitného: "))
POCET_LIDI = int(input("Zadejte počet lidí, kteří se dělí o účet: "))

# celkova_cena = celkova_cena + (celkova_cena * spropitne / 100)

celkova_cena += celkova_cena * spropitne / 100

cena_na_osobu = celkova_cena / POCET_LIDI
print(f"Cena na osobu: {cena_na_osobu:.2f} Kč")
celkova_cena = round(celkova_cena / POCET_LIDI + 0.5)
print(f"Cena na osobu (zaokrouhleno): {celkova_cena} Kč")

print("-------------------------------------------------------------------------------")

