# Affichage de l'utilité du message
print('\n\tPROGRAMME POUR CHERCHER UN NOMBRE COMPRIS ENTRE UN INTERVALLE\n\n')

# Prise du nombre de l'utilisateur
nombre = int(input('Veuillez entrer un nombre compris entre 10 et 20 : '))

# Verification du nombre dans nombre intervalle
while nombre < 10 or nombre > 20:
    if nombre < 10 :
        nombre = int(input('Plus petit : '))
    else :
        nombre = int(input('Plus grand : '))

# Affichage de message de félicitacione
print('\nFelicitations ta reponse est valide !!')