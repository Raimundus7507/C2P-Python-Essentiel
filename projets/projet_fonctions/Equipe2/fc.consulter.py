nom = ""
    prenom = ""
    age = 0
    frais_total = 0
    classe = ""
    etablissement = ""
    bourse = ""
def consuter_eleve():
    global  nom,prenom,age,classe,etablissement,bourse,frais_total
    #verifier si un eleve est inscrit
    if nom  "":
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
        print("Inscription compléte")
    else:
        print("Inscription incompléte")

