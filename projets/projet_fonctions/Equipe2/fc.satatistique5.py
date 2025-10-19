def statistique_eleve():
    global nbre_totale_inscris,recette_totale
    global nbre_totale_classe_6_eme,nbre_totale_classe_5_eme,nbre_totale_classe_4_eme
    global nbre_totale_classe_3eme, nbre_totale_classe_2nde, nbre_totale_classe_1ere,nbre_totale_classe_terminale
    global etablissement,bourse

    #affichage
    print("\nSTATISTIQUES DE L'ÉTABLISSEMENT")
    print("=================================")
    print(f"Nombre total d'élèves inscrits : {nbre_total_incris}\n")

    #Répartition  par classe
    print("Répartition par classe :")
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
    if bourse == "exellence":
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