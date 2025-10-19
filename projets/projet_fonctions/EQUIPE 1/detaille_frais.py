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