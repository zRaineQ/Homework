# Vytvoř string který poté bude hodnocen zda je prava nebo lež pomocí podmínky.

Question = "Je HTML jednoduché?" # Vytvoříme naší proměnou s otázkou
print(Question) # Tu vyvoláme.

Answer = input("Napiš svojí odpověd:" ) # Poté vytvoříme input

if Answer == "Ano" or "ano": # No a zde je podmínka, pokud text obsahuje Ano nebo ano tak vyvolá daný string.
    print("Možná máš pravdu.")

else: Answer == "Ne" or "ne" # No a to samé zde.
print("No.. nevím kámo.")
