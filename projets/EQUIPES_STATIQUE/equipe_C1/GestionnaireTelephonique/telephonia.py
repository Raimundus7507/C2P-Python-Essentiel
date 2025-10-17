nom = ""
solde = 0

def main():
    global nom, solde
    print("=== GESTIONNAIRE DE CRÉDIT TÉLÉPHONIQUE ===\n")
    nom = input("Comment vous appelez-vous ? ")
    print(f"Bienvenue {nom} dans votre gestionnaire de crédit Moov !")
    input("\nAppuyez sur Entrée pour continuer...")
    while True:
        choix = afficher_menu()
        if choix == "1":
            gerer_achat_credit()
        elif choix == "2":
            gerer_appel()
        elif choix == "3":
            gerer_sms()
        elif choix == "4":
            voir_solde()
        elif choix == "5":
            quitter()
        else:
            print("Choix invalide, veuillez réessayer.")

def afficher_menu():
    global nom, solde
    print("\n=== MENU PRINCIPAL ===")
    print(f"Bonjour {nom}, votre solde est de {solde} FCFA\n")
    print("1. Acheter du crédit")
    print("2. Passer un appel")
    print("3. Envoyer des SMS")
    print("4. Voir mon solde")
    print("5. Quitter")
    choisir = input("Votre Choix : ")
    return choisir

def gerer_achat_credit():
    global solde
    print("\n=== ACHAT DE CRÉDIT ===")
    recharge = input("Combien voulez-vous recharger (FCFA) ? ")
    while not recharge.isdigit() or int(recharge) <= 0:
        print("Entrez une recharge valide")
        recharge = input("Combien voulez-vous recharger (FCFA) ? ")
    solde += int(recharge)
    print("\n✅ Recharge effectuée !")
    print(f"Votre nouveau solde est de {solde} FCFA")

def gerer_appel():
    global solde
    print("\n=== PASSER UN APPEL ===")
    appel = input("Durée de votre appel (minutes) ? ")
    while not appel.isdigit() or int(appel) <= 0:
        print("Entrez une durée valide")
        appel = input("Durée de votre appel (minutes) ? ")
    cout = int(appel) * 75
    print(f"Coût de l'appel : {appel} minutes × 75 FCFA = {cout} FCFA")
    if cout > solde:
        manque = cout - solde
        print(f"❌ Crédit insuffisant ! Votre solde est de {solde} FCFA")
        print(f"Il vous manque {manque} FCFA")
    else:
        solde -= cout
        print("✅ Appel effectué !")
        print(f"Votre nouveau solde est de {solde} FCFA")

def gerer_sms():
    global solde
    print("\n=== ENVOYER DES SMS ===")
    sms = input("Combien de SMS voulez-vous envoyer ? ")
    while not sms.isdigit() or int(sms) <= 0:
        print("Entrez un nombre valide")
        sms = input("Combien de SMS voulez-vous envoyer ? ")
    cout = int(sms) * 75
    if cout > solde:
        print("Veuillez recharger votre compte!!!")
    else:
        solde -= cout
        print(f"Coût des SMS : {sms} SMS × 75 FCFA = {cout} FCFA")
        print("✅ SMS envoyés !")
        print(f"Votre nouveau solde est de {solde} FCFA")

def voir_solde():
    global nom, solde
    print(f"Salut {nom}, votre solde actuel est de {solde} FCFA")

def quitter():
    print("\nMerci d'avoir utilisé le gestionnaire de crédit Moov !")
    print(f"A bientôt {nom}! 👋")
    exit()

main()