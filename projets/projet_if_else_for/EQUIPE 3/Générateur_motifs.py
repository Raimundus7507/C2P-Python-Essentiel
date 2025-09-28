# Générateur de motif visuel
prenom = input("Entrez votre prénom : ")
print(f"\nBienvenue {prenom} dans ce générateur de motifs visuels ")
#Affichage du Menu
print("--"*55)
Menu = """📋 MENU PRINCIPAL\n
1. 🟦 Rectangle d'étoiles
2. 🔢 Triangle de nombres
3. 🔺 Pyramide centrée
4. ♟ Damier alternant
5. ✖ Table de multiplication visuelle
6. 🔻 Pyramide renversée
7. 💠 Losange"""
print(Menu)
print("--"*55)

Remerciements = f"\n🎊 Merci {prenom} d'avoir utilisé notre générateur de motif visuel. A plus 👋"

choix = int(input("🔀 Choisir le motif à afficher (1 à 7) : "))
print()

# Premier cas : Le rectangle d'étoiles

if choix == 1:
    print("Vous avez choisi le rectangle d'étoiles 🟦\n")
    L = int(input("Entrez la largeur du rectangle : ")) # L étant la largeur du rectangle d'étoiles
    H = int(input("Entrez la hauteur du rectangle : ")) # H étant la hauteur du rectangle d'étoiles
    print()
    for i in range(H):
        for j in range(L):
            print("⭐", end="")
        print()
    print(Remerciements)

# Second cas : Le triangle de nombres

elif choix == 2:
    print("Vous avez choisi le triangle de nombres 🔢\n")
    T_tri = int(input("Entrez la taille du triangle de nombres : ")) # T_tri est une variable qui correspond à la taille du triangle
    print()
    for i in range(1,T_tri+1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()
    print(Remerciements)

# Troisième cas : La pyramide centrée

elif choix == 3:
    print("Vous avez choisi la pyramide centrée 🔺\n")
    H_pyra = int(input("Entrez la hauteur de la pyramide : ")) #H_pyra désigne la hauteur de la pyramide
    print()
    for i in range(H_pyra):
        etoile = 2 * i + 1
        espace = (H_pyra - i - 1) * 2
        print(" " * espace + "⭐" * etoile, end="")
        print()
    print(Remerciements)

# Quatrième cas : Le damier alternant

elif choix == 4:
    print("Vous avez choisi le damier alternant ♟\n")
    T_Dami = int(input("Entrez la taille du damier alternant : ")) # T_Dami désigne la taille du Damier
    print()
    if T_Dami < 2:
        print("Vous devez entrer un nombre supérieur ou égal à 2 pour pouvoir afficher un Damier alternant")
    else:
        for ligne in range(T_Dami):
            for colonne in range(T_Dami):
                if (ligne + colonne) % 2 == 0:
                    print("⬜", end=" ")
                else:
                    print("⬛", end=" ")
            print()
    print(Remerciements)

# Cinquième  cas : La table de multiplication visuelle

elif choix == 5:
    print("Vous avez choisi la table de multiplication visuelle ✖\n")
    Num = int(input("Entrez un numéro de la table de multiplication : ")) # Num désigne le numéro de la table de multiplication
    Lim = int(input("Entrez la limite de la table de multiplication : ")) # Lim désigne la limite de la table de multiplication
    print()
    for i in range(1,Lim+1):
        print(f"{Num} x {i} = {Num*i:<3}  {(Num*i)* " ●"}")
    print(Remerciements)

# Sixième cas : La pyramide renversée

elif choix == 6:
    print("Vous avez choisi la pyramide renversée 🔺\n")
    h_pyra = int(input("Entrez la hauteur de la pyramide : "))  # h_pyra désigne la hauteur de la pyramide renversée
    print()
    for i in range(h_pyra, -1, -1):
        etoiles = 2 * i + 1
        espaces = (h_pyra - i + 1) * 2
        print(" " * espaces + "⭐" * etoiles, end="")
        print()
    print(Remerciements)

# Dernier cas : Le losange

else:
    print("Vous avez choisi le losange 💠\n")
    longueur = int(input("Entrez la longueur d'un côté du losange : "))
    for i in range(longueur):
        element = (2 * i + 1) * "✨"
        espace1 = (longueur - i - 1) * 2
        print(" " * espace1 + element, end="")
        print()
    for i in range(longueur-2,-1,-1):
        element = (2 * i + 1) * "✨"
        espace2 = (longueur - i - 1) * 2
        print(" " * espace2 + element, end="")
        print()
    print(Remerciements)