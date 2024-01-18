# Vypiš program který vydělí v listu pouze čísla která se dá dělit 5.

ListWithNumbers = [10, 20, 37, 69, 55]
print("Vyděleno číslem 5 je:")
for ThisMagic in ListWithNumbers:
    if ThisMagic % 5 == 0:
        print(ThisMagic)