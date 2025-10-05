#Affichage de l'utilité du programme
print("\n🏦Bienvenue dans votre Calculateur de Budget Personnel!🏦")
print("="*60,"\n")

#Prise de l'utilisateur de ses revenus mensuels
print("💰 ÉTAPE 1 : Vos revenus")
salaire_mensuel = float(input("Entrer votre salaire mensuel (FCFA) :"))
autre_revenues = float(input("Autres revenus mensuels (FCFA) : "))

# Prise des dépenses de l'utilisateur
print("\n💸 ÉTAPE 2 : Vos dépenses")
loyer_location = float(input("Loyer/Location (FCFA) : "))
nourriture_marche = float(input("Nourriture et marché (FCFA) : "))
transport = float(input("Transport(taxi,moto,essence) (FCFA): "))
loisirs_sorties = float(input("Loisirs et sorties (FCFA) : "))
autre_depense = float(input("Autres dépense(santé,vetement...) (FCFA) :"))

#Traitement de certains opération
revenus_totaux = salaire_mensuel + autre_revenues
depenses_totales = loyer_location + nourriture_marche + transport + loisirs_sorties + autre_depense
budget_restant = revenus_totaux - depenses_totales
pourcentage_epargne = float((budget_restant/revenus_totaux)*100)

#Affichage du revenues de l'utilisateur
print(f"\n{'='*30}")
print("📊 RÉSUMÉ DE VOTRE BUDGET 📊")
print(f"{'='*30}")

print(f"💰 Revenus totaux      : {revenus_totaux:.0f} FCFA")
print(f"💸 Dépenses totales    : {depenses_totales:.0f} FCFA")
print(f"📈 Budget restant      : {budget_restant:.0f} FCFA")
print(f"📊 Pourcentage épargné : {pourcentage_epargne:.1f}%")

#Traitement de certains opérations
Loyer = float((loyer_location/revenus_totaux)*100)
Nourriture = float((nourriture_marche/revenus_totaux)*100)
Transport = float((transport/revenus_totaux)*100)
Loisirs = float((loisirs_sorties/revenus_totaux)*100)
Autres = float((autre_depense/revenus_totaux)*100)

#Affichages des pourcentages des dépenses par rapport aux revenues totaux de l'utilisateur
print("\n📋 RÉPARTITION DE VOS DÉPENSES :")
print(f"🏠Loyer   :{loyer_location:.0f} FCFA ({Loyer:.1f}%du revenu)")
print(f"🛒 Nourriture   : {nourriture_marche:.0f} FCFA ({Nourriture:.1f}% du revenu)")
print(f"🛵 Transport    : {transport:.0f} FCFA ({Transport:.1f}% du revenu)")
print(f"🎉 Loisirs      : {loisirs_sorties:.0f} FCFA ({Loisirs:.1f}% du revenu)")
print(f"💼 Autres       : {autre_depense:.0f} FCFA ({Autres:.1f}% du revenu)")

#Traitement de certains operations
budget_jour = float(budget_restant/30)
economie_potentielle = float((budget_jour * 30)*12)

#Affichages des calcul utiles
print("\n🔢 CALCULS UTILES :")
print(f"💵 Budget disponible par jour : {budget_jour} FCFA")
print(f"💎 Économies potentielles par an : {economie_potentielle}FCFA")
