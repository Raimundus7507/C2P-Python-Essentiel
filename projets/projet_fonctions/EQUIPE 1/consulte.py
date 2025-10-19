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