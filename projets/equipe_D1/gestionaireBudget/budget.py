# Initialisation des variables par demande

sal=int(input("Entrez votre salaire mensuel(FCFA) :\n"))
Aut=int(input("Entrez Autres revenus mensuels(FCFA):\n"))
Loy=int(input("Entrez Loyer/Location(FCFA):\n"))
Nourr=int(input("Entrez nourriture et marché  (FCFA):\n"))
Trans=int(input("Entrez transport (taxi,moto,essence,) (FCFA):\n"))
Lois=int(input("Entrez Loisirs et sorties  (FCFA):\n"))
Aut_D=int(input("Entrez Autres dépenses (santé,vêtements.....)(FCFA)\n:"))

# affichage ETAPE 1 et ETAPE 2

print("==🏦Bienvenue dans votres Calculateur de Budget Personnel!==\n")
print("=="*55)
print("-💰 ETAPE 1: Vos revenus\n")
print(f"Votre salaire mensuel (FCFA)={sal}FCFA\n")
print(f"Autres revenus mensuels  (FCFA)={Aut}FCFA\n")
print("💲ETAPE 2:Vos dépenses\n")
print(f"Loyer/Location (FCFA)={Loy}FCFA\n")
print(f"Nourriture et marché  (FCFA)={Nourr}FCFA\n")
print(f"Transport(taxi,moto,essence)  (FCFA)={Trans}FCFA\n")
print(f"Loisirs et sortie  (FCFA)={Lois}FCFA\n")
print(f"Autres dépenses (santé,vêtements....)  (FCFA)={Aut_D}FCFA\n")

#Affichage du résumé du Budget

print("=="*55)
print("==📊RESUME DE VOTRE BUDGET==")
print("=="*55)
revenus_t=sal+Aut
print(f"💰Revenus totaux={revenus_t} FCFA\n")
D_t=Loy+Nourr+Trans+Lois+Aut_D
print(f"💲Dépenses totales={D_t} FCFA\n")
B_rest=revenus_t-D_t
print(f"📈Budget restant ={B_rest} FCFA\n")
Pour_ep=(B_rest/revenus_t)*100
print(f"📊pourcentage épargné ={Pour_ep}%\n")
print("==📃REPARTITION DE VOS DEPENSES==\n")
Pour_Loy=(Loy/revenus_t)*100
print(f"🏠Loyer={Loy} FCFA ({Pour_Loy}% du revenu)\n")
Pour_Nourr=(Nourr/revenus_t)*100
print(f"🛒Nourriture={Nourr} FCFA ({Pour_Nourr}% du revenu)\n")
Pour_Trans=(Trans/revenus_t)*100
print(f"🛵Transport={Trans} FCFA({Pour_Trans}% du revenu)\n")
Pour_Lois=(Lois/revenus_t)*100
print(f"🎉Loisirs={Lois} FCFA({Pour_Lois}% du revenu)\n")
Pour_Aut_D=(Aut_D/revenus_t)*100
print(f"👜Autres dépenses={Aut_D}FCFA({Pour_Aut_D}% du revenu)\n")

# Affichage des calculs utiles

print("==🧮CALCULS UTILES:==\n")
B_jour=(B_rest/30)
print(f"🤑budget disponible par jour={B_jour}FCFA\n")
Eco_an=(B_rest *12)
print(f"💎Economies potentielles par an={Eco_an}FCFA\n")