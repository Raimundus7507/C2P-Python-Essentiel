
print("Bienvenue dans le Créateur de Profil Personnel. Je vais vous poser quelques questions pour mieux vous connaître.\n")

# Saisie des informations personnels

nom = input('Quel est ton nom complet ')
age = int(input('Quel âge avez-vous ? '))
ville = input('Dans quelle ville habitez-vous ?')
couleur = input('Quelle est votre couleur préférée ? ')
plat = input('Quel est votre plat favori ? ')
sport = input('Quel sport pratiquez-vous ? ')
metier = input('Quel métier voulez-vous faire ? ')
objectif = input('Quel est votre objectif cette année ? ')
livre = input('Quel est votre livre préféré ? ')
musique = input('Quel type de musique aimez-vous ? ')
hobby = input('Que faites-vous le weekend ? \n')


# Affichage du profil

print('=' * 40)
print('\n       VOTRE PROFIL PERSONNEL              \n')
print('=' * 40)

print("Nom : ", nom)
print('Age : ', age)
print('Ville : ', ville + '\n')

# PRÉFÉRENCES

print('Couleur : ', couleur)
print('Plat : ', plat)
print('Sport : ', sport)
print('Musique : ', musique + '\n')

#PROJETS ET AMBITIONS

print('Métier souhaité : ', metier)
print('Objectif 2025 : ', objectif)

#LOISIRS

print('Lecture : ', livre)
print('Weekend : ', hobby + '\n' * 2)

#Message de fin

print(f'{nom}, votre profil est maintenant créé !\n Vous êtes une personne de {age} ans passionnée par {metier}')