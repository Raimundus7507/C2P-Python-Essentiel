# Pour supprimer les avertissements liés aux variables globales non utilisées
nombre_total_inscrits = 0
effectif_6eme = effectif_5eme = effectif_4eme = effectif_3eme = 0
effectif_2nde = effectif_1ere = effectif_terminale = 0
bourse_excellence = bourse_sociale = bourse_familiale = aucune_bourse = 0
recettes_totales = 0

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