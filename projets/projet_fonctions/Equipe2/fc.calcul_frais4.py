def calcul_frais4(classe,etablissement,bourse = "aucune"):
    global recette_totale
    #frais des etablissemtent
    if etablissement == "privé":
        frais_basique = 45000
    elif etablissement == "public":
        frais_basique = 40000
    elif etablissement == "technique":
        frais_basique = 35000
    else:
        frais_basique = 0
    #reduction grace au bource
    if bourse == "exellence":
        reduction = 0.5
    elif bourse == "sociale":
        reduction = 0.3
    elif bourse == "familiale":
        reduction = 0.2
    else:
        reduction = 0
    # le frais suplementaire APE
    frais_APE =2000
    frais_cantine = 2500
    frais_transport = 1000
    #calcul
    frais_totale = frais_basique * (1-reduction) +frais_APE + frais_cantine + frais_transport
    #recette totale
    recette_totale = frais_totale
    print("CALCUL DETTAILLER DES FRAIS")
    print("-----------------------------")
    print(f"Frais de base ({frais_basique}) :")
    print(f"Reduction Bourse ({int(reduction*100)}%) :")
    print(f"Frais APE ({frais_APE}) :")
    print(f"Frais cantine ({frais_cantine}) :")
    print(f"Frais transport ({frais_transport}) :")
    print(f"Totale a payer : {frais_totale}  FCFA ")
    return frais_totale

