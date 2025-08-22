# Affichage de l'utilité
print('\n\n\tTABLE DE MULTIPLICATION DE X\n\n')

# Saisie et verification d'entrée
nombre = int(input('Entrez la valeur de X : '))

# Verification du nombre saisie par l'utilisateur
while nombre < 1 or nombre > 10:
    nombre = int(input('Valeur incorrecte. Veuillez entrer une valeur de X entre 1 et 10.'))

# Traitement
compteur = 0
while compteur <= 10:
    print(f'{nombre} * {compteur} = {nombre * compteur}')
    compteur += 1