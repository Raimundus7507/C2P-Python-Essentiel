# Message d'accueil
print("=" * 40)
print("🎉 CRÉATION DE VOTRE PROFIL UTILISATEUR 🎉")
print("=" * 40)
print("\n 👋 Bonjour ! Créons ensemble  votre profil personnel.\n")

# Création du profil d'utilisateur 
fullName = str(input("📝 Veuillez saisir votre nom complet : "))
print(f"✅ Parfait {fullName} !\n")

age = int(input("Quel est votre âge ? : "))
print(f"✅ Âge enrégistré : {age} ans\n")

ville = str(input("🏙 Dans quelle ville habitez-vous ? "))
print(f"✅ Ville enrégistreé : {ville}\n")

# Configuration de mot de passe
print("=" * 40)
print("🔐 CONFIGURATION DE VOTRE MOT DE PASSE")
print("=" * 40)

password = str(input("🔑 Créer un mot de passe sécurisé (minimum 8 caractères) : "))
while len(password) < 8 :
        password = input(f"🔑 Mot de passe iinvalide. Créer un mot de passe sécurisé (minimum 8 caractères) : ")
print(("✅ Mot de passe accepté !"))

confirm = str(input("🔑 Confirmez votre mot de passe : "))
while password != confirm :
        str(input("🔑 Mot de passe de confirmation incorrecte. Réessayer : "))
print("✅ Mot de passe confirmé avec succès !\n")

recuperation1 = str(input("🔐 Premier mot de récupération : "))
recuperation2 = str(input("🔐 Deuxième mot de récupération : "))
# Validation si recuperation1 != recuperation2
if recuperation1 != recuperation2 :
        print("✅ Mot de récupération enrégistrés !\n")

# Message de félicitation
print("=" * 40)
print("🎉 PROFIL CRÉÉ AVEC SUCCES ! 🎉")
print("=" * 40)

# Connection
print("🔐 Veuillez maintenant vous connecter pour accéder à votre profil.\n")

nb_tentative = 1
while nb_tentative <= 3:
        username = str(input("Nom d'utilisateur : "))
        mot2pass = str(input("Mot de passe : "))

        if username == fullName and password == mot2pass :
                nb_tentative = 4 # Juste un nombre stristement supérieur à 3
        else :
              nb_tentative += 1  
              print("\nNom d'utilisateur ou mot de passe incorrect. Réessayez.\n ")

if username == fullName and password == mot2pass :
    print(f"\n✅ CONNEXION RÉUSSIE ! Bienvenue {fullName} ✅\n")

    # Affichage profil
    print("=" * 40)
    print("📔 VOTRE PROFIL PERSONNEL")
    print("=" * 40)
    print(f"👤 Nom   : {fullName}")
    print(f"🎂 Âge   : {age} ans")
    print(f"🏙  Ville : {ville}")
    print("🔐 Compte sécurisé avec mots de récupération.")
    print("\n Ce service est conçu pour vous offrir une expérience simple et efficace.")
    print(f"Nous sommes ravis de vous compter parmi nos utilisateurs {fullName}.\n")
    print("=" * 40)
else :        
    print("=" * 70)                
    print("🚫  Votre compte a été bloqué suite à trois tentatives invalides. 🚫")
    print(" \tVeuillez contacter le service client.")
    print("=" * 70)
print("\n Merci d'utiliser notre système ! 🙂\n")