# Napiš program který napíše zda zadané číslo je sudé nebo liché.

hodnota = float(input("Zadej hodnotu ")) # Vytvoříme proměnou, použijeme input aby jsme mohli napsat naše čislo.
if hodnota%2==0: # Pokud hodnota % 2 se rovná nule
   print("Toto číslo je sudé")
else:
   print("Toto číslo je liché")