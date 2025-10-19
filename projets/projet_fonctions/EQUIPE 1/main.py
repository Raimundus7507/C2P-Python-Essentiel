# Fonction d'affichage du menu principal
def afficher_menu() :
    # Menu d'affichage principal
    print("\nGESTION D'INSCRIPTION SCOLAIRE")
    print(f"{'='*30}")
    # Options du menu
    print("\n1. Inscrire un élève")
    print("2. Consulter l'élève actuel")
    print("3. Modifier les informations")
    print("4. Calculer les frais")
    print("5. Voir les statistiques")
    print("6. Quitter")

# Fonction d'inscription d'un élève
def inscrire_eleve () :
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
        if etablissement == 'privé' :
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
        else :
            bourse = "aucune"
            aucune_bourse += 1
        # Message d'affichage du calcul des frais
        print("\nFRAIS CALCULÉS")
        # Calcul des frais et mise à jour des recettes
        frais = calculer_frais(etablissement, bourse)

        print(f"Frais de base : {'35000 FCFA' if etablissement == 'privé' else '0 FCFA'}")
        if etablissement == 'privé' :
            # Calcul de la réduction appliquée
            reduction = 0.5 if bourse == "excellence" else 0.3 if bourse == "sociale" else 0.2 if bourse == "familiale" else 0
            print(f"Réduction appliquée : {35000 * reduction} FCFA")

            print(f"Frais APE : 2000 FCFA")
            # Affichage du total des frais
            print(f"Total : {frais} FCFA")
        else :
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
def saisir_age() :
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
def saisir_classe() :
    # Saisie et validation de la classe
    while True:
        classe = input("Classe (6ème, 5ème, 4ème, 3ème, 2nde, 1ère, Terminale) : ")
        # Validation de la classe
        if classe == "6ème" or classe == "5ème" or classe == "4ème" or classe == "3ème" or classe == "2nde" or classe == "1ère" or classe == "Terminale" :
            return classe
        else :
            print("Erreur ! Entrez une classe valide.")

# Fonction de saisie et validation du type de bourse
def saisir_bourse() :
    # Saisie et validation du type de bourse
    while True:
        bourse = input("Type de bourse (excellence, sociale, familiale, aucune) : ")
        # Validation du type de bourse
        if bourse == "excellence" or bourse == "sociale" or bourse == "familiale" or bourse =="aucune":
            return bourse
        else :
            print("Type de bourse invalide ! Veuillez réessayer.")

# Fonction de saisie et validation de l'établissement
def saisir_etablissement() :
    # Saisie et validation de l'établissement
    while True:
        etablissement = input("Établissement (public/privé) : ")
        # Validation de l'établissement
        if etablissement == "public" or etablissement == "privé":
            return etablissement
        else :
            print("Établissement invalide ! Veuillez réessayer.")
    
# Fonction de consultation des informations de l'élève
def consulter_eleve () :
    # Variables globales utilisées
    global nom, prenom, age, classe, etablissement, bourse, frais
    # Message d'affichage de la consultation de l'élève actuel
    print("CONSULTATION DE L'ÉLÈVE ACTUEL")
    print(f"{'='*30}")
    # Affichage des informations de l'élève
    print(f"Nom : {nom}")
    print(f"Prénom : {prenom}")
    print(f"Âge : {age}")
    print(f"Classe : {classe}")
    print(f"Établissement : {etablissement}")
    # Si l'établissement est privé, afficher le type de bourse
    if etablissement == 'privé' :
        print(f"Type de bourse : {bourse}")
    print(f"Frais totaux : {frais} FCFA")
    print("Statut : Inscription complète")
    
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
    
# Fonction de calcul détaillé des frais d'inscription
def calcul_detaille_fraie () :
    # Variables globales utilisées
    global classe, etablissement, bourse, frais
    # Message d'affichage du calcul détaillé des frais
    print("CALCUL DETAILLÉ DES FRAIS")
    print(f"{'='*25}")
    # Affichage des informations de l'élève
    print(f"classe : {classe}")
    print(f"Établissement : {etablissement}")
    # Affichage du type de bourse si l'établissement est privé
    if etablissement == 'privé' :
        print(f"Type de bourse : {bourse}")
    # Affichage du détail des frais
    print("\nDÉTAIL DES FRAIS :")
    print(f"- Frais de base : {'35000 FCFA' if etablissement == 'privé' else '0 FCFA'}")
    # Calcul de la réduction appliquée si l'établissement est privé
    if etablissement == 'privé' :
        reduction = 0.5 if bourse == "excellence" else 0.3 if bourse == "sociale" else 0.2 if bourse == "familiale" else 0
        print(f"- Réduction appliquée {'50%' if bourse == 'excellence' else '30%' if bourse == 'sociale' else '20%' if bourse == 'familiale' else '0%'} : - {reduction * 35000} FCFA")
        print(f"- Frais APE : 2000 FCFA")
        print("- Cantine : 1500 FCFA")
        print("- Transport : 1000 FCFA")
        # Affichage du total des frais à payer
        print(f"- Total à payer : {frais} FCFA")
    else :
        print(f"- Frais APE : 2000 FCFA")
        # Affichage du total des frais à payer
        print(f"- Total à payer : {frais} FCFA")
    
# Fonction d'affichage des statistiques générales
def statistique_generale () :
    # Message d'affichage des statistiques générales
    print("STATISTIQUES GÉNÉRALES")
    print(f"{'='*22}")
    # Affichage des différentes statistiques
    print(f"Nombre total d'inscrits : {nombre_total_inscrits}")
    print("Effectif par classe :")
    print(f"  6ème : {effectif_6eme} élèves")
    print(f"  5ème : {effectif_5eme} élèves")
    print(f"  4ème : {effectif_4eme} élèves")
    print(f"  3ème : {effectif_3eme} élèves")
    print(f"  2nde : {effectif_2nde} élèves")
    print(f"  1ère : {effectif_1ere} élèves")
    print(f"  Terminale : {effectif_terminale} élèves")
    # Affichage des recettes totales
    print(f"\nRecettes totales : {recettes_totales} FCFA")
    # Affichage de la répartition des bourses
    print("Répartition des bourses :")
    print(f"- Excellence : {bourse_excellence} élèves")
    print(f"- Sociale : {bourse_sociale} élèves")
    print(f"- Familiale : {bourse_familiale} élèves")
    print(f"- Aucune : {aucune_bourse} élèves")
     
# Variables globales initialisées
nombre_total_inscrits = 0
effectif_6eme = 0
effectif_5eme = 0
effectif_4eme = 0
effectif_3eme = 0
effectif_2nde = 0
effectif_1ere = 0
effectif_terminale = 0
recettes_totales = 0
bourse_excellence = 0
bourse_sociale = 0
bourse_familiale = 0
aucune_bourse = 0

nom = ""
prenom = ""
age = 0
classe = ""
etablissement = ""
bourse = ""
frais = 0

# Boucle principale du programme
while True:
    # Appel de la fonction d'affichage du menu
    afficher_menu()
    # Lecture du choix de l'utilisateur
    choix = input("\nVotre choix : ")
    print()
    # Exécution de l'option choisie
    if choix == "1":
        # Apel de la fonction d'inscription
        inscrire_eleve()
    elif choix == "2":
        # Apel de la fonction de consultation
        consulter_eleve()
    elif choix == "3":
        # Apel de la fonction de modification
        modifier_inscription()
    elif choix == "4":
        # Apel de la fonction de calcul détaillé des frais
        calcul_detaille_fraie()
    elif choix == "5":
        # Apel de la fonction des statistiques générales
        statistique_generale()
    elif choix == "6":
        # Message pour quitter le programme
        print("Merci d'avoir utilisé le gestionnaire d'inscription !\n")
        break
    else:
        # Message d'erreur pour un choix invalide
        print("Choix invalide ! Veuillez réessayer.")