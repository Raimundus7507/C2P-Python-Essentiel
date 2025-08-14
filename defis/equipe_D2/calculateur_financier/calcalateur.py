print("Calculateur d'economies - Varsion 1.0")

#Saisi par l'utilisateur

nom = str(input("Nom : "))
R_mensuel = float(input("Revenus mensuels (FCFA) : "))
D_mensuel = float(input("Dépenses mensuelles (FCFA) : "))

#Affichage des resultats
print(nom ,"- Revenus : ", R_mensuel , " FCFA")
print("Dépenses : ", D_mensuel , " FCFA")

Epargne = float(R_mensuel - D_mensuel)
T_epargne = float(Epargne/R_mensuel *100)

print("Economies : ", Epargne ," FCFA")
print("Taux d'épargne : ", T_epargne , "%")