print("🌍 === AFRIKART GENERATOR ===")
print("Bienvenue dans votre générateur d'art africain !\n")

# Collecte des informations
nom = input("Quel est votre nom ? ")
pays = input("Dans quel pays vivez-vous ? ")
ville = input("Dans quelle ville ? ")
age = int(input("Quel est votre âge ? "))
langue = input("Quelle langue parlez-vous le mieux ? ")
plat = input("Quel est plat préféré ? ")

# Message personnalisé
if pays.lower() == "togo":
    print("\n🇹🇬 Ah ! Vous venez du Togo !")
print(f"Bonjour {nom} de {ville} !\n")

# Récapitulatif
print("=== INFORMATIONS RÉCAPITULATIVES ===")
print(f"👤 Nom : {nom}")
print(f"🌍 Pays : {pays}")
print(f"🌃 Ville : {ville}")
print(f"🎂 Âge : {age} ans")
print(f"🗣 Langue : {langue}")
print(f"🍽 Plat préféré : {plat}\n")

# Drapeau (symbolique)
print("🇹🇬 DRAPEAU DU TOGO 🇹🇬\n")
for i in range (1):
    print("🟥" * 9, "🟩" * 12)
    print("🟥" * 4,"☆", "🟥" * 4, "🟨" * 12)
    print("🟥" * 9, "🟩" * 12)
    print("🟨" * 21)
    print("🟩" * 21)

# Générateur de motifs
reponse = input(f"\n👋 {nom}, voulez-vous créer des motifs artistiques ?\nTapez 'oui' pour continuer : ").lower()

while reponse == "oui":
    print("\n🎨 === GÉNÉRATEUR DE MOTIFS ===")
    print("Choisissez votre forme :")
    print("1. Triangle🔺")
    print("2. Rectangle🟥")
    print("3. Pyramide🔺")
    print("4. Pyramide inversée🔻")

    choix = int(input("Votre choix (1-4) : "))
    caractere = input("Caractère à utiliser (*, #, 0, etc.) : ")

    print()
    if choix == 1:
        hauteur = int(input("Hauteur du triangle : "))
        for i in range(1, hauteur + 1):
            print(" " * (hauteur - i) + caractere * i)
    elif choix == 2:
        Longueur = int(input("Longueur du rectangle : "))
        Largeur = int(input("Largeur du rectangle : "))
        for _ in range(Largeur):
            print(caractere * Longueur)
    elif choix == 3:
        hauteur = int(input("Hauteur du Pyramide : "))
        for i in range(1, hauteur + 1):
            print(" " * (hauteur - i) + caractere * (2 * i - 1))
    elif choix == 4:
        hauteur = int(input("Hauteur du Pyramide renversé : "))
        for i in range(hauteur, 0, -1):
            print(" " * (hauteur - i) + caractere * (2 * i - 1))
    else:
        print("Choix invalide.")

    print(f"\n🎉 Magnifique création, {nom} !")
    reponse = input("Voulez-vous créer un autre motif ? (oui/non) : ").lower()

print("\nMerci d'avoir utilisé AfriKart Generator !")
print("🌍 Vive l'Afrique et sa créativité ! 🌍")
