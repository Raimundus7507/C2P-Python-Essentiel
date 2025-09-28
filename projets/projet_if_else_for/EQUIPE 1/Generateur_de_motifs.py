#Menu Principal

print("Generateur De Motifs")

print("=" * 30)
print("1. Rectangle d'etoiles ")
print("2. Triangle de nombres")
print("3. Pyramide centrée ")
print("4. Damier alternant")
print("5. Table multiplication visuelle")

#Choix de l'Utilisateur
choix = int(input("Veuillez Entrer Votre Choix :"))
#Rectangle d'etoiles
if choix == 1 :
    largeur = int(input("Largeur du Rectangle : "))
    hauteur = int(input("Hauteur du Rectangle : "))
    for i in range (hauteur) :
        for j in range (largeur) :
            print("*",end= "")
        print()

#Triangle de nombres
elif choix == 2 :
    taille = int(input("Taille du Triangle : "))
    for i in range (1, taille + 1) :
        for j in range (1, i + 1) :
            print(j, end= "")
        print()

#Pyramide centré
elif choix == 3 :
    hauteur = int(input("Hauteur du Pyramide : "))
    largeur_total = hauteur * 2 - 1
    for i in range (hauteur) :
        nbre_etoile = 2 * i + 1
        nbre_espace = (hauteur - i - 1)
        print(" " * nbre_espace, end= "")
        print("*" * nbre_etoile)

#Damier Alternant
elif choix == 4 :
    taille = int(input("Taille du Damier : "))
    for i in range (taille) :
        for j in range (taille) :
            if (i+j) % 2 == 0 :
                print(" ▪ ", end= "")
            else :
                print(" ▫ ", end= "")
        print()

#Table multiplication visuelle
elif choix == 5 :
    table = int(input("Entrer la table de multiplication : "))
    limite = int (input("Entrer la limite : "))
    for i in range (1, limite +1) :
        reponse = table * i
        point = "●" * reponse
        # Formatage
        print(f"{table : > 2} * {i:<2} = {reponse:< 4}  {point}")

print("Merci d'avoir utiliser le Générateur !")