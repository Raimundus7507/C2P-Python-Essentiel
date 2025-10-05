#🎮Jeu de Devinettes Interactif

import random

# Variables de statistiques
nombre = 0
dés = 0
quiz = 0
lettre = 0

reussite_nombre = 0
reussite_lettre = 0
meilleur_score_quiz = 0

# Menu Principal
continuer = True
while continuer:
    print("\n🎮 JEU DE DEVINETTES")
    print("~" * 30)
    print("1. 🔢 Deviner un nombre")
    print("2. 🎲 Lancer les dés")
    print("3. 💯 Quiz de calcul mental")
    print("4. 🔤 Deviner la lettre")
    print("5. 📊 Voir mes statistiques")
    print("6. ❌ Quitter")

    choix = input("\nVeuillez entrer votre choix : ")

    # Validation du choix
    if not choix.isdigit():
        print("❌ Veuillez entrer un chiffre entre 1 et 6.")
        continue

    choix = int(choix)

    print("~" * 30)
    #Deviner un nombre
    print("~" * 30)
    if choix == 1:
        nombre += 1
        print("\n🔢 DEVINER UN NOMBRE")
        print("Je pense à un nombre entre 1 et 100.")
        print("Vous avez 7 essais (tapez 0 pour abandonner)")

        nombre_secret = random.randint(1, 100)
        essais = 0
        trouve = False

        while essais < 7 and not trouve:
            essais += 1
            reponse = input(f"\nEssai {essais}/7 : ")

            if not reponse.isdigit():
                print("❌ Entrez un nombre valide.")
                essais -= 1
                continue

            reponse = int(reponse)
            if reponse == 0:
                print("🚪 Vous avez abandonné !")
                break

            if reponse == nombre_secret:
                print(f"🎉 Bravo ! Trouvé en {essais} essais !")
                trouve = True
                reussite_nombre += 1
                break
            elif reponse < nombre_secret:
                print("📈 Plus grand !")
            else:
                print("📉 Plus petit !")

        if not trouve:
            print(f"💀 Perdu ! Le nombre était {nombre_secret}.")


    # Lancer les Dés
    elif choix == 2:
        dés += 1
        print("\n🎲 LANCER LES DÉS")
        print("Objectif : Obtenir un double !")

        lancers = 0
        while True:
            lancers += 1
            de1 = random.randint(1, 6)
            de2 = random.randint(1, 6)
            print(f"Lancer {lancers} : 🎲 {de1} - 🎲 {de2}")
            if de1 == de2:
                print(f"🎉 Double obtenu en {lancers} lancers !")
                break

    #Calcul Mental

    elif  choix == 3 :
        quiz += 1
        print("\n💯 QUIZ DE CALCUL MENTAL")
        print("(Tapez 'p' pour passer une question)")

        score = 0
        erreurs = 0
        question = 0

        while True:
            question += 1
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            operateur = random.choice("+-")

            if operateur == "+":
                resultat = a + b
            else:
                resultat = a - b

            reponse = input(f"\nQuestion {question} : {a} {operateur} {b} = ? ")

            if reponse.lower() == "p":
                print("⏭ Question passée.")
                continue

            if not reponse.lstrip('-').isdigit():
                print("❌ Entrez un nombre ou 'p' pour passer.")
                continue

            reponse = int(reponse)
            if reponse == resultat:
                score += 1
                print(f"✅ Correct ! Score : {score} | Erreurs : {erreurs}")
            else:
                erreurs += 1
                print(f"❌ Faux ! C'était {resultat}. Erreurs : {erreurs}")

            if erreurs >= 3:
                print("\n💀 3 erreurs ! Fin du quiz.")
                print(f"Score final : {score} bonnes réponses.")
                if score > meilleur_score_quiz:
                    meilleur_score_quiz = score
                break

    #Deviner une lettre

    elif choix == 4:
        lettre += 1
        print("\n🔤 DEVINER LA LETTRE")
        print("Je pense à une lettre entre A et Z.")
        lettre_secret = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        essais = 0
        trouve = False

        while essais < 10 and not trouve:
            essais += 1
            proposition = input(f"Essai {essais}/10 : ").upper()

            if len(proposition) != 1 or not proposition.isalpha():
                print("❌ Entrez une seule lettre valide (A-Z).")
                essais -= 1
                continue

            if proposition == lettre_secret:
                print(f"🎉 Bravo ! La lettre était {lettre_secret}.")
                trouve = True
                reussite_lettre += 1
                break
            elif proposition < lettre_secret:
                print("📈 C'est après dans l'alphabet !")
            else:
                print("📉 C'est avant dans l'alphabet !")

        if not trouve:
            print(f"💀 Perdu ! La lettre était {lettre_secret}.")

    # Statistique

    elif choix == 5:
        print("\n📊 STATISTIQUES")
        print("~"*30)
        print(f"Jeu du nombre     : {nombre} parties | Réussites : {reussite_nombre}")
        print(f"Lancer de dés     : {dés} parties")
        print(f"Quiz calcul mental: {quiz} parties | Meilleur score : {meilleur_score_quiz}")
        print(f"Deviner la lettre : {lettre} parties | Réussites : {reussite_lettre}")
        pass

    #Quitter

    elif choix == 6:
        print("\n👋 Merci d'avoir joué !")
        continuer = False
        break

    else:
        print("❌ Choix invalide. Entrez un nombre entre 1 et 6.")