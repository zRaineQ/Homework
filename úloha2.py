# Napište funkci, která vrátí True, pokud je první a poslední číslo daného seznamu stejné. 
# Pokud se čísla liší, vrátí hodnotu False.

def FirstAndLastIsSame(List): # Vytvoříme funkci
    print("List:", List)
    
    FirstNum = List[0] # Proměná říká který "index" chceme
    LastNum = List[5] # Proměná říká který "index" chceme
    
    if FirstNum == LastNum:
        return True
    else:
        return False

FirstList = [10, 20, 30, 40, 50, 10]
print("Tento první list je:", FirstAndLastIsSame(FirstList))

SecondList = [2, 4, 6, 8, 10, 9]
print("Tento druhý list je:", FirstAndLastIsSame(SecondList))

# A nebo..

# def message1():
    # print("Obsahuje dvě stejné čísla")

# def message2():
    # print("Neobsahuje dvě stejné čísla")    

# def FirstAndLastIsSame(List): # Vytvoříme funkci
    # print("List:", List)
    
    # FirstNum = List[0] 
    # LastNum = List[5]
    
    # if FirstNum == LastNum:
        # return message1
    # else:
        # return message2

# FirstList = [10, 20, 30, 40, 50, 10]
# print("Tento první list je:", FirstAndLastIsSame(FirstList))

# SecondList = [2, 4, 6, 8, 10, 9]
# print("Tento druhý list je:", FirstAndLastIsSame(SecondList))