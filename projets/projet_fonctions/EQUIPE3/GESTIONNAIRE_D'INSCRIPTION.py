# Projet de gestionnaire d'inscription

# Variables globales
nombre_total_inscrits = 0
effectif_6eme = 0
effectif_5eme = 0
effectif_4eme = 0
effectif_3eme = 0
effectif_2nde = 0
effectif_1ere = 0
effectif_terminale = 0
recettes_totales = 0
eff_bourse_excellence = 0 # Pour compteur de la bourse par excellence
eff_bourse_social = 0     # Pour compteur de la bourse par social
eff_bourse_familiale = 0  # Pour compteur de la bourse par familiale
eff_bourse_aucune = 0     # Pour compteur de la bourse par aucune

# Variables d'élève courantes (globales, pour ton style)
nom = ""
prenom = ""
age = 0
classe = ""
etablissement = ""
bourse = ""

# Variables de détail de frais (remplies par calculer_frais)
frais_base = 0
reduction = 0
frais_final = 0


# Definition des fonctions

#Fonction pour l'affichage du menu
def afficher_menu():
    print("""
1️⃣  Inscrire un élève
2️⃣  Consulter l'élève actuel
3️⃣  Modifier les informations
4️⃣  Calculer les frais (détail)
5️⃣  Voir les statistiques
6️⃣  Quitter 🛑""")


# Fonction pour la saisie de la variable l'âge
def saisir_age():
    while True:
        try:
            age = int(input("Âge : "))
            if age < 10 or age > 25:
                print("⚠️ Âge invalide ! Entre 10 et 25 ans.")
                continue
            return age
        except ValueError:
            print("🚫 Erreur ! Entrez un nombre valide.")

# Fonction pour la saisie de la variable classe
def saisie_classe():
    classe = input("Entrer la classe (6ème, 5ème, 4ème, 3ème, 2nde, 1ère, Tle) de l'élève: ")
    while (classe != "6ème") and (classe != "5ème") and (classe!= "4ème") and (classe != "3ème") and (classe != "2nde") and (classe != "1ère") and (classe != "Tle"):
        classe = input("Entrer la classe (6ème, 5ème, 4ème, 3ème, 2nde, 1ère, Tle): ")
    return classe

# Fonction pour la saisie de la variable etablissement
def saisie_etablissement():
    etablissement = input("Entrer Type d'établissement (public, privé, technique): ")
    while (etablissement != "public") and (etablissement != "privé") and (etablissement != "technique"):
        etablissement = input("Entrer Type d'établissement (public, privé, technique): ")
    return etablissement

# Fonction pour la saisie de la variable bourse
def saisie_bourse():
    bourse = input("Entrer type de bourse (excellence, sociale, familiale, aucune): ")
    while (bourse  != "excellence") and (bourse  != "sociale") and (bourse  != "familiale") and (bourse  != "aucune"):
        bourse = input("Entrer type de bourse (excellence, sociale, familiale, aucune): ")
    return bourse


#Fonction qui calcule les frais

def calculer_frais(etablissement, bourse="aucune"):
    global frais_base, reduction, frais_final

    frais_base = 35000 if etablissement == "privé" else 0
    reduction = 0.5 if bourse == "excellence" else 0.3 if bourse == "sociale" else 0.2 if bourse == "familiale" else 0

    montant_reduction = frais_base * reduction
    frais_final = frais_base - montant_reduction + 2000  # frais APE


    print(f"- Frais de base : {frais_base} FCFA")
    print(f"- Montant de la réduction ({int(reduction*100)}%) : -{montant_reduction} FCFA")
    print(f"- Frais APE : 2000 FCFA")
    print(f"- Montant à payer : {frais_final} FCFA")

    return frais_final



#Fonction qui affiche les details des frais
def detail_frais():
    global frais_base, reduction, frais_final
    fr_APE = 2000
    fr_cantine = 1500
    fr_transport = 1000

    # sécurité si detail_frais est appelé avant calculer_frais
    if frais_base is None:
        print("Aucun calcul de frais disponible. Veuillez d'abord calculer les frais.")
        return

    montant_reduction = frais_base * reduction
    total_pay = (frais_base - montant_reduction) + fr_cantine + fr_transport + fr_APE

    print("\n--- DÉTAIL COMPLET DES FRAIS ---")
    print(f"Frais de base : {frais_base} FCFA")
    print(f"Réduction : -{montant_reduction} FCFA")
    print(f"Frais cantine : {fr_cantine} FCFA")
    print(f"Frais transport : {fr_transport} FCFA")
    print(f"Frais APE : {fr_APE} FCFA")
    print(f"TOTAL (avec cantine & transport) : {total_pay} FCFA")


# Fonction pour la disponibilité des places
def verifier_disponibilite(classe):
    global effectif_6eme, effectif_5eme, effectif_4eme, effectif_3eme
    global effectif_2nde, effectif_1ere, effectif_terminale

    if classe == "6ème":
        effectif = effectif_6eme
    elif classe == "5ème":
        effectif = effectif_5eme
    elif classe == "4ème":
        effectif = effectif_4eme
    elif classe == "3ème":
        effectif = effectif_3eme
    elif classe == "2nde":
        effectif = effectif_2nde
    elif classe == "1ère":
        effectif = effectif_1ere
    elif classe == "Tle":
        effectif = effectif_terminale
    else:
        effectif = 0

    return effectif < 45

#Fonction pour l'option 1
def inscrire_eleve():
    global nombre_total_inscrits, recettes_totales
    global effectif_6eme, effectif_5eme, effectif_4eme, effectif_3eme
    global effectif_2nde, effectif_1ere, effectif_terminale
    global eff_bourse_excellence, eff_bourse_aucune, eff_bourse_social, eff_bourse_familiale
    global nom, prenom, age, etablissement, bourse, classe

    print("--" * 30)
    nom = input("Entrer nom de l'élève : ")
    prenom = input("Entrer prénom de l'élève : ")
    age = saisir_age()
    classe = saisie_classe()

    if not verifier_disponibilite(classe):
        print("⚠️ Place maximale atteinte pour cette classe !")
        return  # on sort sans rien modifier

    # incrémenter le total d'inscrits uniquement si l'inscription va se faire
    nombre_total_inscrits += 1

    # mise à jour effectif par classe
    if classe == "6ème":
        effectif_6eme += 1
    elif classe == "5ème":
        effectif_5eme += 1
    elif classe == "4ème":
        effectif_4eme += 1
    elif classe == "3ème":
        effectif_3eme += 1
    elif classe == "2nde":
        effectif_2nde += 1
    elif classe == "1ère":
        effectif_1ere += 1
    elif classe == "Tle":
        effectif_terminale += 1

    etablissement = saisie_etablissement()
    bourse = saisie_bourse()

    # compteur bourse
    if bourse == "excellence":
        eff_bourse_excellence += 1
    elif bourse == "sociale":
        eff_bourse_social += 1
    elif bourse == "familiale":
        eff_bourse_familiale += 1
    elif bourse == "aucune":
        eff_bourse_aucune += 1

    print("--" * 30)
    print("FRAIS CALCULÉS\n")
    frais = calculer_frais(etablissement, bourse)
    # On ajoute une seule fois aux recettes ici (inscription effective)
    recettes_totales += frais
    print(f"- Frais totaux ajoutés aux recettes : {frais} FCFA")
    print("Élève inscrit avec succès ✅\n")

#Fonction pour l'option 2
def consult_eleve():
    global nom, prenom, age, classe, etablissement, bourse, frais_final, recettes_totales
    print("\n--- CONSULTATION ÉLÈVE ---")
    print(f"Nom : {nom}")
    print(f"Prénom : {prenom}")
    print(f"Age : {age}")
    print(f"Classe : {classe}")
    print(f"Etablissement : {etablissement}")
    print(f"Type de bourse : {bourse}")
    # frais_final peut être 0 si aucun calcul effectué ; c'est acceptable
    print(f"Frais totaux (dernier calcul) : {frais_final} FCFA")
    print(f"Recettes totales (toutes inscriptions) : {recettes_totales} FCFA")
    print("Statut: Inscription complète\n")

#Fonction pour l'option 3
def modifier_eleve():
    global recettes_totales
    global effectif_6eme, effectif_5eme, effectif_4eme, effectif_3eme
    global effectif_2nde, effectif_1ere, effectif_terminale
    global nom, prenom, age, classe, etablissement, bourse

    print("--- MODIFICATION ÉLÈVE ---")
    print(f"Nom actuel : {nom}")
    nom = input("Entrer le nouveau nom  : ")
    print(f"Nouveau nom : {nom}")

    print(f"Prénom actuel : {prenom}")
    prenom = input("Entrer le nouveau prénom : ")
    print(f"Nouveau prénom : {prenom}")

    print(f"Âge actuel : {age}")
    age = saisir_age()
    print(f"Nouvel âge : {age}")

    ancienne_classe = classe
    print(f"Classe actuelle : {classe}")
    classe = saisie_classe()
    print(f"Nouvelle classe : {classe}")

    print(f"Etablissement actuel : {etablissement}")
    etablissement = saisie_etablissement()
    print(f"Nouvel établissement : {etablissement}")

    print(f"Type de bourse actuel : {bourse}")
    bourse = saisie_bourse()
    print(f"Nouveau type de bourse : {bourse}")

    # Recalcul des frais pour cette nouvelle configuration
    frais = calculer_frais(etablissement, bourse)
    # On suppose que modification entraîne un paiement supplémentaire : on ajoute une fois
    recettes_totales += frais
    print(f"frais totaux (ajoutés aux recettes) : {frais} FCFA")

    # Mettre à jour les effectifs (ancienne -> nouvelle)
    if ancienne_classe == "6ème":
        effectif_6eme -= 1
    elif ancienne_classe == "5ème":
        effectif_5eme -= 1
    elif ancienne_classe == "4ème":
        effectif_4eme -= 1
    elif ancienne_classe == "3ème":
        effectif_3eme -= 1
    elif ancienne_classe == "2nde":
        effectif_2nde -= 1
    elif ancienne_classe == "1ère":
        effectif_1ere -= 1
    elif ancienne_classe == "Tle":
        effectif_terminale -= 1

    if classe == "6ème":
        effectif_6eme += 1
    elif classe == "5ème":
        effectif_5eme += 1
    elif classe == "4ème":
        effectif_4eme += 1
    elif classe == "3ème":
        effectif_3eme += 1
    elif classe == "2nde":
        effectif_2nde += 1
    elif classe == "1ère":
        effectif_1ere += 1
    elif classe == "Tle":
        effectif_terminale += 1

    print("INFORMATIONS MODIFIÉES AVEC SUCCÈS !\n")

#Fonction pour option 4
def calculer_Dfrais():
    # Cette option calcule les frais (sans ajouter aux recettes) puis affiche le détail complet.
    global classe, etablissement, bourse, frais_final

    if not etablissement or not bourse:
        print("Aucune information d'établissement/bourse sur l'élève actuel. Veuillez d'abord inscrire ou modifier l'élève.")
        return

    print(f"Classe : {classe}")
    print(f"Etablissement : {etablissement}")
    print(f"Type de bourse : {bourse}")

    print("\nDETAIL DES FRAIS")
    print("--" * 55)
    # calculer_frais ici sert à mettre à jour frais_base, reduction, frais_final (mais ne modifie pas recettes_totales)
    calculer_frais(etablissement, bourse)
    # afficher le détail complet (cantine, transport, APE)
    detail_frais()

#Fonction pour l'option 5
def statistic_gene():
    print("\n--- STATISTIQUES GÉNÉRALES ---")
    print(f"Nombre total d'inscrits : {nombre_total_inscrits}")
    print("Effectif par classe :")
    print(f" - 6ème : {effectif_6eme} élèves")
    print(f" - 5ème : {effectif_5eme} élèves")
    print(f" - 4ème : {effectif_4eme} élèves")
    print(f" - 3ème : {effectif_3eme} élèves")
    print(f" - 2nde : {effectif_2nde} élèves")
    print(f" - 1ère : {effectif_1ere} élèves")
    print(f" - Terminale : {effectif_terminale} élèves\n")
    print(f"Recettes totales : {recettes_totales} FCFA")
    print("Répartition des bourses :")

    print(f"""
    - Excellence : {eff_bourse_excellence}    élève(s)
    - Sociale :    {eff_bourse_social}        élève(s)
    - Familiale :  {eff_bourse_familiale}     élève(s)
    - Aucune :     {eff_bourse_aucune}        élève(s)""")


# Boucle principale
print()
print("GESTIONNAIRE D'INSCRIPTION SCOLAIRE")
print("=" * 55)
afficher_menu()
choix = input("Entrer entre 1 et 6 : ")
while choix != "6":

    if choix == "1":
        print("1. Inscrire un élève")
        inscrire_eleve()

    elif choix == "2":
        print("--" * 55)
        print("2. Consulter l'élève actuel")
        consult_eleve()

    elif choix == "3":
        print("3. Modifier les informations")
        print("--" * 55)
        modifier_eleve()

    elif choix == "4":
        print("4. Calculer les frais")
        print("--" * 55)
        calculer_Dfrais()

    elif choix == "5":
        print("5. Voir les statistiques")
        print("--" * 55)
        statistic_gene()

    else:
        print("\nChoix invalide, veuillez réessayer")

    print("GESTIONNAIRE D'INSCRIPTION SCOLAIRE")
    print("-" * 55)
    afficher_menu()
    choix = input("Entrer entre 1 et 6 : ")
else:
    print("Merci d'avoir utilisé le gestionnaire d'inscription !")
