# Accueil equipe2
print("🎨 GÉNÉRATEUR DE MOTIF")
print("="* 30)
print("1. ⬜ Rectangle d'étoiles")
print("2. 📐 Triangle de nombres")
print("3. 🔺 Pyramide centrée")
print("4. 🏁 Damier alternant")
print("5. ❎ Table de multiplication visuelle")
print("6. 🔻 Triangle inversé")
print("7. 🔷 Losange\n")

print("="* 30)
choix = int(input("\nVotre choix: "))
print("="* 30)

if choix == 1 :
    # Traitement rectangle d'étoiles
    print("\n⬜ RECTANGLE D'ETOILES")
    print("=" * 30)
    largeur = int(input("La largeur du rectangle: "))
    hauteur = int(input("La hauteur du rectangle: "))

    for i in range(hauteur) :
        for j in range(largeur) :
            print("*", end="")
        print()

if choix == 2 :
    # Tritement du triangle de nombres
    print("📐 TRIANGLE DE NOMBRES")
    print("=" * 30)
    taille = int(input("La taille du triangle: "))
    for i in range(1, taille+1) :
        for j in range(1, i+1) :
            print(f"{j}", end="")
        print()

if choix == 3 :
    # Traitement de la pyramide centrée
    print("🔺 PYRAMIDE CENTRÉE")
    print("=" * 30)
    hauteur = int(input("La hauteur de la pyramide: "))
    for i in range(1, hauteur+1) :
            print(" " * (hauteur - i) + "*" * (2 * i-1))

if choix == 4 :
    # Traitement du damier alternant
    print("🏁 DAMIER")
    print("=" * 30)
    taille_damier = int(input("La taille du damier: "))
    for i in range(1, taille_damier+1) :
         if i % 2 == 1 :
             for j in range(1, taille_damier+1) :
                 if j % 2 == 1 :
                     print("■ ", end="")
                 else :
                     print("□ ", end="")
             print()
         else :
             for j in range(1, taille_damier+1) :
                 if j % 2 == 1 :
                     print("□ ", end="")
                 else :
                     print("■ ", end="")
             print()

if choix == 5 :
    #Traitement de la table de multiplication
    print("❎ TABLE DE MULTIPLICATION")
    print("=" * 30)
    table = int(input("Table de: "))
    limite = int(input("Veuillez renseigner la limite: "))

    for i in range(1, limite+1) :
        print(f"{table} x {i} = {table * i}", end="\t")
        print("•" * (table * i))

if choix == 6 :
    # Traitement de la pyramide centrée
    print("🔻 TRIANGLE INVERSÉ")
    print("=" * 30)
    hauteur2 = int(input("La hauteur de la pyramide: "))
    for i in range(hauteur2, 0, -1) :
            print(" " * (hauteur2 - i) + "*" * (2 * i-1))

if choix == 7 :
    # Traitement du losange
    print("🔷 LOSANGE")
    print("=" * 30)
    mi_hauteur = int(input("La demi-hauteur du losange: "))
    for i in range(1, mi_hauteur+1) :
            print(" " * (mi_hauteur - i) + "*" * (2 * i-1))
    for i in range(mi_hauteur, 0, -1) :
            print(" " * (mi_hauteur - i) + "*" * (2 * i-1))

if choix not in (1, 2, 3, 4, 5, 6, 7) :
    print("🚫 OUPS CHOIX INDEFINI 🚫")
print("\n🎉 Merci d'avoir utilisé le générateur !")