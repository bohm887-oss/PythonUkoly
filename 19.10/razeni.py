def seradit_promenne():
    print("--- Program na řazení 4 proměnných ---")
    
    # 1. Postupné zadání 4 jednotlivých proměnných
    try:
        a = float(input("Zadej hodnotu a: "))
        b = float(input("Zadej hodnotu b: "))
        c = float(input("Zadej hodnotu c: "))
        d = float(input("Zadej hodnotu d: "))
    except ValueError:
        print("Chyba: Musíš zadat platná čísla.")
        return

    # 2. Výběr způsobu řazení
    print("\nVyber způsob řazení:")
    print("1 - Od nejmenšího do největšího")
    print("2 - Od největšího do nejmenšího")
    
    volba = input("Zadej svou volbu (1 nebo 2): ").strip()

    # 3. Ruční seřazení proměnných bez použití seznamů
    if volba == '1':
        # Vzestupné řazení (od nejmenšího)
        if a > b:
            q = a; a = b; b = q
        if b > c:
            q = b; b = c; c = q
        if c > d:
            q = c; c = d; d = q
            
        if a > b:
            q = a; a = b; b = q
        if b > c:
            q = b; b = c; c = q
            
        if a > b:
            q = a; a = b; b = q

        print("---------------------------------------------------------------------------")    
        print(f"\nSeřazeno od nejmenšího: {a}, {b}, {c}, {d}")
        print("---------------------------------------------------------------------------")
        
    elif volba == '2':
        # Sestupné řazení (od největšího)
        if a < b:
            q = a; a = b; b = q
        if b < c:
            q = b; b = c; c = q
        if c < d:
            q = c; c = d; d = q
            
        if a < b:
            q = a; a = b; b = q
        if b < c:
            q = b; b = c; c = q
            
        if a < b:
            q = a; a = b; b = q

        print("---------------------------------------------------------------------------")
        print(f"\nSeřazeno od největšího: {a}, {b}, {c}, {d}")
        print("---------------------------------------------------------------------------")

    else:
        print("\nNeplatná volba. Zadej prosím 1 nebo 2.")

# Spuštění programu
if __name__ == "__main__":
    seradit_promenne()