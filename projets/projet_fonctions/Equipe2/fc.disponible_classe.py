from ensembe_projet0 import nbre_totale_classe_5_eme

def verifier_disponibilite(classe):
    global nbre_totale_classe_6eme, nbre_totale_classe_5eme, nbre_totale_classe_4eme
    global nbre_totale_classe_3eme, nbre_totale_classe_2nde, nbre_totale_classe_1ere, nbre_totale_classe_terminale
    if classe == "6eme" and nbre_totale_classe_6eme >= 45:
        return False
    elif classe == "5eme" and nbre_totale_classe_5eme >= 45:
        return False
    elif classe == "4eme" and nbre_totale_classe_4eme >= 45:
        return False
    elif classe == "3eme" and nbre_totale_classe_3eme >= 45:
        return False
    elif classe == "2nde" and nbre_totale_classe_2nde >= 45:
        return False
    elif classe == "1ere" and nbre_totale_classe_1ere >= 45:
        return False
    elif classe == "terminale" andnbre_totale_classe_terminale >= 45:
        return False
    return True