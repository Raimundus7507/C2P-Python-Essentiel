import random
# Deviner le nombre
nombre_parties_nombre = 0
nombre_reussites_nombre = 0
# Lancer de dés
nombre_parties_des = 0
nombre_reussites_des = 0
# Quiz de calcul mental
nombre_parties_quiz = 0
nombre_reussites_quiz = 0
meilleur_score_quiz = 0
# Deviner la lettre
nombre_parties_lettre = 0
nombre_reussites_lettre = 0
nom = input("Bienvenue. Veuillez entrer votre prénom : ")
# Affichage du menu

menu = """\n🎮 JEUX DE DEVINETTE 
====================
1. 🔢 Deviner un nombre
2. 🎲 Lancer les dés
3. 🧮 Quiz de calcul mental
4. 🔤 Deviner la lettre
5. 📊 Voir mes statistiques
6. ❌ Quitter """
print(menu)

choix = input("\n🔀 Entrer votre choix : ")
while choix != "6":
    if choix == "1": # Deviner un nombre
        print("🔢 DEVINER UN NOMBRE \n")
        nombre_parties_nombre += 1
        nombre_machine = random.randint(1 , 100)
        print("Entrer un nombre compris entre 1 et 100 : ")
        print("Vous avez droit à 7 essais (enter 0 pour abandonner) :")
        nombre_essai = 1
        while nombre_essai  <= 7:
            nombre_utilisateur = int(input(f"Essai {nombre_essai}/7 :  "))
            if nombre_utilisateur > nombre_machine:
                print("📉 Plus petit ! ")
            elif nombre_utilisateur < nombre_machine:
                print("📈 Plus grand ! ")
            elif nombre_utilisateur == 0:
                print("🏳 Vous avez abandonné")
                break
            else:
                nombre_reussites_nombre += 1
                print(f"🎊 Bravo ! Vous avez deviné le nombre en {nombre_essai} essai(s) !")
                break
            nombre_essai += 1
        else:
            print(f"Vous avez atteint la limite.Le bon nombre était {nombre_machine}")

    elif choix == "2": # Lancer les dés
        print("🎲 LANCER DE DES")
        nombre_parties_des += 1
        print("Objectif : Obtenir un double !\n")
        nombre_lance = 1
        choix_lance = input("Entrer un nombre ou un caractère pour commencer : ")
        premier_de = random.randint(1, 6)
        second_de = random.randint(1, 6)
        print(f"Lancer {nombre_lance} : 🎲{premier_de} - 🎲{second_de}")
        while premier_de != second_de:
            choix_lance = input("Entrer un nombre strictement positif pour réessayer (0 pour abandonner) : ")
            if int(choix_lance) > 0:
                nombre_lance += 1
                premier_de = random.randint(1, 6)
                second_de = random.randint(1, 6)
                print(f"Lancer {nombre_lance} : 🎲{premier_de} - 🎲{second_de}")
            elif int(choix_lance) == 0:
                print("🏳 Vous avez abandonné")
                break
            else:
                print("❌ Choix invalide. Veuillez réessayer ")
        else:
            nombre_reussites_des += 1
            print(f"🎊 Double obtenu en {nombre_lance} lancer(s)!")

    elif choix == "3": #  Quiz de calcul mental
        print("🧮 QUIZ DE CALCUL MENTAL")
        nombre_parties_quiz += 1
        print("Vous n'avez droit qu'a trois erreurs au maximum\n ")
        nombre_erreur = 0
        score = 0
        while nombre_erreur < 3:
            nombre1 = random.randint(1, 50)
            nombre2 = random.randint(1, 50)
            operateur = random.choice("+-*")
            if operateur == "+":
                resultat = nombre1 + nombre2
            elif operateur == "-":
                resultat = nombre1 - nombre2
            else:
                resultat = nombre1 * nombre2
            print(f"Combien fait {nombre1} {operateur} {nombre2} ?")
            reponse = input("Votre réponse (p pour passer la question et 0 pour abandonner) : ")
            if reponse == str(resultat) :
                score += 1
                print(f"✅ Bonne réponse ! Score : {score} | Nombre d'erreurs : {nombre_erreur}")
            elif reponse == "p":
                print(f"⏭️ Question passée ! | Nombre d'erreurs = {nombre_erreur}")
                continue
            elif reponse == "0":
                print("🏳 Vous avez abandonné ")
                break
            else:
                nombre_erreur += 1
                print(f"❌ Mauvaise réponse ! La bonne réponse était {resultat} | Nombre d'erreurs : {nombre_erreur}")
        else:
            print("💀 Vous avez fait trois erreurs ! La partie est terminée ")
            print(f"Score final : {score} bonne(s) réponse(s)")
        if score > 0:
            nombre_reussites_quiz += 1
        if score > meilleur_score_quiz:
            meilleur_score_quiz = score

    elif choix == "4": #Deviner la lettre
        print("🔤 DEVINER LA LETTRE \n")
        nombre_parties_lettre += 1
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        lettre = random.choice(alphabet)
        lettre_essai = 1
        while lettre_essai <= 10:
            print(f"Choisissez une lettre parmi cette suite de lettres : {alphabet} ")
            lettre_utilisateur = input("Entrer votre réponse (0 pour abandonner) : ")
            if lettre == lettre_utilisateur:
                nombre_reussites_lettre += 1
                print(f"🎉 Bravo ! Lettre trouvée en {lettre_essai} essai(s)")
                break
            elif lettre_utilisateur == str(0):
                print(f"🏳 Vous avez abandonné. La bonne lettre était {lettre}")
            else:
                print(f"❌ Mauvaise réponse ! Veuillez  réessayer ")
            lettre_essai += 1
        else:
            print(f"\n💀 Vous atteint la limite de 10 essais. La bonne lettre était {lettre} ")
            break

    elif choix == "5": #voir mes statistiques
        print("📊 VOS STATS ")
        print("=============\n")
        print(f"🔢 Deviner un nombre      : {nombre_parties_nombre} partie(s) | {nombre_reussites_nombre} réussite(s) ")
        print(f"🎲 Lancer les dés         : {nombre_parties_des} partie(s)    | {nombre_reussites_des} réussite(s)")
        print(f"🧮 Quiz de calcul mental  : {nombre_parties_quiz} partie(s)   | {nombre_reussites_quiz} réussite(s)   | Meilleur score : {meilleur_score_quiz} bonne(s) réponse(s)")
        print(f"🔤 Deviner la lettre      : {nombre_parties_lettre} partie(s) | {nombre_reussites_lettre} réussite(s)")

    else:
        print("❌ Choix invalide. Veuillez réessayer ")
    print(menu)
    choix = input("\n🔀 Entrer votre choix : ")
else:
    print(f"Merci {nom} d'avoir joué. A bientôt 👋")