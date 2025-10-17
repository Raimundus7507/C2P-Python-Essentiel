
print("")
# ============= QUIZ CYBERSECURITE ============
print("+++++++++++++  QUIZ CYBERSECURITE  ++++++++++++++++++++")
print("Bienvenu dans le quiz de cybersécurité")
print("Répondez par 'oui' ou 'non' aux questions suivantes : \n")

resultat_oui = 0

quiz_1 = input("1. utilisez-vous un mot de passe différent pour chaque compte ? : ")
if quiz_1 == "oui":
    resultat_oui = resultat_oui + 1

quiz_2 = input("2. Vérifiez-vous l'URL avant de saisir vos informations personnelles ?: ")
if quiz_2 == "oui":
    resultat_oui = resultat_oui + 1
    
quiz_3 = input("3. Activez-vous les mises à jour automatiques de sécurité ?: ")
if quiz_3 == "oui":
    resultat_oui = resultat_oui + 1
    
quiz_4 = input("4. Évitez-vous de vous connecter sur des réseaux Wi-Fi publics pour des tâches sensibles ?: ")
if quiz_4 == "oui":
    resultat_oui = resultat_oui + 1

quiz_5 = input("5. Utilisez-vous l'authentification à deux facteurs quand c'est possible ? : ")
if quiz_5 == "oui":
    resultat_oui = resultat_oui + 1

# ============= ANALYSE DES RESULTATS =================
print(" ++++++++++++++  ANALYSE DES RESULTATS +++++++++++++++++")
print(f" SCORE TOTAL : {resultat_oui} /5 \n")

if resultat_oui < 1 :
    print(f"🚨Cyber-Novice : Attention, des améliorations sont nécessaires...\n")
elif resultat_oui < 3 :
    print(f"⚠️ Utilisateur Prudent : Bonne bases, Quelques améliorations possibles...\n")
else :
    print(f"🛡️ Cyber-Expert : Excellent niveau de sécurité...\n")

