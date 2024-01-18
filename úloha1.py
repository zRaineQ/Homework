# Na vstupu je věk člověka v letech. 
# Vytiskněte pro kontrolu zadaný věk, poté počet uplynulých dní a počet minut života.

age = int(input("Zadej tvůj věk: "))

age_days = age * 365 # Vytvořímě proměnou která vynásobí age
age_mins = age_days * 24 * 60 # proměná vynásobí age_days

print("Zadaný věk: ", age)
print("Počet dní: ", age_days)
print("Počet minut: ", age_mins)