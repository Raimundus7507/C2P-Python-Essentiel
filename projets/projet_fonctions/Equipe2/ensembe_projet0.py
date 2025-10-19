#afficher bienvenue
print("~"*56)
print("|| BIENVENUE DANS LA GESTION DES INSCRIPTIONS SCOLAIRE || ")
print("~"*56)
#creation du fonction qui affiche le menu
def afficher_menu():
    print("\n1.Inscrire un élève")
    print("2.Consulter les élèves actuels")
    print("3.Modifier les informations")
    print("4.Calcuer des frais")
    print("5.Voir les statistique de l'Etablissement")
    print("6.QUITTER")
#variable globale

#fonction inscrire
nbre_total_incris = 0
nbre_totale_classe_6_eme = 0
nbre_totale_classe_5_eme = 0
nbre_totale_classe_4_eme = 0
nbre_totale_classe_3_eme = 0
nbre_totale_classe_2_nde = 0
nbre_totale_classe_1_ere = 0
nbre_totale_classe_terminale = 0
recette_totale = 0


# --- Vérifier la disponibilité d'une classe ---
def verifier_disponibilite(classe):
    global nbre_totale_classe_6_eme, nbre_totale_classe_5_eme, nbre_totale_classe_4_eme
    global nbre_totale_classe_3_eme, nbre_totale_classe_2_nde, nbre_totale_classe_1_ere, nbre_totale_classe_terminale

    if classe == "6eme" and nbre_totale_classe_6_eme >= 45:
        return False
    elif classe == "5eme" and nbre_totale_classe_5_eme >= 45:
        return False
    elif classe == "4eme" and nbre_totale_classe_4_eme >= 45:
        return False
    elif classe == "3eme" and nbre_totale_classe_3_eme >= 45:
        return False
    elif classe == "2nde" and nbre_totale_classe_2_nde >= 45:
        return False
    elif classe == "1ere" and nbre_totale_classe_1_ere >= 45:
        return False
    elif classe == "terminale" and nbre_totale_classe_terminale >= 45:
        return False
    return True


def incrire_eleve2():
    global nbre_total_incris, recette_totale
    global nbre_totale_classe_6_eme, nbre_totale_classe_5_eme, nbre_totale_classe_4_eme, nbre_totale_classe_3_eme
    global nbre_totale_classe_1_ere, nbre_totale_classe_2_nde, nbre_totale_classe_terminale
    global  nom,prenom,age,classe,etablissement,bourse,frais_total
    #frais_total = calcul_frais4(classe,etablissement,bourse)
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
            if not verifier_disponibilite(classe):
                print(f"La classe {classe} est deja  pleine")
                continue
            break
        except ValueError:
            print("Veuiler Entrer un nombre valide !")

    #boucle pour classe
    while True:
        classe = input("Votre Classe (4eme,5eme....terminale) :")
        if classe == "6eme" or classe == "5eme" or classe == "4eme" or classe == "3eme" or classe == "2nde" or classe == "1ere"or classe == "terminale":
            break
        print("Votre Classe  est invalide !")
    #boucle pour etablisement
    while True:
        etablissement = input("Votre Etablissement (public/privé/technique): ")
        if etablissement == "public" or etablissement =="privé" or etablissement =="technique":
            break
        print("Votre Etablissement est invalide !")
    #boucle pour  bourse
    while True:
        bourse = input("Votre type de bourse :(Exellence/sociale/familiale/aucune) : ")
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
    frais_total = calcul_frais4(classe,etablissement, bourse)
    recette_totale += frais_total
    #or sujet{desoe},, atribuer un numero unique au eleve
    numero_eleve = nbre_total_incris
    #afficher recapituler
    print("********************************")
    print("\nElève inscrit avec succès !")
    print("********************************")
    print(f"Numero de l'élève: {numero_eleve}")
    print(f"Nom et prenom  : {prenom}  {nom}")
    print(f"Age de l'élève: {age} ans")
    print(f" classe  :  {classe}")
    print(f"Type de Bourse: {bourse}")
    print(f"Etablissement: {etablissement}")
    print(f"frais a payer : {frais_total} FCFA \n")

#fonction frais
nom = ""
prenom = ""
age = 0
frais_total = 0
classe = ""
etablissement = ""
bourse = ""
def consuter_eleve():
    global  nom,prenom,age,classe
    global frais_total,etablissement,bourse
    #verifier si un eleve est inscrit
    if nom == "":
        print("\n Aucun élève incrit pour le moment")
        return
    print("===================================")
    print(" \nCONSULTATION DE L'ÉLÈVE ACTUEL")
    print("====================================")
    print(f"Nom : {nom}")
    print(f"Prénom : {prenom}")
    print(f"Âge : {age} ans")
    print(f"Classe : {classe}")
    print(f"Établissement : {etablissement}")
    print(f"Bourse : {bourse}")
    print(f"Frais totaux : {frais_total} FCFA")
    #verifier que si l'inscriotion est complet
    if 10 <= age  <= 25 and classe != "" and etablissement != "" and bourse != "":
        print("\nInscription compléte")
    else:
        print("Inscription incompléte")


def modifier_eleve():
    global nom,prenom,age,classe,etablissement,bourse,frais_total
    ancien_nom = nom
    ancien_prenom = prenom
    ancien_age = age
    ancienne_classe = classe
    ancien_etablissement = etablissement
    ancienne_bourse = bourse

    nouveau_nom = input(f"Nouveau Nom ({nom}):  ")
    nouveau_prenom = input(f"Nouveau Prenom ({prenom}):  ")
    #change de l'age
    while True:
        try:
            nouveau_age = input(f"Nouveau Age ({age}): ")
            if nouveau_age == "":
                nouveau_age = age
            else:
                nouveau_age= int(nouveau_age)
                if nouveau_age < 10 or nouveau_age > 25 :
                    print("Age ivalide !, Entrer age entre 10 et25")
                    continue
            break
        except ValueError:
            print("Erreur ! Enter une valeur valide a la norme")
    nouveau_classe = input(f"Nouvelle  Classe ({classe}) :")
    nouveau_etablissement = input(f"Nouvelle Etablissement  ({etablissement}) : ")
    nouveau_bourse = input(f"Nouvelle bourse ({bourse}) : ")
    #recette_totale -= frais_total
    nom = nouveau_nom
    prenom = nouveau_prenom
    age = nouveau_age
    classe = nouveau_classe
    etablissement = nouveau_etablissement
    bourse = nouveau_bourse
    #clacul des frais
    print("\nMODIFICATION DES INFORMATIONS")
    print("==============================")
    print("Nouveau nom :",nouveau_nom)
    print("Nouveau prenom :",nouveau_prenom)
    print("Nouvel age: ",nouveau_age)
    print("Nouvelle classe : ",nouveau_classe)
    print("Etablissement Actuel: ",nouveau_etablissement)
    print("Nouvelle bourse : ",nouveau_bourse)
    print("\nInformation Modiféer avec succès")
# fonctionfrais
def calcul_frais4(classe,etablissement,bourse = "aucune"):
    global recette_totale
    #frais des etablissemtent
    if etablissement == "privé":
        frais_basique = 45000
        frais_cantine = 1500
        frais_transport = 1000
        frais_APE = 2000
    elif etablissement == "public":
        frais_basique = 40000
        frais_cantine = 1000
        frais_transport = 2000
        frais_APE = 1500
    elif etablissement == "technique":
        frais_basique = 35000
        frais_cantine = 2000
        frais_transport = 1500
        frais_APE = 2500

    else:
        frais_basique = 0
        frais_cantine = 0
        frais_transport = 0
        frais_APE = 0
    #reduction grace au bource
    if bourse == "Exellence":
        reduction = 0.5
    elif bourse == "sociale":
        reduction = 0.3
    elif bourse == "familiale":
        reduction = 0.2
    else:
        reduction = 0
    # le frais suplementaire APE
    #frais_APE =2000
    #frais_cantine = 2500
    #frais_transport = 1000
    #calcul
    frais_totale = frais_basique * (1-reduction) +frais_APE + frais_cantine + frais_transport
    #recette totale
    return frais_totale

    print("CALCUL DETAILLE DES FRAIS")
    print("-----------------------------")
    print(f"Classe : {classe}")
    print(f"Etablissement : {etablissement}")
    print(f"type de Bourse: {bourse}")
    print("\nDETAILLE DES FRAIS")
    print(f"Frais de base  : {frais_basique}  FCFA")
    print(f"Reduction Bourse {int(reduction*100)}% : -{frais_basique* reduction} FCFA")
    print(f"Frais APE : {frais_APE} FCFA")
    print(f"Frais cantine : {frais_cantine} FCFA ")
    print(f"Frais transport  :  {frais_transport} FCFA ")
    print(f"Totale a payer : {frais_totale}  FCFA ")
    return frais_totale

#statistique
nbre_bourse_excellence = 0
nbre_bourse_sociale = 0
nbre_bourse_familiale = 0
nbre_bourse_aucune = 0
nbre_public = 0
nbre_prive = 0
nbre_technique = 0

def statistique_eleve():
    global nbre_totale_inscris,recette_totale,frais_totale
    global nbre_totale_classe_6_eme,nbre_totale_classe_5_eme,nbre_totale_classe_4_eme
    global nbre_totale_classe_3eme, nbre_totale_classe_2nde, nbre_totale_classe_1ere,nbre_totale_classe_terminale
    global etablissement,bourse

    #affichage
    print("\nSTATISTIQUES DE L'ÉTABLISSEMENT")
    print("=================================")
    print(f"Nombre total d'élèves inscrits : {nbre_total_incris}\n")

    #Répartition  par classe
    print("Répartition par classe :\n")
    print(f"- 6ème : {nbre_totale_classe_6_eme}")
    print(f"- 5ème : {nbre_totale_classe_5_eme}")
    print(f"- 4ème : {nbre_totale_classe_4_eme}")
    print(f"- 3ème : {nbre_totale_classe_3_eme}")
    print(f"- 2nde : {nbre_totale_classe_2_nde}")
    print(f"- 1ère : {nbre_totale_classe_1_ere}")
    print(f"- Terminale : {nbre_totale_classe_terminale}\n")

    #Répartition par  d’établissement
    print("Répartition par type d’établissement :")
    if etablissement == "public":
        print("- Public : 1 élève")
        print("- Privé : 0 élève")
        print("- Technique : 0 élève")
    elif etablissement == "privé":
        print("- Public : 0 élève")
        print("- Privé : 1 élève")
        print("- Technique : 0 élève")
    elif etablissement == "technique":
        print("- Public : 0 élève")
        print("- Privé : 0 élève")
        print("- Technique : 1 élève")
    else:
        print("Aucun établissement enregistré.\n")

    # --- Répartition par bourse ---
    print("\nRépartition par bourse :")
    if bourse == "Exellence":
        print("- Excellence : 1")
    elif bourse == "sociale":
        print("- Sociale : 1")
    elif bourse == "familiale":
        print("- Familiale : 1")
    elif bourse == "aucune":
        print("- Aucune : 1")
    else:
        print("Aucune bourse enregistrée.\n")

    # --- Recette totale ---
    print(f"\nRecette totale actuelle : {recette_totale} FCFA")
    print("=================================\n")
#boucle pour le numero 6
def menu_pricipal0():
    while True:
        try:
            afficher_menu()
            choix= input("\nVeiller enter votre choix :")
            #gestion des choix
            if choix == "1":
                incrire_eleve2()
            elif choix == "2":
                consuter_eleve()
            elif choix == "3":
                modifier_eleve()
            elif choix == "4":
                if classe== "" or etablissement == "":
                    print("Aucun eleve inscrit pour calculer les frais")
                else:
                    calcul_frais4(classe,etablissement,bourse)
            elif choix == "5":
                statistique_eleve()
            elif choix == "6":
                print("\n6MERCI D'AVOIR UTILISER LE GESTIONNAIRE")
                break
            else:
                print("choix invalide!..veillez Reessayer")
        except Exception as erreur:
             print("Erreur :",erreur)
menu_pricipal0()
