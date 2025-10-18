#afficher de la message de bienvenu
print("=======================================================")
print("|| BIENVENUE DANS LA GESTION DES INSCRIPTION SCOLAIRE || ")
print("=======================================================")

#creation du fonction qui affiche le menu
def afficher_menu():
    print("1. Inscrire un élève")
    print("2.Consulter l'élève actuel")
    print("3.Modifier les informations")
    print("4.Calcuer des frais")
    print("5.Voir les statistique de l'Etablissement")
    print("6.QUITTER")
affiche_menu()
#boucle pour le numero 6
def menu_pricipal():
    while True:
        try:
            afficher_menu()
            choix= input("Veiller enter votre choix :")

            #gestion des choix
            if choix == "1":
                print("Vous avez choisis option 1")
            elif choix == "2":
                print("Vous avez choisis option 2")
            elif choix == "3":
                print("Vous avez choisis option 3")
            elif choix == "4":
                print("Vous avez choisis option 4")
            elif choix == "5":
                print("Vous avez choisis option 5")
            elif choix == "6":
                print("MERCI D'AVOIR UTILISER LE GESTIONNAIRE")
                break
            else:
                print("choix invalide!..veillez Reessayer")
        except Exception as erreur:
             print("Erreur :",erreur)
