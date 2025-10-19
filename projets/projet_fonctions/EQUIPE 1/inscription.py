# Fonction d'inscription d'un élève
def inscrire_eleve():
    # Variables globales utilisées
    global nom, prenom, age, classe, etablissement, bourse, frais
    global nombre_total_inscrits
    global effectif_6eme, effectif_5eme, effectif_4eme, effectif_3eme
    global effectif_2nde, effectif_1ere, effectif_terminale
    global bourse_excellence, bourse_sociale, bourse_familiale, aucune_bourse
    # Message d'affichage de l'inscription d'un nouvel élève
    print("INSCRIPTION D'UN NOUVEL ÉLÈVE")

    # Saisie des informations de l'élève
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    age = saisir_age()
    classe = saisir_classe()
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
    elif classe == "Terminale":
        effectif_terminale += 1

    # Vérification des effectifs avant l'inscription
    if effectif_6eme <= 45 and effectif_5eme <= 45 and effectif_4eme <= 45 and effectif_3eme <= 45 and effectif_2nde <= 45 and effectif_1ere <= 45 and effectif_terminale <= 45:
        # Mise à jour de l'effectif selon la classe
        if classe == "6ème":
            effectif_6eme -= 1
        elif classe == "5ème":
            effectif_5eme -= 1
        elif classe == "4ème":
            effectif_4eme -= 1
        elif classe == "3ème":
            effectif_3eme -= 1
        elif classe == "2nde":
            effectif_2nde -= 1
        elif classe == "1ère":
            effectif_1ere -= 1
        elif classe == "Terminale":
            effectif_terminale -= 1
        # Saisie de l'établissement et du type de bourse
        etablissement = saisir_etablissement()
        if etablissement == 'privé':
            # Saisie du type de bourse
            bourse = saisir_bourse()
            # Mise à jour du nombre d'élèves selon le type de bourse
            if bourse == "excellence":
                bourse_excellence += 1
            elif bourse == "sociale":
                bourse_sociale += 1
            elif bourse == "familiale":
                bourse_familiale += 1
            else:
                aucune_bourse += 1
        else:
            bourse = "aucune"
            aucune_bourse += 1
        # Message d'affichage du calcul des frais
        print("\nFRAIS CALCULÉS")
        # Calcul des frais et mise à jour des recettes
        frais = calculer_frais(etablissement, bourse)

        print(f"Frais de base : {'35000 FCFA' if etablissement == 'privé' else '0 FCFA'}")
        if etablissement == 'privé':
            # Calcul de la réduction appliquée
            reduction = 0.5 if bourse == "excellence" else 0.3 if bourse == "sociale" else 0.2 if bourse == "familiale" else 0
            print(f"Réduction appliquée : {35000 * reduction} FCFA")

            print(f"Frais APE : 2000 FCFA")
            # Affichage du total des frais
            print(f"Total : {frais} FCFA")
        else:
            print("Frais APE : 2000 FCFA")
            print(f"Total : {frais} FCFA")

        nombre_total_inscrits += 1
        # Message de confirmation de l'inscription
        print("\nElève inscrit avec succès !")
    else:
        print("\nEffectif maximum atteint pour cette classe. Inscription impossible.")
        return


# Fonction de calcul des frais
def calculer_frais(etablissement, bourse):
    # Variable globale des recettes totales
    global recettes_totales

    # Calcul des frais
    frais_base = 35000 if etablissement == "privé" else 0
    reduction = 0.5 if bourse == "excellence" else 0.3 if bourse == "sociale" else 0.2 if bourse == "familiale" else 0
    frais_final = frais_base * (1 - reduction) + 2000  # + frais APE

    # Mise à jour des recettes
    recettes_totales += frais_final

    return frais_final


# Fonction de saisie et validation de l'âge
def saisir_age():
    # Saisie et validation de l'âge
    while True:
        try:
            age = int(input("Âge : "))
            if age < 10 or age > 25:
                print("Âge invalide ! Entre 10 et 25 ans.")
                continue
            return age
        except ValueError:
            print("Erreur ! Entrez un nombre valide.")


# Fonction de saisie et validation de la classe
def saisir_classe():
    # Saisie et validation de la classe
    while True:
        classe = input("Classe (6ème, 5ème, 4ème, 3ème, 2nde, 1ère, Terminale) : ")
        # Validation de la classe
        if classe == "6ème" or classe == "5ème" or classe == "4ème" or classe == "3ème" or classe == "2nde" or classe == "1ère" or classe == "Terminale":
            return classe
        else:
            print("Erreur ! Entrez une classe valide.")


# Fonction de saisie et validation du type de bourse
def saisir_bourse():
    # Saisie et validation du type de bourse
    while True:
        bourse = input("Type de bourse (excellence, sociale, familiale, aucune) : ")
        # Validation du type de bourse
        if bourse == "excellence" or bourse == "sociale" or bourse == "familiale" or bourse == "aucune":
            return bourse
        else:
            print("Type de bourse invalide ! Veuillez réessayer.")


# Fonction de saisie et validation de l'établissement
def saisir_etablissement():
    # Saisie et validation de l'établissement
    while True:
        etablissement = input("Établissement (public/privé) : ")
        # Validation de l'établissement
        if etablissement == "public" or etablissement == "privé":
            return etablissement
        else:
            print("Établissement invalide ! Veuillez réessayer.")