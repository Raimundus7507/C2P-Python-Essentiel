# Affichages de message de l'utilité du programme
print(f'\n{"=" * 43}')
print("🎉 CREATION DE VOTRE PROFILE UTILISATEUR 🎉")
print('='*43)

# Affichage du message de bienvenue
print("\n👋🏾 Bonjour ! Créons ensemble votre profil personnel.\n")

# Collecte des informations
nomComplet = input('👤 Veuillez saisir votre nom complet : ')
print(f'✅ Parfait {nomComplet} !\n')

age = int(input('🎂 Quel est votre âge ? : '))
print(f'✅ Age enrégistré : {age} ans\n')

residence = input('🌃 Dans quelle ville habitez-vous ? : ')
print(f'✅ Ville enrégistrée : {residence}\n')

# Informations sur la création du mot de passe
print('='*42)
print('🔐 CONFIGURATION DE VOTRE MOT DE PASSE 🔐')
print('='*42)

# Création du mot de passe
motDePasse = input('\n🔑 Créez un mot de passe sécurisé (minimum 8 caractères) : ')
while len(motDePasse) < 8:
    print('Votre mot de passe doit dépasser 8 caractères')
    motDePasse = input('🔑 Créez un mot de passe sécurisé (minimum 8 caractères) : ')
print('✅ Mot de passe accepté !')

# Confirmation du mot de passe
confirMotDePasse = input('\n🔑 Confirmez votre mot de passe : ')
while confirMotDePasse != motDePasse:
    confirMotDePasse = input('🔑 Mot de passe incorrect saisissez le meme qu\'à la création : ')
print('✅ Mot de passe confirmé avec succès !\n')

# Création de mots de récupération
motConfir1 = input('🔐 Premier mot de récupération : ')
motConfir2 = input('🔐 Deuxième mot de récupération (différent du premier) : ')
while motConfir1 == motConfir2:
    print('La deuxième mot de confirmation doit etre differente de la première')
    motConfir2 = input('🔐 Deuxième mot de récupération (différent du premier) : ')
print('✅ Mots de récupération enregistrés !\n')

# Affichage d'un message à propos de profile créer
print('='*32)
print('🎉 PROFILE CRÉE AVEC SUCCÈS ! 🎉')
print('='*32)

print('\n🔐 Veuillez maintenant vous connecter pour accéder à votre profil.\n')

# Connexion à votre profile créer et Vérification du nom et du mot de passe
nbTentatives = 0
while nbTentatives < 3:
    connexionNom = input('Nom d\'utilisateur : ')
    connexionMotDePasse = input('Mot de passe : ')
    if connexionMotDePasse == motDePasse and connexionNom == nomComplet:
        nbTentatives = 3
    else:
        print('Nom d\'utilisateur ou mot de passe incorrect. Veuillez réessayer.\n')
        nbTentatives += 1

# Recommencer la connexion si le mot de passe ou le nom n'est pas correct
if connexionMotDePasse == motDePasse and connexionNom == nomComplet:
    print(f'\n✅ CONNEXION RÉUSSIE ! Bienvenue {connexionNom} ! ✅')

    # Affichage du profil personnel
    print(f'\n{"=" * 30}')
    print('📋 VOTRE PROFIL PERSONNEL 📋')
    print('=' * 30)
    print(f'👤 Nom : {nomComplet}')
    print(f'🎂 Age : {age} ans')
    print(f'🌃 Ville : {residence}')
    print('🔐 Compte sécurisé avec mots de récuperation')
    print(f'{"=" * 44}')
else:
    print(f'\n{"=" * 56}')
    print('❌ TROP DE TENTATIVES. VOTRE COMPTE VIENS D\'ÊTRE BLOQUÉ. ❌\nVEUILLEZ CONTACTER LE SERVICE CLIENT POUR PLUS D4INFORMATIONS.')
    print(f'{"=" * 56}')

print('\nMerci d\'utilisé notre système ! 🙂')