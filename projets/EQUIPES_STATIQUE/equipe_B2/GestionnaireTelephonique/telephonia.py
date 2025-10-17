# === VARIABLES GLOBALES DECLARATIONS ===
solde = 0.0
tarif_appel_minute = 25.0
tarif_sms = 25.0
nom_utilisateur = ""

# === FONCTIONS NECESSAIRES ===
# Fonction pour demander le nom de l'utilisateur
def demander_nom() :
    # Declaration de la variable globale nom_utilisateur
    global nom_utilisateur
    nom_utilisateur = input("Comment vous appelez-vous ? ")
    print(f"\nBienvenue {nom_utilisateur} dans votre gestionnaire de crédit Moov !\n")

# Fonction pour afficher le solde actuel
def afficher_solde() :
    print(f"\nBonjour {nom_utilisateur}, votre solde est de {solde:.1f} FCFA\n")

# Fonction pour acheter du crédit
def acheter_credit() :
    # Declaration de la variable globale solde
    global solde
    print("\n=== ACHAT DE CRÉDIT ===")
    montant_recharge = input("Combien voulez-vous recharger (FCFA) ? ")
    # Vérification que l'entrée est un nombre positif
    if montant_recharge.isdigit():
        montant_recharge = float(montant_recharge)
        # Vérification que le montant de la recharge est positif
        if montant_recharge > 0:
            solde += montant_recharge
            print("\n✅ Recharge effectuée !")
            afficher_solde()
            return
        else :
            print("❌ Entrée invalide. Veuillez entrer un nombre positif.\n")
    else:
        print("❌ Entrée invalide. Veuillez entrer un nombre positif.\n")

# Fonction pour passer un appel
def passer_appel() :
    # Declaration de la variable globale solde
    global solde
    print("\n=== PASSER UN APPEL ===")
    duree_appel = input("Durée de votre appel (minutes) ? ")
    # Vérification que l'entrée est un nombre positif
    if duree_appel.isdigit():
        duree_appel = float(duree_appel)
        # Vérification que la durée de l'appel est positive
        if duree_appel > 0:
            cout = duree_appel * tarif_appel_minute
            print(f"\nCoût de l'appel : {duree_appel:.0f} minutes × {tarif_appel_minute:.0f} FCFA = {cout:.1f} FCFA")
            if solde >= cout:
                solde -= cout
                print("✅ Appel effectué !")
                afficher_solde()
            else:
                manque = cout - solde
                print(f"❌ Crédit insuffisant ! Votre solde est de {solde:.1f} FCFA")
                print(f"Il vous manque {manque:.1f} FCFA\n")
        else:
            print("❌ Entrée invalide. Veuillez entrer un nombre positif.\n")
    else:
        print("❌ Entrée invalide. Veuillez entrer un nombre positif.\n")

# Fonction pour envoyer des SMS
def envoyer_sms():
    # Declaration de la variable globale solde
    global solde
    print("\n=== ENVOYER DES SMS ===")
    nombre_sms = input("Combien de SMS voulez-vous envoyer ? ")
    # Vérification que l'entrée est un entier positif
    if nombre_sms.isdigit():
        nombre_sms = int(nombre_sms)
        # Vérification que le nombre de SMS est positif
        if nombre_sms > 0:
            cout = nombre_sms * tarif_sms
            print(f"\nCoût des SMS : {nombre_sms} SMS × {tarif_sms:.0f} FCFA = {cout:.1f} FCFA")
            if solde >= cout:
                solde -= cout
                print("✅ SMS envoyés !")
                afficher_solde()
            else:
                manque = cout - solde
                print(f"❌ Crédit insuffisant ! Votre solde est de {solde:.1f} FCFA")
                print(f"Il vous manque {manque:.1f} FCFA\n")
        else:
            print("❌ Entrer invalide. Veuillez entrer un entier positif.\n")
    else:
        print("❌ Entrer invalide. Veuillez entrer un entier positif.\n")

# Fonction pour afficher le menu et obtenir le choix de l'utilisateur
def afficher_menu():
    print("=== MENU PRINCIPAL ===")
    afficher_solde()
    print("1. Acheter du crédit")
    print("2. Passer un appel")
    print("3. Envoyer des SMS")
    print("4. Voir mon solde")
    print("5. Quitter")
    choix = input("\nVotre choix : ")
    # Vérification que l'entrée est un entier entre 1 et 5
    if choix.isdigit():
        return int(choix)
    else:
        print("❌ Choix invalide. Veuillez entrer un nombre entre 1 et 5.\n")
        return None


# === PROGRAMME PRINCIPAL ===
# Affichage de l'utilité du programme
print("\n=== GESTIONNAIRE DE CRÉDIT TÉLÉPHONIQUE ===\n")
# Demander le nom de l'utilisateur au début
demander_nom()

# Boucle principale du menu
while True:
    # Afficher le menu et obtenir le choix de l'utilisateur
    choix = afficher_menu()
    if choix == 1:
        acheter_credit()
    elif choix == 2:
        passer_appel()
    elif choix == 3:
        envoyer_sms()
    elif choix == 4:
        afficher_solde()
    elif choix == 5:
        print(f"\nMerci d'avoir utilisé votre gestionnaire de crédit !\nÀ bientôt {nom_utilisateur} ! 👋")
        break
    else:
        print("Veuillez choisir une option valide entre 1 et 5.\n")