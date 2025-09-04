# Importation des modules
import random # pour les choix aléatoire
import string # contient les caractères (A-Z, a-z, 0-9)

# Fonction pour générer le mot de passe
def generer_mot_de_passe (longueur = 12):
    # Tous les caractères possible
    caracteres = string.ascii_letters + string.digits + "@#$!&"
    # Génération de notre mot de passe
    motDePasse = ''.join(random.choice(caracteres) for choix in range(longueur))
    return motDePasse

for i in range(10):
    print(f'Votre mot de passe {i+1} --> {generer_mot_de_passe()}')