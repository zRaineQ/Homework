# Napiš program, který vypočítá faktoriál čísla.

Number = int(input("Zadej číslo které se bude počítat: ")) # Vytvoříme inteager input
Factorial = 1 # Vytvoříme proměnou
for i in range(1, Number + 1):
    Factorial *= i

print("Faktoriál čísla",Number, "je", (Factorial))