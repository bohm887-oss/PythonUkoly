def spocti_vstupne():
    # Zadání vstupních údajů
    try:
        vek = float(input("Zadejte věk návštěvníka: "))
        je_student = input("Je student? (ano/ne): ").strip().lower()
        pocet_osob = int(input("Zadejte počet osob: "))
    except ValueError:
        print("Chyba: Zadejte platná číselná data pro věk a počet osob.")
        return

    # Základní cena jedné vstupenky
    zakladni_cena = 500
    
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

    # Výsledek
    print("\n--- Výsledek prodeje ---")
    print(f"Typ slevy: {nazev_slevy}")
    print(f"Cena za jednu vstupenku po slevě: {cena_za_jednu:.0f} Kč")
    print(f"Celková cena za všechny vstupenky: {celkova_cena:.0f} Kč")
