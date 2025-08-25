# Afficher message d'utilité de notre programme
print('\n\n=== COMPTEUR MAGIQUE ===\n')

# Affichage d'un meesage destiné à l'utilisateur sur ce que notre programme va faire
print('Comptage de 1 à 20 avec des règles spéciales...\n')

# Initialisation du nombre à 1
nombre = 1

# Traitement des conditions et affichage
for nombre in range(1, 20) :
    # Verifier si le nombre est un multiple de 3
    if nombre % 3 == 0 :
        continue
    # Verifier si le nombre est 13 pour passer
    elif nombre % 13 == 0 :
        print(f'{nombre} (nombre mystère - on ne fait rien)')
        pass
    # Verifier si le nombre est 17 pour s'arreter
    elif nombre == 17 :
        print('\nSTOP ! Nombre 17 trouvé - arrêt du compteur !')
        break
    # Si tous les coditions sont pas verifiers, afficher ce nombre
    else :
        if nombre % 3 == 2 :
            print(nombre)
        elif nombre == 1 :
            print(nombre)
        else :
            print(f'{nombre} ', end = '')
            print(f'({nombre - 1} ignoré - multiple de 3)') # Nombre multitle de 3