#Fonction de bienvenue et rôle du programme
def Accueil ():
    print("\n === GESTIONNAIRE DE BUDGET MENSUEL ===\n")
    print("Bonjour ! Je vais t'aider à gérer ton budget mensuel\n")


# Fonction conseiller
def Conseiller (pourcentage_economie):
    if pourcentage_economie < 0:
        print("Conseil : Il y a un GROS problème ! Ne dépensez pas plus d'argent que vous n'en gagner ! 😒")
    elif pourcentage_economie == 0:
        print("Conseil : Il y a un GROS problème ! Vous ne pouvez pas dépensez tout votre argent.😒")
    elif 0 < pourcentage_economie <= 50:
        print("Conseil :Conseil : Vous êtees sur la bonne voie. Continuez de travailler et d'économiser.😊")
    elif 50 < pourcentage_economie < 100:
        print(f"Conseil : Excellent ! Vous économisez {pourcentage_economie}% de vos revenus. Continuez comme ça. Vous pouvez même vous faire un peu plaisir.😁")
    else:
        print(f"Conseil : Cet argent est le VOTRE. Utilisez-le !")

# Verificateur des entrées 
def Verificateur (valeur):
    if valeur < 0 :
        int(input("Saisi invalide. Pas de nombre négatif resaisisez : "))

# fonction saisie et traitement des infos perso   
def Saisi_Traitement():
    valeur = revenu_mensuel = int(input("💰Quel est votre revenu mensuel ? : "))
    Verificateur(valeur)
    valeur = depense_logement = int(input("🏠Combien dépensez-vous pour le logement ? : "))
    Verificateur(valeur)
    valeur = budget_nourriture = int(input("🍕Budget nourriture mensuel ? : "))
    Verificateur(valeur)
    valeur = depense_transport = int(input("🚗Transport (essence, transport public) ? : "))
    Verificateur(valeur)
    valeur = budget_loisirs = int(input("🛝Budget loisirs ? : "))
   
    #Récapitulatif du budget
    print("\n=== RÉCAPITULATIF DE TON BUDGET ===\n")
    total_depense = depense_logement + depense_transport + budget_nourriture + budget_loisirs
    reste_dispo = revenu_mensuel - total_depense
    print(f"Revenus : {revenu_mensuel}")
    print(f"Dépenses totales : {depense_logement + depense_transport}")
    print(f"Reste disponible : {reste_dispo}")
    print("")
    pourcentage_economie = reste_dispo * 100 / revenu_mensuel
    print()
    #Appel consiller
    Conseiller (pourcentage_economie)


# Fonction pour reprendre
def Reprendre(): 
     while 1:
        #Possibilité de reprendre le calcul
        continuer = input("Souhaitez-vous refaire un calcul ? (oui/non) : ")
        if continuer.lower() == "non":
            break
        else :
            Saisi_Traitement()

# Fonction remerciement   
def Merci(): 
    print("\nMerci d'avoir utilisé le gestionnaire de budget ! 🙂")
# Programme principal
Accueil()
Saisi_Traitement()
Reprendre()
Merci()