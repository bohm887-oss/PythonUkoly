def spocti_vstupne():
    # Zadání vstupních údajů
    try:
        vek = float(input("Zadejte věk: "))
        je_student = input("Jste student? (ano/ne): ").strip().lower()
        pocet_osob = int(input("Zadejte počet osob: "))
        den = input("Zadejte den v týdnu: ").strip().lower()
    except ValueError:
        print("Chyba: Zadejte platná číselná data pro věk a počet osob.")
        return

    # Výzva C: Validace vstupu (ošetření záporných hodnot)
    if vek < 0 or pocet_osob < 1:
        print("Chyba: Neplatný počet osob nebo věk!")
        return

    # Výzva B: Víkendový příplatek pomocí ternárního operátoru
    priplatek = 50 if (den == "sobota" or den == "neděle") else 0
    zakladni_cena = 500 + priplatek

    # Rozhodovací logika pro slevy
    if pocet_osob >= 4:
        nazev_slevy = "Skupinová sleva (25 %)"
        cena_za_jednu = zakladni_cena * 0.75
    elif je_student == "ano" and vek < 26:
        nazev_slevy = "Studentská sleva (30 %)"
        cena_za_jednu = zakladni_cena * 0.70
    elif vek >= 65:
        nazev_slevy = "Seniorská sleva (20 %)"
        cena_za_jednu = zakladni_cena * 0.80
    else:
        nazev_slevy = "Žádná sleva"
        cena_za_jednu = zakladni_cena

    # Výpočet celkové ceny
    celkova_cena = cena_za_jednu * pocet_osob

    # Výzva A: Zkrácené skloňování pomocí ternárního operátoru
    slovo = "osoba" if pocet_osob == 1 else "osob"
    
    # Doplnění textu pro víkendové představení
    info_den = " (Víkendové představení)" if priplatek > 0 else ""

    # Výsledek (přizpůsobený vzoru z ukázky)
    print("\n--- Výsledná účtenka ---")
    print(f"Typ lístku: {pocet_osob} {slovo}{info_den}")
    print(f"Druh slevy: {nazev_slevy}")
    print(f"Cena za 1 vstupenku: {cena_za_jednu:.2f} Kč")
    print(f"Celková cena: {celkova_cena:.2f} Kč")


if __name__ == "__main__":
    spocti_vstupne()