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
eff_bourse_excellence = 0
eff_bourse_social = 0
eff_bourse_familiale = 0
eff_bourse_aucune = 0

# Élève
nom = ""
prenom = ""
age = 0
classe = ""
etablissement = ""
bourse = ""

# Variables de frais
frais_base = 0
reduction = 0
frais_final = 0

# Fonctions

def afficher_menu():
    print("""
1️⃣  Inscrire un élève
2️⃣  Consulter l'élève actuel
3️⃣  Modifier les informations
4️⃣  Calculer les frais (détail)
5️⃣  Voir les statistiques
6️⃣  Quitter 🛑""")

# --- Fonctions de saisie ---
def saisir_age():
    while True:
        try:
            mon_age = int(input("Âge : "))
            if mon_age < 10 or mon_age > 25:
                print("⚠ Âge invalide ! Entre 10 et 25 ans.")
                continue
            return mon_age
        except ValueError:
            print("🚫 Erreur ! Entrez un nombre valide.")

def saisie_classe():
    ma_classe = input("Entrer la classe (6ème, 5ème, 4ème, 3ème, 2nde, 1ère, Tle) : ")
    while (ma_classe != "6ème") and (ma_classe != "5ème") and (ma_classe!= "4ème") and (ma_classe != "3ème") and (ma_classe != "2nde") and (ma_classe != "1ère") and (ma_classe != "Tle"):
        print("🚫 Classe invalide ! Ressayez.")
        ma_classe = input("Entrer la classe (6ème, 5ème, 4ème, 3ème, 2nde, 1ère, Tle) : ")
    return ma_classe

def saisie_etablissement():
    mon_ets = input("Entrer le type d'établissement (public, privé, technique) : ")
    while (mon_ets != "public") and (mon_ets != "privé") and (mon_ets != "technique"):
        print("🚫 Type d'établissement invalide ! Ressayez.")
        mon_ets = input("Entrer le type d'établissement (public, privé, technique) : ")
    return mon_ets

def saisie_bourse():
    ma_bourse = input("Entrer le type de bourse (excellence, sociale, familiale, aucune) : ")
    while (ma_bourse  != "excellence") and (ma_bourse  != "sociale") and (ma_bourse  != "familiale") and (ma_bourse  != "aucune"):
        print("🚫 Type de bourse invalide ! Ressayez.")
        ma_bourse = input("Entrer le type de bourse (excellence, sociale, familiale, aucune) : ")
    return ma_bourse

# --- Calcul des frais ---
def calculer_frais(type_etab, type_bourse="aucune"):
    global frais_base, reduction, frais_final
    frais_base = 35000 if type_etab == "privé" else 0
    reduction = 0.5 if type_bourse == "excellence" else 0.3 if type_bourse == "sociale" else 0.2 if type_bourse == "familiale" else 0
    montant_reduction = frais_base * reduction
    frais_final = frais_base - montant_reduction + 2000  # frais APE
    print(f"- Frais de base : {frais_base} FCFA")
    print(f"- Réduction ({int(reduction*100)}%) : -{montant_reduction} FCFA")
    print(f"- Frais APE : 2000 FCFA")
    print(f"- Montant à payer : {frais_final} FCFA")
    return frais_final

def detail_frais():
    global frais_base, reduction, frais_final
    fr_ape = 2000
    fr_cantine = 1500
    fr_transport = 1000
    montant_reduction = frais_base * reduction
    total_pay = (frais_base - montant_reduction) + fr_cantine + fr_transport + fr_ape
    print("\n--- DÉTAIL COMPLET DES FRAIS ---")
    print(f"Frais de base : {frais_base} FCFA")
    print(f"Réduction : -{montant_reduction} FCFA")
    print(f"Frais cantine : {fr_cantine} FCFA")
    print(f"Frais transport : {fr_transport} FCFA")
    print(f"Frais APE : {fr_ape} FCFA")
    print(f"TOTAL (avec cantine & transport) : {total_pay} FCFA")

# --- Vérification de la disponibilité ---
def verifier_disponibilite(cl):
    global effectif_6eme, effectif_5eme, effectif_4eme, effectif_3eme
    global effectif_2nde, effectif_1ere, effectif_terminale
    if cl == "6ème":
        effectif = effectif_6eme
    elif cl == "5ème":
        effectif = effectif_5eme
    elif cl == "4ème":
        effectif = effectif_4eme
    elif cl == "3ème":
        effectif = effectif_3eme
    elif cl == "2nde":
        effectif = effectif_2nde
    elif cl == "1ère":
        effectif = effectif_1ere
    elif cl == "Tle":
        effectif = effectif_terminale
    else:
        effectif = 0
    return effectif < 45

# --- Option 1 : Inscription ---
def inscrire_eleve():
    global nombre_total_inscrits, recettes_totales
    global effectif_6eme, effectif_5eme, effectif_4eme, effectif_3eme
    global effectif_2nde, effectif_1ere, effectif_terminale
    global eff_bourse_excellence, eff_bourse_aucune, eff_bourse_social, eff_bourse_familiale
    global nom, prenom, age, etablissement, bourse, classe
    print("--" * 30)
    nom = input("Nom de l'élève : ")
    prenom = input("Prénom de l'élève : ")
    age = saisir_age()
    classe = saisie_classe()
    if not verifier_disponibilite(classe):
        print("⚠ Nombre de places maximal atteint pour cette classe !")
        return
    nombre_total_inscrits += 1
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
    recettes_totales += frais
    print(f"- Frais ajoutés aux recettes : {frais} FCFA")
    print("✅ Élève inscrit avec succès !\n")

# --- Option 2 : Consultation ---
def consult_eleve():
    print("\n--- CONSULTATION ÉLÈVE ---")
    print(f"Nom : {nom}")
    print(f"Prénom : {prenom}")
    print(f"Âge : {age}")
    print(f"Classe : {classe}")
    print(f"Etablissement : {etablissement}")
    print(f"Bourse : {bourse}")
    print(f"Frais (dernier calcul) : {frais_final} FCFA")
    print(f"Recettes totales : {recettes_totales} FCFA\n")

# --- Option 3 : Modification ---
def modifier_eleve():
    global recettes_totales, eff_bourse_excellence, eff_bourse_aucune, eff_bourse_social, eff_bourse_familiale
    global effectif_6eme, effectif_5eme, effectif_4eme, effectif_3eme
    global effectif_2nde, effectif_1ere, effectif_terminale
    global nom, prenom, age, classe, etablissement, bourse
    print("--- MODIFICATION ÉLÈVE ---")
    print(f"Nom actuel : {nom}")
    nom = input("Nouveau nom : ")
    print(f"Prénom actuel : {prenom}")
    prenom = input("Nouveau prénom : ")
    print(f"Âge actuel : {age}")
    age = saisir_age()
    print(f"Nouvel âge : {age}")
    ancienne_classe = classe
    print(f"Classe actuelle : {classe}")
    classe = saisie_classe()
    print(f"Nouvelle classe : {classe}")
    print(f"Etablissement actuel : {etablissement}")
    etablissement = saisie_etablissement()
    print(f"Nouvel Etablissement : {etablissement}")
    print(f"Bourse actuelle : {bourse}")
    bourse = saisie_bourse()
    print(f"Nouvelle bourse : {bourse}")
    frais = calculer_frais(etablissement, bourse)
    recettes_totales += frais
    if bourse == "excellence":
        eff_bourse_excellence += 1
    elif bourse == "sociale":
        eff_bourse_social += 1
    elif bourse == "familiale":
        eff_bourse_familiale += 1
    elif bourse == "aucune":
        eff_bourse_aucune += 1
    # mise à jour des effectifs
    if ancienne_classe != classe:
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
    print("✅ Informations modifiées avec succès !\n")

# --- Option 4 : Calcul détaillé ---
def calcul_de_frais():
    global etablissement, bourse
    if not etablissement or not bourse:
        print("Aucune information sur l'élève actuel. Veuillez d'abord inscrire ou modifier.")
        return
    print(f"Classe : {classe}")
    print(f"Etablissement : {etablissement}")
    print(f"Bourse : {bourse}\n")
    calculer_frais(etablissement, bourse)
    detail_frais()

# --- Option 5 : Statistiques ---
def statistic_gene():
    print("\n--- STATISTIQUES GÉNÉRALES ---")
    print(f"Nombre total d'inscrits : {nombre_total_inscrits}")
    print("Effectif par classe :")
    print(f" 6ème : {effectif_6eme}")
    print(f" 5ème : {effectif_5eme}")
    print(f" 4ème : {effectif_4eme}")
    print(f" 3ème : {effectif_3eme}")
    print(f" 2nde : {effectif_2nde}")
    print(f" 1ère : {effectif_1ere}")
    print(f" Terminale : {effectif_terminale}")
    print(f"Recettes totales : {recettes_totales} FCFA")
    print("Répartition des bourses :")
    print(f" - Excellence : {eff_bourse_excellence}")
    print(f" - Sociale : {eff_bourse_social}")
    print(f" - Familiale : {eff_bourse_familiale}")
    print(f" - Aucune : {eff_bourse_aucune}")

# Programme principal
def prog_principal():
    print("\nGESTIONNAIRE D'INSCRIPTION SCOLAIRE")
    print("=" * 55)
    afficher_menu()
    choix = input("Entrer votre choix (1,...,6) : ")
    while choix != "6":
        if choix == "1":
            inscrire_eleve()
        elif choix == "2":
            consult_eleve()
        elif choix == "3":
            modifier_eleve()
        elif choix == "4":
            calcul_de_frais()
        elif choix == "5":
            statistic_gene()
        else:
            print("Choix invalide. Réessayez.")
        print("\nGESTIONNAIRE D'INSCRIPTION SCOLAIRE")
        print("-" * 55)
        afficher_menu()
        choix = input("Entrer votre choix (1,...,6) : ")
    print("\nMerci d'avoir utilisé le gestionnaire d'inscription ! 👋")

prog_principal()