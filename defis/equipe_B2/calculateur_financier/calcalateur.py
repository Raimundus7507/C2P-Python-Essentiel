# Affichage de l'utilité de notre programme
print('\tCALCULATEURD\'ECONOMIE - version Groupe B2')

# Lecture des informations
name = input('Veuillez entrer votre nom : ')
revenue = float(input('Veuillez entrer votre Revenue mention (FCFA) : '))
depence = float(input('Veuillez entrer Dépence mensuelles (FCFA) : '))

# Calcul de l'epargne de l'utilisateur
epargne = revenue - depence
taux_epargne = int(epargne * 100 / revenue)

# Affichage des informations
print('\n\t/!/!/! BILAN MENSUEL !\\!\\!\\')
print(name, ' - Revenues : ', revenue, ' FCFA')
print('Dépenses : ', depence, ' FCFA')
print('Economie : ', epargne, ' FCFA')
print('Votre taux d\'épargne : ', taux_epargne, '%')