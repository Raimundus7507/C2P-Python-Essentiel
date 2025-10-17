
print("--"*70)

print(" ===CYBERGUARDIAN: TESTEZ VOTRE SECURITE NUMERIQUE !===")

print("Bienvenue ! Ce quiz va évaluer vos habitudes de cybersécurité \n"
       "Répondez par 'oui' ou 'non' à chaque question ")
# demande de question
Q1=input("Question 1/5:Utisez-vous un mot de passe different pour chaque compte ?\n"
          "Merci de repondre par (oui ou non):")
Q2=input("Question 2/5:Vérifiez-vous l'URL avant de saisir vos informations personnelles ??\n"
          "Merci de repondre par (oui ou non):")
Q3=input("Question 3/5:Activez-vous les mises à jour automatiques de sécurité ??\n"
          "Merci de repondre par (oui ou non):")
Q4=input("Question 4/5:Evitez-vous de vous connecter sur des réseaux WI-FI publics pour des tâches sensibles??\n"
          "Merci de repondre par (oui ou non):")
Q5=input("Question 5/5:Utilisez-vous l'authentification à deux facteurs quand c'est possible??\n"
          "Merci de repondre par (oui ou non):")
print("--"*70)
# Instructions conditionnelles
# pour Q1
if Q1=='oui':
    Q11=1
elif Q1=='non':
    Q11=0
# pour Q2
if Q2=='oui':
    Q22=1
elif Q2=='non':
    Q22=0
# pour Q3
if Q3=='oui':
    Q33=1
elif Q3=='non':
    Q33=0
# pour Q4
if Q4=='oui':
    Q44=1
elif Q4=='non':
    Q44=0
# pour Q5
if Q5=='oui':
    Q55=1
elif Q5=='non':
    Q55=0
# déclaration des variables repo= Q11+Q22+Q33+Q44+Q55
repo= Q11+Q22+Q33+Q44+Q55

# Instructions conditionnelles
print("===VOTRE PROFIL CYBERSECURITE===")
if 4 <= repo <= 5:
    print('✅cyber-Expert')
    print("Excélent niveau de sécurité")
elif 2<= repo <= 3 :
    print('⚠️Utilisateur Prudent')
    print("Bonnes bases , quelques améliorations possibles")
elif 0<= repo <= 1 :
    print("⭕cyber-novice")
    print("Attention,des améliorations sont nécessaires")
print("--"*70)
print("fin du QUIZ ")
print("--"*70)


