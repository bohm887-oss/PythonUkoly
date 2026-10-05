# Program, který podle zadané hodiny vypíše vhodný pozdrav.

try:
	hodina = float(input("Zadejte aktuální hodinu (0-23): "))

	# 1. Kontrola záporného čísla
	if hodina < 0:
		print("Hodina nemůže být záporná.")

	# 2. Kontrola horní hranice
	elif hodina >= 24:
		print("Zadávejte platné hodiny, které se nacházejí v rozmezí 0-23.")

	# 3. Určení pozdravu podle denního času
	elif 5 <= hodina < 9:
		print("Dobré ráno.")
	elif 9 <= hodina < 11.5:
		print("Dobré dopoledne.")
	elif 11.5 <= hodina < 12.5:
		print("Dobré poledne.")
	elif 12.5 <= hodina < 18:
		print("Dobré odpoledne.")
	elif 18 <= hodina < 22:
		print("Dobrý večer.")
	else:  # od 0 do 5 a od 22 do 24
		print("Dobrou noc.")

except ValueError:
	print("Zadejte platné číslo. 1:00 - 23:59")
