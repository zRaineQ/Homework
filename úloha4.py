# Napiš program, který odstraní znaky ze stringu a vrátí nový string

def RemoveCharacters(Word, cutted):  # Vytvoříme funkci
    print('Původní slovo bylo:', Word) # Vypíšeme naše původní slovo
    CutWord = Word[cutted:] # Vytvořímě proměnou
    return CutWord # Vrátíme proměnou

print(RemoveCharacters("Synapse is useless", 6)) # Vypíšeme naše ořízlé slovo