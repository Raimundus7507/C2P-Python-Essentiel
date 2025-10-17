print("===========AFRIKART GENERATOR===========".center(50))
print("Bienvenue dans votre generateur d'arts Africaine !\n")

nom = input("Quel est votre nom ? ")
pays = input("Dans quel pays vivez-vous ? ")
ville = input("Dans quelle ville ?")
age = input("Quel est votre age ? ")
langue = input("Quelle langue parlez vous le mieux ? ")
plat = input("Quel est votre plat Africaine prefere ? ")

print(f"Ahh! Vous venez du {pays} !")
print(f"Bonjour {nom} du {ville} !\n")

print("===========INFORMATION RECAPITULATIVES===========")
print(f"Nom: {nom}")
print(f"Pays: {pays}")
print(f"Ville: {ville}")
print(f"Age: {age}")
print(f"Langue: {langue}")
print(f"Plat Préféré: {plat}\n")

for i in range(5):
    if i == 0:
        print("🟥⭐" + "🟩" * 7)  
    elif i == 1:
        print("🟥 " + "🟨" * 7)   
    elif i == 2:
        print("🟥 " + "🟩" * 7)   
    elif i == 3:
        print("🟥 " + "🟨" * 7)   
    elif i == 4:
        print("🟥 " + "🟩" * 7)   

print(f"{nom}, Voulez vous creez des motifs artistiques ?")
reponse = input("Tapez 'oui' pour continuer ou 'non' pour arreter : ")
if reponse == 'oui':
    reponse = input("Super ! Continuons à créer des motifs artistiques.\n")
    print("==========GENERATEUR DE MOTIFS===========")
    choissir = print("Choisissez votre forme :")
    triangle = print("1. Triangle")
    rectangle = print("2. Rectangle")
    pyramide = print("3. Pyramide")
    pyramideinverse = print("4. Pyramide Inverse\n")
    choix = input("Votre choix :")
    hauteur = input(f"Hauteur du {choix}(3-10) :")
    signe = input("Caractere a utiliser (*, #, @, etc.) :\n")
    if choix == '1':
        for i in range(int(hauteur)):
            print(signe * (i + 1))
    elif choix == '2':
        for i in range(int(hauteur)):
            print(signe * int(hauteur))
    elif choix == '3':
        for i in range(int(hauteur)):
            print(" " * (int(hauteur) - i - 1) + signe * (2 * i + 1))
    elif choix == '4':
        for i in range(int(hauteur)):
            print(" " * i + signe * (2 * (int(hauteur) - i) - 1))
        print(f"Magnifique Creation, {nom} !")
        
    answer = input("\nVoulez-vous continuer à créer des motifs ? (oui/non) : ")
    if answer == 'non':
        print("\nMerci d'avoir utilisé le générateur d'arts africains !")
        print("Vive l'Afrique et sa creativite")
elif reponse == 'non':
    print("Merci d'avoir utilisé le générateur d'arts africains !")
    print("Vive l'Afrique et sa creativite")
