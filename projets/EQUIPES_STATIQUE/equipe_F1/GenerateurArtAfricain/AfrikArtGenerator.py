# importation de la biblio de code pays
import pycountry

# Message d'acceuil

print("🌍=== AFRIKART GENERATOR ===")
print(" Bienvenue dans votre générateur d\'art africain ! ")
print()

# Questionnaire sur info personnelles
nom = str(input("Quel est votre nom ? " ))
pays = str(input(" Dans quel pays vivez-vous ? "))
ville = str(input("Dans quelle ville ?" ))
age = int(input("Quel est votre âge ? "))
langueParlée = input(str(" Quelles langue parlez-vous le mieux ? "))
platPréféré = input(str("Quel est votre plat préféré ?" ))

# Recherche du pays dans la base ISO 3166-1
nomPays = pays
pays = pycountry.countries.get(name = pays)
if pays:
    codePays = pays.alpha_2
else:
    codePays = "xx"

# Sortie 
print(f" {codePays} Ah ! Vous venez du {nomPays} !")
print(f"Bonjour {nom} de {ville} !")

# Récapitulatif
print("=== INFORMATION RÉCAPITULATIVES ===")
print(f"👤 Nom : {nom}")
print(f"🌍 Pays : {nomPays}")
print(f"🏙 Ville : {ville}")
print(f"🎂 Âge : {age}")
print(f"🗣️ Langue : {langueParlée}")
print(f"🍽️ Plat préférée : {platPréféré}")
print()

# Affichage de dessin du drapeau du pays 
print(f"{codePays}  DRAPEAU DU PAYS   {codePays}")
print()
if nomPays in ("Togo", "togo", "TOGO"): 
    # Au fait je me demand esi c'est possible de creer une biblio qui va 
    # contenir les drapeaux de tout les pays qu'in aura a dessiner nous même
    # pour le moment on a que pour le togo 
    print("🟥"*5 + "🟩"*10)
    print("🟥"*1 + "⭐"+ "🟥"*3 + "🟨"*10)
    print("🟥"*5 + "🟩"*10)
    print("🟥"*5 +  "🟨"*10)
    print("🟩"*15)

else:
    print("Oups")
    print(f"Nous ne disposons pas encore du drapeau de {nomPays} dans notre base 😅")

#Création des motifs si la personne le souhaite
print()
print(f"{nom}, voulez-vous créer des motifs artistiques ?")
continuer = input("Tapez 'oui' pour continuer : ")


if continuer in ('oui', 'Oui', 'OUI'):
    print("")
    while 1:
        print("=== GÉNÉRATEUR DE MOTIFS ===")
        print("Choisissez votre forme : ")
        print("1. Triangle")
        print("2. Rectangle")
        print("3. Pyramide")
        print("4. Pyramide inversée")
        print()
        choix = int(input("Votre choix (1-4) : "))

        #Construction du motif selon le choix
        # Réalisation motif 1
        if choix == 1:
            hauteur = int(input(f"Hauteur du triangle (3 - 10) : "))
            caractere = input("Caractère à utiliser (*, #, @, etc.) : ")
            for i in range(hauteur + 1):
                print(i * caractere)

        # Réalisation motif 2
        elif choix == 2:
            while 1:
                longueur = int(input(f"Longueur du rectangle (3 - 10) : "))
                largeur = int(input("Largeur du rectangle (3 - 10): "))
                if longueur < largeur:
                    print("La longueur doit être supérieure à la largeur.")
                else:
                    break
            caractere = input("Caractère à utiliser (*, #, @, etc.) : ")
            for i in range (largeur):
             print(caractere * longueur)

        # Réalisation motif 3
        elif choix == 3:
            hauteur = int(input(f"Hauteur de la pyramide (3 - 10) : "))
            caractere = input("Caractère à utiliser (*, #, @, etc.) : ")
            for i in range(1 ,hauteur + 1):
                print(" " * (hauteur - i) + caractere * (2 * i - 1))

        # Réalisation motif 4
        elif choix == 4:
            hauteur = int(input(f"Hauteur de la pyramide inversée (3 - 10) : "))
            caractere = input("Caractère à utiliser (*, #, @, etc.) : ")
            for i in range(hauteur + 1,0 ,-1):
                print(" " * (hauteur - i) + caractere * (2 * i -2 ))
        #Message pour valeur hors plage
        elif choix not in (1, 2, 3, 4):
            print()
            print("Choix invalide\n")

        #Message de fin après création du motif
        print()
        print(f"Magnifique création, {nom} !")
        continuer = input("Voulez-vous créer un autre motif ? (oui/non) : ")
        if continuer in ('non', 'Non', 'NON'):
            break

#Message de remerciement
print
print("Merci d'avoir utilisé Afrikart Generator !")
print("Vive l'Afrique et sa créativité !")