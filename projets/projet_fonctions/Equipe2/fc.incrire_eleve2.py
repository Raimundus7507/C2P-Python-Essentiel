#variable globale
nbre_total_incris = 0
nbre_totale_classe_6_eme = 0
nbre_totale_classe_5_eme = 0
nbre_totale_classe_4_eme = 0
nbre_totale_classe_3_eme = 0
nbre_totale_classe_2_nde = 0
nbre_totale_classe_1_ere = 0
nbre_totale_classe_terminale = 0
recette_totale = 0
def incrire_eleve2():
    global nbre_total_incris, recette_totale
    global nbre_totale_classe_6_eme, nbre_totale_classe_5_eme, nbre_totale_classe_4_eme, nbre_totale_classe_3_eme
    global nbre_totale_classe_1_ere, nbre_totale_classe_2_nde, nbre_totale_classe_terminale
    global nom,prenom,age,classe,etablissement
    #information de la personne
    nom = input("Votre Nom :")
    prenom = input("Votre Prenom :")
    #boucle pour age
    while True:
        try :
            age = int(input("Votre Age :"))
            if age <10 or age >25:
                print("Age invalide !;Age compris entre 10 e 25 !")
                continue
            break
        except ValueError:
            print("Veuiler Entrer un nombre valide !")

    #boucle pour classe
    while True:
        classe = input("Votre Classe :(4eme,5eme....")
        if classe == "6eme" or classe == "5eme" or classe == "4eme" or classe == "3eme" or classe == "2nde" or classe == "1ere"or classe == "terminale":
            break
        print("Votre Classe  est invalide !")
    #boucle pour etablisement
    while True:
        etablissement = input("Votre Etablissement :(public/privé/technique)")
        if etablissement == "public" or etablissement =="privé" or etablissement =="technique":
            break
        print("Votre Etablissement est invalide !")
    #boucle pour  bourse
    while True:
        bourse = input("Votre type de bourse :(Exellence/sociale/familiale/aucune") or "aucune"
        if bourse == "Exellence" or bourse =="sociale"  or bourse == "familiale" or bourse =="aucune":
            break
        print("Bourse invalide !, réessayez")
    #la mise ajours des nbr inscrit
    nbre_total_incris += 1
    #mise a jours effectife des classe
    if classe == "6eme":
        nbre_totale_classe_6_eme += 1
    elif classe == "5eme":
        nbre_totale_classe_5_eme += 1
    elif classe == "4eme":
        nbre_totale_classe_4_eme += 1
    elif classe == "3eme":
        nbre_totale_classe_3_eme += 1
    elif classe == "2nde":
        nbre_totale_classe_2_nde += 1
    elif classe == "1ere":
        nbre_totale_classe_1_ere += 1
    elif classe == "terminale":
        nbre_totale_classe_terminale += 1
    #clacul des frais
    frais = 0 #initialisation
    recette_totale += frais
    #or sujet{desoe},, atribuer un numero unique au eleve
    numero_eleve = nbre_total_incris
    #afficher recapituler
    print("********************************")
    print("\nElève inscrit avec succès !")
    print("********************************")
    print(f"Numero de eleve: {numero_eleve}")
    print(f"Nom et prenom  : {prenom}  {nom}")
    print(f"Age de l'élève: {age} ans")
    print(f"Elève en classe de {classe}")
    print(f"Type de Bourse: {bourse}")
    print(f"Etablissement: {etablissement}")
    print(f"frait a payer : {frais} FCFA ")

