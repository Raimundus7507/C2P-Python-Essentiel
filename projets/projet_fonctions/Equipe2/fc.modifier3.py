    global nom,prenom,age,classe,etablissement,bourse,frais_total
    nouveau_nom = input(f"Nouveau Nom : ({nom})") or nom
    nouveau_prenom = input("fNouveau Prenom : ({prenom})") or prenom
    #change de l'age
    while True:
        try:
            nouveau_age = int(input(f"Nouveau Age : ({age})"))
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
    nouveau_classe = input(f"Nouvelle  Classe : ({classe})") or classe
    nouveau_etablissement = input(f"Nouvelle Etablissement : ({etablissement}) ") or etablissement
    nouveau_bourse = input(f"Nouvelle bourse : ({bourse}) ") or bourse

    nom= nouveau_nom
    prenom = nouveau_prenom
    age = nouveau_age
    classe = nouveau_classe
    etablissement = nouveau_etablissement
    bourse = nouveau_bourse
    #clacul des frais
    frais_total = calcul_frais4()
    print("Information Modiféer avec succès")



