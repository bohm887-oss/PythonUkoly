a= int(input("Zadejte první číslo: "))
b= int(input("Zadejte druhé číslo: "))  
c= int(input("Zadejte třetí číslo: "))

min = a
max = a

# Zpracování proměnné b
if b < min:
    min = b
elif b > max:
    max = b

# Zpracování proměnné c
if c < min:
    min = c
elif c > max:
    max = c

print(f"Minimum je: {min}")
print(f"Maximum je: {max}")