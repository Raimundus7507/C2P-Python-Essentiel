print("=========================================")
print("🎉 CRÉATION DE VOTRE PROFIL UTILISATEUR 🎉")
print("=========================================\n")

print("👋 Bonjour ! Créons ensemble votre profil personnel.\n")

nom = input("📝 Veuillez saisir votre nom complet :")
print(f"✅ Parfait {nom}!\n")

age = int(input("🎂 Quel est votre âge ? :"))
print(f"🎉 Vous avez {age} ans, c'est super!\n")

ville = input("🏙️ Dans quelle ville habitez-vous ? :")
print(f"🏡 Vous habitez à {ville}, C'est enregistré\n")

print("=========================================")
print("🔐 CONFIGURATION DE VOTRE MOT DE PASSE")
print("=========================================\n")

password = input("🔑 Créez un mot de passe sécurisé (minimum 8 caractères) : ")
if len(password) < 8:
        print("❌ Mot de passe trop court, veuillez réessayer.")
else:
        print("✅ Mot de passe créé avec succès !")

print("\nVeuillez creer un mot de recuperation :")
input("Appuyez sur Entrée pour continuer...")

while True:
    premiermot = input("\n🔐 Premier mot de récupération :")
    deuxiememot = input("Deuxième mot de récupération (différent du premier) :")
    if premiermot and deuxiememot and premiermot != deuxiememot:
        print("✅ Mots de récupération enregistrés !\n")
        break
    else:
        print("❌ Les mots doivent être différents et non vides. Veuillez réessayer.")

print("=========================================")
print("🎉 PROFIL CRÉÉ AVEC SUCCÈS ! 🎉")
print("=========================================\n")

print("🔐 Veuillez maintenant vous connecter pour accéder à votre profil.\n")

attempts = 3
while attempts > 0:
    username = input("Nom d'utilisateur :")
    motdepasse = input("Mot de passe :")
    if username == nom and motdepasse == password:
        print(f"\n✅ CONNEXION RÉUSSIE ! Bienvenue {nom}! ✅")
        input("Appuyez sur Entrée pour continuer...\n")

        print("=========================================")
        print("📋 VOTRE PROFIL PERSONNEL")
        print("=========================================\n")
        print(f"👤Nom : {nom}")
        print(f"🎂Âge : {age}")
        print(f"🏡Ville : {ville}")
        print("=========================================\n")
        print("Merci d'avoir utilisé notre service de création de profil utilisateur. À bientôt ! 👋")
        break
    else:
        attempts -= 1
        print(f"❌ Identifiants incorrects, veuillez réessayer. ({attempts} tentatives restantes)")
        if attempts == 0:
            print("\n🔐 Vous avez épuisé vos tentatives. Veuillez récupérer votre mot de passe.\n")
            input("Appuyez pour continuer...")
            premiermot1 = input("\n🔐 Premier mot de récupération :")
            deuxiememot2 = input("Deuxième mot de récupération :")
            if premiermot1 == premiermot and deuxiememot2 == deuxiememot:
                print(f"\n✅ RÉCUPÉRATION RÉUSSIE, Votre mot de passe est {password}! Bienvenue {nom}! ✅")
                input("Appuyez sur Entrée pour continuer...\n")

                print("=========================================")
                print("📋 VOTRE PROFIL PERSONNEL")
                print("=========================================\n")
                print(f"👤Nom : {nom}")
                print(f"🎂Âge : {age}")
                print(f"🏡Ville : {ville}")
                print("=========================================\n")
                print("Merci d'avoir utilisé notre service de création de profil utilisateur. À bientôt ! 👋")
                break
            else:
                print("❌ Mots de récupération incorrects. Accès refusé.")