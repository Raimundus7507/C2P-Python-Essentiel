# Fonction de vérification de la saisi utilisateur
def verificator(messages, typ ):
    while True:
        try:
            retour = typ(input(messages))
            return retour
        except ValueError:
            print("❌Saisi invalide. Réessayez svp")
