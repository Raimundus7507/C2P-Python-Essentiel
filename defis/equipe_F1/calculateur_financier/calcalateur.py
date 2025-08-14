#Déclaration et saisie des données

print('Calculateur d''économie-version 1.0')
Nom=input('Nom:')
Revenus=input("Revenus mensuelles (FCFA):")
Depenses=input("Dépenses mensuelles (FCFA):")
Economies=int(Revenus) - int(Depenses)

#Affichage résultat
print("=== BILAN MENSUEL ===")
print(str(Nom),'- Revenus:', int(Revenus),'FCFA')
print('Dépenses:',int(Depenses),'FCFA')
print('Economies:',int(Economies),'FCFA')
print('Taux d''épargne:',int(Economies)/int(Revenus) * 100,'%')