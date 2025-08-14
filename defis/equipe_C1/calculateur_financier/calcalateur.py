print("Calculateur d'économies - Version 1.0")

nom = input("Nom : ")
r = int(input("Revenus mensuels (FCFA) : "))
d = int(input("Dépenses mensuelles (FCFA) : "))

e = r - d
taux_epargne = (e / r) * 100

print("=== BILAN MENSUEL ===")
print(nom, "- Revenus :", r, "FCFA")
print("Dépenses :", d, "FCFA")
print("Économies :", e, "FCFA")
print("Taux d'épargne :", taux_epargne, "%")