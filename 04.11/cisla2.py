print("----------------------------------------------------------------------------------")

print("Mysli si číslo od 1 do 100. Já se ho pokusím uhodnout.")
print("Odpovídej následovně:")
print("  v - pokud je tvé číslo VĚTŠÍ")
print("  m - pokud je tvé číslo MENŠÍ")
print("  s - pokud je tip SPRÁVNĚ")

dole = 1
nahore = 100
pokusy = 0
odpoved = ""

while odpoved != "s":
    tip = (dole + nahore) // 2
    pokusy += 1
    
    print(f"Můj tip č. {pokusy} je: {tip}")
    odpoved = input("Tvá odpověď (v/m/s): ").strip().lower()
    
    if odpoved == "v":
        dole = tip + 1
    elif odpoved == "m":
        nahore = tip - 1
    elif odpoved == "s":
        print("Hurá, uhodl jsem to!")
    else:
        print("Neplatná odpověď. Zadej prosím 'v', 'm' nebo 's'.")
       

print(f"Celkový počet pokusů: {pokusy}")

print("----------------------------------------------------------------------------------")