def menu_pricipal0():
    while True:
        try:
            afficher_menu()
            choix= input("Veiller enter votre choix :")

            #gestion des choix
            if choix == "1":
                inscrire_eleve()
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
