# Affichage de l'utilité du programme
print("🎨 GÉNÉRATEUR DE MOTIFS")
print("========================")

# Affichage des motifs possibles
print("1. Rectangle d'étoiles")
print("2. Triangle de nombres")
print("3. Pyramide centrée")
print("4. Damier alternant")
print("5. Table multiplication visuelle")
print()

# Chix de l'utilisateur
choix = int(input("Votre choix : "))

# Rendu du motif en fonction du choix
if choix == 1:
    # Motifs du rectangle prise de longueur et hauteur
    print("\n🧱 RECTANGLE D'ÉTOILES")
    largeur = int(input("Largeur : "))
    hauteur = int(input("Hauteur : "))
    # Code du dessin
    for ligne in range(hauteur):
        for colonne in range(largeur):
            print(" * ", end="")
        print()
elif choix == 2:
    # Motifs du triangle prise de taille
    print("\n🔺 TRIANGLE DE NOMBRES")
    taille = int(input("Taille : "))
    # Code du dessin
    for ligne in range(1, taille + 1):
        for nombre in range(1, ligne + 1):
            print(nombre, end=" ")
        print()
elif choix == 3:
    # Motifs de la pyramide prise de hauteur
    print("\n🔺 PYRAMIDE CENTRÉE")
    hauteur = int(input("Hauteur : "))
    # Code du dessin
    for ligne in range(hauteur):
        espaces = hauteur - ligne - 1
        etoiles = 2 * ligne + 1
        for e in range(espaces):
            print(" ", end="")
        for s in range(etoiles):
            print("*", end="")
        print()
elif choix == 4:
    # Motif de damier prise de sa taille
    print("\n🏁 DAMIER")
    taille = int(input("Taille : "))
    # Code du dessin
    for ligne in range(taille):
        for colonne in range(taille):
            if (ligne + colonne) % 2 == 0:
                print("■", end=" ")
            else:
                print("□", end=" ")
        print()
elif choix == 5:
    # Motif de table de multiplication prise de table et limite
    print("\n📊 TABLE MULTIPLICATION VISUELLE")
    table = int(input("Table : "))
    limite = int(input("Limite : "))
    # Code du dessin
    for i in range(1, limite + 1):
        produit = table * i
        print(f"{table} x {i} = {produit}", end="   ")
        for point in range(produit):
            print("•", end="")
        print()
else:
    # Message d'erreur si l'utilisateur choisit une option invalide
    print("\n❌ Choix invalide. Veuillez sélectionner une option entre 1 et 5.")

# Message de fin de programme
print("\n🎉 Merci d'avoir utilisé le générateur !")