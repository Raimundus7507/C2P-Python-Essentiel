#Message de bienvenue
print("\n🌍=== AFRIKART GENERATOR ===")
print("Bienvenue dans votre générateur d'art africain !\n")

#Récolte des infos personnelles
nom = input("👤 Quel est votre nom ? : ")
pays = input("🌍 Dans quel pays vivez-vous ? : ")
ville = input("🏙 Dans quelle ville ? : ")
age = input("🎂 Quel est votre âge ? : ")
langue = input("🗣️ Quelle langue parlez-vous le mieux ? : ")
plat = input("🍽️ Quel est votre plat africain préféré ? : ")

print(f"Ah ! Vous venez du {pays}\nBonjour Koffi de {ville} !")

#Affichage des infos récapitulatives
print("Nom : ")
print("Pays : ")
print("Ville : ")
print("Âge : ")
print("Langue : ")
print("Plat préféré :")
print("")

#Drapeau du pays

# importation de la biblio de code pays
import pycountry
print("")

# Recherche du pays dans la base ISO 3166-1
nomPays = pays
pays = pycountry.countries.get(name = pays)
if pays:
    codePays = pays.alpha_2
else:
    codePays = "xx"

# Affichage de dessin du drapeau du pays 
print(f"{codePays} DRAPEAU DU PAYS {codePays}")
if nomPays in ("Togo", "togo", "TOGO"): 
    # Au fait je me demand esi c'est possible de creer une biblio qui va 
    # contenir les drapeaux de tout les pays qu'in aura a dessiner nous même
    # pour le moment on a que pour le togo 
    print("🟥"*5 + "🟨"*10)
    print("🟥"*1 + "⭐"+ "🟥"*3 + "🟩"*10)
    print("🟥"*5 + "🟨"*10)
    print("🟥"*5 +  "🟩"*10)
    print("🟨"*15)

else:
    print("Oups")

#Création des motifs si la personne le souhaite
print(f"{nom}, voulez-vous créer des motifs artistiques ?")
creer = input("Tapez 'oui' pour continuer : ")

if creer in ('oui', 'Oui', 'OUI'):
    print("")
    while 1:
        print("=== GÉNÉRATEUR DE MOTIFS ===")
        print("Choisissez votre forme : ")
        print("1. Triangle")
        print("2. Rectangle")
        print("3. Pyramide")
        print("4. Pyramide inversée")
        print("")
        choix = int(input("Votre choix (1-4) : "))

        #Construction du motif selon le choix
        if choix == 1:
            hauteur = int(input(f"Hauteur du triangle (3 - 10) : "))
            caractere = input("Caractère à utiliser (*, #, @, etc.) : ")
            for i in range(hauteur + 1):
                print(i * caractere)
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
        elif choix == 3:
            hauteur = int(input(f"Hauteur de la pyramide (3 - 10) : "))
            caractere = input("Caractère à utiliser (*, #, @, etc.) : ")
            for i in range(hauteur + 1):
                print(i * caractere)
        elif choix == 4:
            hauteur = int(input(f"Hauteur de la pyramide inversée (3 - 10) : "))
            caractere = input("Caractère à utiliser (*, #, @, etc.) : ")
            for i in range(hauteur + 1,0 ,-1):
                print(i * caractere)
        #Message de fin après création du motif
        print("")
        print(f"Magnifique création, {nom} !")
        continuer = input("Voulez-vous créer un autre motif ? (oui/non) : ")
        if continuer in ('non', 'Non', 'NON'):
            break

#Message de remerciement
print("Merci d'avoir utilisé Afrikart Generator !")
print("Vive l'Afrique et sa créativité !")