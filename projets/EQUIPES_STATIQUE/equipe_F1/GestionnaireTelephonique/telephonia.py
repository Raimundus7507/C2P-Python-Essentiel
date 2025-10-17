
# Fonction accueil
solde = 0.0
def Accueil():
    global nom
    print("=== GESTIONNAIRE DE CRÉDIT TÉLÉPHONIQUE===")
    nom = input("\n Comment vous appelez-vous ? : ")

# Fonction option
def Option(solde) :
    print(f"\nBienvenue {nom} dans votre gestionnaire de crédit moov !")
    print("\n=== MENU PRINCIPAL ===")
    print(f"Bonjour {nom}, Votre solde est de {solde} FCFA")
    print("1. Achat de crédit")
    print("2. Passer un appel")
    print("3. Envoyer un SMS")
    print("4. Voir mon solde")
    print("5. Quitter\n")

# Une fonction qui présente les options et demande votre choix
def Option_choix(solde):
    global choix
    Option(solde)
    choix = int(input("Votre choix : "))
    print()
# la fonction operation
def Operation(solde) :
    while True:
        if choix == 1 :
            print("\n === ACHAT DE CRÉDIT ===")
            solde += float(input("Combien voulez-vous recharger (FCFA) ? : "))
            print("✅ Recharge effectuée !")
            print(f"Votre nouveau solde est {solde} FCFA\n")
            Option_choix(solde)
        elif choix == 2 :
            print("\n === PASSER UN APPEL ===")
            duree = float(input("Durée de votre appel (minute) ? : "))
            print(f"Coût de l'appel {duree} minutes x 25 FCFA = {duree*25} FCFA")
            if duree*25 <= solde :
                print("✅ Appel effectuée !")
                solde -= duree * 25
                print(f"Votre nouveau solde {solde} FCFA")
                Option_choix(solde)
            else :
                print(f"❌ Crédit insuffisant, Votre solde est {solde} (FCFA)")
                print(f" Il vous manque {duree*25 - solde} FCFA")
                Option_choix(solde)
        elif choix == 3 :
            print("\n=== Envoyer des SMS ===")
            nbreSMS = int(input("Combien de SMS voulez-vous envoyer ?: "))
            print(f"\nCoût des SMS : { nbreSMS} SMS x 25 FCFA = {nbreSMS*25} FCFA")
            if solde >= nbreSMS*25 :
                solde -= nbreSMS * 25
                print("✅ SMS envoyés")
                print(f"Votre nouveau solde {solde} FCFA")
                Option_choix(solde)
            else :
                 print(f"❌ Crédit insuffisant, Votre solde est {solde} (FCFA)")
                 print(f" Il vous manque {nbreSMS*25 - solde} FCFA")
                 Option_choix(solde)
        elif choix == 4 :
            print(f"Bonjour {nom}, Votre solde est {solde}")
            Option_choix(solde)
        elif choix == 5 :
            print("Merci d'avoir utilisé Votre gestionnaire de crédit !")
            print(f"À bientôt {nom}! 👋\n")
            break
    return solde

# Fonction principal
Accueil()
Option_choix(solde)
solde += Operation(solde)
