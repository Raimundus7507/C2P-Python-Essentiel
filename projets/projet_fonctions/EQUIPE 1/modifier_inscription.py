from main import saisir_age, saisir_classe, saisir_etablissement, saisir_bourse
# Fonction de modification des informations d'inscription d'un élève
def modifier_inscription () :
    # Globalisation des variables utilisées
    global nom, prenom, age, classe, etablissement, bourse
    global effectif_6eme, effectif_5eme, effectif_4eme, effectif_3eme
    global effectif_2nde, effectif_1ere, effectif_terminale
    global bourse_excellence, bourse_sociale, bourse_familiale, aucune_bourse
    # Message d'affichage de la modification des informations
    print("MODIFICATION DES INFORMATIONS")
    print(f"{'='*28}")
    # Affichage et modification du nom actuelle
    print(f"Nom actuel : {nom}")
    nom = input("Nouveau nom : ")
    # Affichage et modification du prénom actuelle
    print(f"Prénom actuel : {prenom}")
    prenom = input("Nouveau prénom : ")
    # Affichage et modification de l'age actuelle
    print(f"Âge actuel : {age}")
    age = saisir_age()
    # Affichage et modification de la classe actuelle
    print(f"Classe actuelle : {classe}")
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
    classe = saisir_classe()
    # Mise à jour de l'effectif selon la classe
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
    # Affichage et modification de l'établissement actuelle
    print(f"Établissement actuel : {etablissement}")
    etablissement = saisir_etablissement()
    # Si l'établissement est privé, permettre la modification du type de bourse
    if etablissement == 'privé' :
        # Affichage et modification du type de bourse actuelle
        print(f"Type de bourse actuel : {bourse}")
        if bourse == "excellence":
            bourse_excellence -= 1
        elif bourse == "sociale":
            bourse_sociale -= 1
        elif bourse == "familiale":
            bourse_familiale -= 1
        else:
            aucune_bourse -= 1
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
    else :
        bourse = "aucune"
    # Message de confirmation de la modification des informations
    print("\nINFORMATIONS MODIFIÉES AVEC SUCCÈS !")