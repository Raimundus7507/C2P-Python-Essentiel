# Messa de bienvenue
print("\n === CYBERGUARDIAN : TESTEZ VOTRE SÉCURITÉ NUMÉRIQUE ! ===\n")
print("Bienvenue ! Ce quiz va évaluer vos habitudes de cybersécurité. Répondez par 'oui' ou 'non' à chaque question.\n")

# Questions pour l'analyse
nombre_de_oui = 0

print('Question 1/5 : Utilisez-vous un mot de passe différent pour chaque compte ?')
reponse1 = input("Votre réponse : ")
if reponse1 in ("OUI" , "Oui" , "oui"):
    nombre_de_oui += 1
print("")

print('Question 2/5 :  Vérifiez-vous l\'URL avant de saisir vos informations personnelles ?')
reponse2 = input("Votre réponse : ")
if reponse2  in ("OUI" , "Oui" , "oui"):
    nombre_de_oui += 1
print("")

print('Question 3/5 : Activez-vous les mises à jour automatiques de sécurité ?')
reponse3 = input("Votre réponse : ")
if reponse3  in ("OUI" , "Oui" , "oui"):
    nombre_de_oui += 1
print("")

print('Question 4/5 : Évitez-vous de vous connecter sur des réseaux Wi-Fi publics pour des tâches sensibles ?')
reponse4 = input("Votre réponse : ")
if reponse4  in ("OUI" , "Oui" , "oui"):
    nombre_de_oui += 1
print("")

print('Question 5/5 : Utilisez-vous l''authentification à deux facteurs quand c''est possible ?')
reponse5 = input("Votre réponse : ")
if reponse5  in ("OUI" , "Oui" , "oui"):
    nombre_de_oui += 1
print("")

print("\n=== VOTRE PROFIL DE CYBERSÉCURITÉ\n")

# Analyse des résultats

if 4 <= nombre_de_oui <= 5:
    print("Cyber-Expert")
    print("Excellent niveau de sécurité.\n")
    if reponse1  in ("NON" , "Non" , "non"):
        print("Cependant, vous devez utilisez un mot de passe uniques pour chaque compte.ATTENTION !\n")
elif 2 <= nombre_de_oui <= 3:
    print("Utilisateur Prudent")
    print("Bonnes bases, quelques améliorations possibles.\n")
elif 0 <= nombre_de_oui <= 1:
    print("Cyber-Novice")
    print("Attention, des améliorations sont nécessaires.\n")
    if reponse5  in ("OUI" , "Oui" , "oui"):
        print("Cependant vous êtes à félliciter en raison de l''authentification à deux facteurs quand c''est possible. Vous êtes sur le bon chemin.\n")

# Affichage du résultat 
print(f"Score final : {nombre_de_oui}/5 - Continuez vos efforts.")

# Resultat personnalisé
if reponse1 in ("NON" , "Non" , "non"):
    print("Utilisez un mot de passe different pour chaque compte")
if reponse2 in ("NON" , "Non" , "non"):
    print (" Verifiez l\' URL avant de saisir vos informations personnelles")
if reponse3 in ("NON" , "Non" , "non"):
    print("Activez les mises à jour automatiques de sécurité")
if reponse4 in ("NON" , "Non" , "non"):
    print("Evitez de vous connectez sur les reseaux wifi publics pour les taches sensibles")
if reponse5 in ("NON" , "Non" , "non"):
    print("Utilisez l\'authentification à deux facteurs quand c\'est possible")
