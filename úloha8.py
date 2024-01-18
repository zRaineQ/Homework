# Napiš program, který zjistí zda se jedná o čtverec nebo obdelník, také vypíše kolik jsou strany v cm.

a = input("Zadej velikost a ")
b = input("Zadej velikost b ")

if a == b:
   print("Čtverec má delku strany ",a,"cm")
else:
   print("Obdelník má délku strany ",a,"cm", b, "cm")