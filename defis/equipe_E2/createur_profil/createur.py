print("Bienvenu dans le Créateur de Profil Personnel \n"
      "Je vais vous poser quelques questions pour mieux vous connaître \n"
      "voici quelques questions de base")

#informations de base
nom = str(input(print("Quel est votre nom complet ?")))
age = int(input(print("Quel âge avez-vous ?")))
ville = str(input(print("Dans quelle ville habitez-vous ?")))

print("Nous allons maintenant vous poser des questions sur vos préférences")

#Préférences
couleur_prefere = str(input(print("Quelle est votre couleur préférée ?")))
plat = str(input(print("Quel est votre plat favori ?")))
sport = str(input(print("Quel Sport pratiquez-vous ?")))

print("Place maintenant aux projets")

#Projets
metier = str(input(print("Quel métier voulez-vous faire ?")))
objectif = str(input(print("Que est votre objectif cette année ?")))
livre = str(input(print("Quel est votre livre préféré ?")))
print("Parlons mainenant des loisirs")

#loisirs
musique = str(input(print("Quel type de musique aimez-vous ?")))
weekend = str(input(print("Que faites-vous les weekend ?")))
print(" ")
print(" ")

#affichage
print("================================================ \n"
      "          VOTRE PROFIL PERSONNEL                 \n"
      "================================================ ")
print(" ")
print(f'Nom : {nom}')
print(f'Age : {age} ans')
print(f'Ville : {ville}')
print(" ")
print("PREFERENCES")
print(f'Couleur : {couleur_prefere}')
print(f'Plat : {plat}')
print(f'Sport : {sport}')
print(f'Musique : {musique}')
print(" ")
print("PROJETS ET AMBITIONS")
print(f'Métier souhaité : {metier}')
print(f'Objectif 2024 : {objectif}')

print("LOISIRS")
print(f'Lecture : {livre}')
print(f'Weekend : {weekend}')
print("")
print(f'{nom}, votre profil est maintenant créé !\n'
      f'Vous êtes une personne de {age} ans passionnée par le développement. ')