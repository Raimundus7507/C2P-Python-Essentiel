# Affichage de l'utilité du programme
print('\n\tPROGGRAMME DE CALCUL DE LA SOMME DE 1 JUSQU\'A VOTRE NOMBRE\n')

# Saisie du nombre de l'utilisateur
nombre = int(input('Veuillez entrer votre nombre : '))

# Verification de la strict positivité du nombre et supérieur à 1
while nombre <= 1 :
    nombre = int(input('Saisie invalide ! Votre nombre dois etre > 1 : '))

# Traitement
compteur = 1
somme = 0
while compteur <= nombre :
    somme += compteur
    compteur += 1

# Affichage du résultat (La somme)
print(f'\n\tLa somme des nombre de 1 jusqu\'à {nombre} est : {somme}')