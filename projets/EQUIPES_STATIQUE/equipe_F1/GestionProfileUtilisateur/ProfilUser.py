# Importation de la bibliothéque qui gère les couleurs
           # Pour l'installer "pip install colorama" dans le shell
from colorama import Fore, Style

# Message d'accueil
print("=" * 40)
print("🎉 CRÉATION DE VOTRE PROFIL UTILISATEUR 🎉")
print("=" * 40)
print("\n 👋 Bonjour ! Créons ensemble  votre profil personnel.\n")

# Création du profil d'utilisateur 
fullName = str(input("📝 Veuillez saisir votre nom complet : "))
print(Fore.GREEN + f"✅ Parfait {fullName} !\n")      

age = int(input(Style.RESET_ALL + "Quel est votre âge ? : "))      # reinitialisation de la couleur
print(Fore.GREEN + f"✅ Âge enrégistré : {age} ans\n")

ville = str(input(Style.RESET_ALL + "🏙 Dans quelle ville habitez-vous ? "))
print(Fore.GREEN + f"✅ Ville enrégistreé : {ville}\n")

# Configuration de mot de passe
print(Style.RESET_ALL + "=" * 40)
print("🔐 CONFIGURATION DE VOTRE MOT DE PASSE")
print("=" * 40)
print()

password = str(input("🔑 Créer un mot de passe sécurisé (minimum 8 caractères) : "))
while len(password) < 8 :
        password = input(f"🔑 Mot de passe invalide. Créer un mot de passe sécurisé (minimum 8 caractères) : ")
print((Fore.GREEN + "✅ Mot de passe accepté !"))

confirm = str(input(Style.RESET_ALL + "🔑 Confirmez votre mot de passe : "))
while password != confirm :
        print(Fore.RED + "🔑 Mot de passe de confirmation incorrecte. Réessayer : ")
        confirm = str(input(Style.RESET_ALL + "🔑 Confirmez votre mot de passe : "))
print(Fore.GREEN + "✅ Mot de passe confirmé avec succès !\n")

recuperation1 = str(input(Style.RESET_ALL +"🔐 Premier mot de récupération : "))
recuperation2 = str(input("🔐 Deuxième mot de récupération : "))
# Validation si recuperation1 != recuperation2
while recuperation1 == recuperation2 :
        print(Fore.RED + "Erreur. Mots de récupération identiques.\n")
        recuperation2 = str(input(Style.RESET_ALL + "🔐 Deuxième mot de récupération : "))
print(Fore.GREEN + "✅ Mots de récupération enregistrés !\n")

# Message de félicitation
print(Style.RESET_ALL +"=" * 40)
print("🎉 PROFIL CRÉÉ AVEC SUCCES ! 🎉")
print("=" * 40)

# Connection
print()
print("🔐 Veuillez maintenant vous connecter pour accéder à votre profil.\n")

nb_tentative = 1
while nb_tentative <= 3:
        username = str(input(Style.RESET_ALL + "Nom d'utilisateur : "))
        mot2pass = str(input("Mot de passe : "))

        if username == fullName and password == mot2pass :
                nb_tentative = 4 # Juste un nombre strictement supérieur à 3
        else :
              nb_tentative += 1

              if   nb_tentative <= 3 : # Pour ne plus afficher le message après un 3ème essai invlide
                  print(Fore.RED + "\nNom d'utilisateur ou mot de passe incorrect. Réessayez.\n ")

if username == fullName and password == mot2pass :
    print(Fore.GREEN + f"\n✅ CONNEXION RÉUSSIE ! Bienvenue {fullName} ✅\n")

    # Affichage profil
    print(Style.RESET_ALL +"=" * 40)
    print("📔 VOTRE PROFIL PERSONNEL")
    print("=" * 40)
    print()
    print(f"👤 Nom   : {fullName}")
    print(f"🎂 Âge   : {age} ans")
    print(f"🏙  Ville : {ville}")
    print("🔐 Compte sécurisé avec mots de récupération.")
    print("\n Ce service est conçu pour vous offrir une expérience simple et efficace.")
    print(f"Nous sommes ravis de vous compter parmi nos utilisateurs {fullName}.\n")
    print("=" * 40)
else :        
    print("=" * 70)                
    print(Fore.RED  + "🚫  Votre compte a été bloqué suite à trois tentatives invalides. 🚫")
    print(Style.RESET_ALL +"=" * 70)

    # Récupération du compte
    print("\nVeuillez répondre correctement aux questions pour récupérer votre compte.\n")
    input("Appuyer sur Entrée pour continuer...\n ")

    mot2recuperation1 = input("Votre premier mot de récupération : ")
    mot2recuperation2 = input("Votre deuxième mot de récupération : ")

    if mot2recuperation1 == recuperation1 and mot2recuperation2 == recuperation2 :
        print(Fore.GREEN + f"\nBravo {fullName} !\n")
        print(Style.RESET_ALL + f"Votre nom d'utilisateur : {fullName}")
        print(f"Votre mot de passe : {password}\n")

        # Affichage profil
        print("=" * 40)
        print("📔 VOTRE PROFIL PERSONNEL")
        print("=" * 40)
        print()
        print(f"👤 Nom   : {fullName}")
        print(f"🎂 Âge   : {age} ans")
        print(f"🏙  Ville : {ville}")
        print("🔐 Compte sécurisé avec mots de récupération.")
        print("\n Ce service est conçu pour vous offrir une expérience simple et efficace.")
        print(f"Nous sommes ravis de vous compter parmi nos utilisateurs {fullName}.\n")
        print("=" * 40)
    else:
        print("=" * 70)
        print(Fore.RED + "\nMots de récupération incorrectes.")
        print(" Veuillez contacter le service client ou vous rendre à l'agence.")
        print(Style.RESET_ALL + "=" * 70)
           

print("\n Merci d'utiliser notre système ! 🙂\n")