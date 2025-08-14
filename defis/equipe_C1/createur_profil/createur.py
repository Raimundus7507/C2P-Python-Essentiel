print("Bienvenue dans le createur de profil personnel de Jean Luc et Vianel,"
"Afin de mieux vous connaitre, nous allons vous poser quelques questions.")

nom = input("Quel est votre nom complet?")
age = int(input("Quel age avez vous?"))
ville = input("Dans quelle ville habitez vous?")
couleur = input("Quelle est votre couleur preferer?")
plat = input("Quel est votre plat preferer?")
sport = input("Quel sport pratiquez vous?")
metier = input("Quel metier voulez vous faire?")
objectif = input("Quel est votre objectif cette annee?")
livre = input("Quel est votre livre preferer?")
musique = input("Quel type de musique aimez vous?")
weekend = input("Que faites vous le weekend?")



print("=================================================")
print("VOTRE PROFIL PERSONNEL")
print("=================================================\n")
print("Nom :", nom)
print("Age :", age, "ans")
print("Ville :", ville)

print("\nPREFERENCE")
print("Couleur :", couleur)
print("Plat :", plat)
print("Sport :", sport)
print("Musique :", musique)

print("\nPROJETS ET AMBITIONS")
print("Metier Souhaite :", metier)
print("Objectif 2025 :", objectif)

print("\nLOISIRS")
print("Lecture :", livre)
print("weekend :", weekend)

print(nom,"votre profil est maintenant cree! Vous etes une personne de", age,"ans", "passionne par le developpement web, Congrats.")