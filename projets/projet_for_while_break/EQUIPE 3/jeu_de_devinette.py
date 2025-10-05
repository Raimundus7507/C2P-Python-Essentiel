# Jeu de Devinettes
import random  # Pour générer des nombres et choix aléatoires

# Menu affiché au joueur
menu = """
1. 🔢 Deviner un nombre1
2. 🎲 Lancer les dés
3. 💯 Quiz de calcul mental
4. 🔤 Deviner la lettre
5. 📊 Voir mes statistiques
6. ❌ Quitter"""

# --- Initialisation des compteurs pour le nombre de parties jouées ---
nbre_part_1 = 0  # Jeu 1 : Deviner un nombre
nbre_part_2 = 0  # Jeu 2 : Lancer les dés
nbre_part_3 = 0  # Jeu 3 : Quiz de calcul mental
nbre_part_4 = 0  # Jeu 4 : Deviner la lettre

# --- Initialisation des compteurs pour victoires et défaites ---
nbre_perd_1, nbre_perd_2, nbre_perd_3, nbre_perd_4 = 0, 0, 0, 0
nbre_gag_1, nbre_gag_2, nbre_gag_3, nbre_gag_4 = 0, 0, 0, 0

# Boucle principale du programme
continuer = True
while continuer:
    print("JEU DE DEVINETTE")
    print("--" * 55)
    print(menu)
    choix = int(input("Entrer entre 1 et 6 : "))  # L'utilisateur choisit un jeu


    # 1. Jeu : Deviner un nombre

    if choix == 1:
        nombre_secret = random.randint(1, 100)  # Nombre secret aléatoire
        max_essais = 7  # Nombre maximum d'essais autorisés
        trouve = False  # Indicateur de victoire
        essais = 0  # Compteur d'essais effectués

        print("🔢 DEVINER UN NOMBRE")
        print("Je pense à un nombre entre 1 et 100")
        print("Vous avez 7 essais (tapez 0 pour abandonner)\n")

        # Boucle principale du jeu
        while essais < max_essais and not trouve:  # Tant que le joueur n’a pas trouvé et qu’il reste des essais
            A = int(input(f"Essai {essais + 1}/{max_essais} : "))

            if A == 0:  # L'utilisateur abandonne
                print(f"🏳 Vous avez abandonné. Le nombre secret était {nombre_secret}.")
                break
            elif A == nombre_secret:  # Nombre trouvé
                print(f"🎉 Bravo ! Vous avez trouvé le nombre secret {nombre_secret} en {essais + 1} essais.")
                nbre_gag_1 += 1  # Compteur de victoires
                trouve = True
            elif A > nombre_secret:  # Indice si le nombre proposé est trop grand
                print("📉 Plus petit !")
            else:  # Indice si le nombre proposé est trop petit
                print("📈 Plus grand !")

            essais += 1  # Incrément du nombre d’essais

        nbre_part_1 += 1  # Incrément du nombre de parties jouées pour ce jeu
        if not trouve and A != 0:  # Si le joueur n’a pas trouvé et n’a pas abandonné
            nbre_perd_1 += 1  # Compteur de défaites
            print(f"❌ Échec ! Le nombre secret était {nombre_secret}.")


    # 2. Jeu : Lancer les dés

    elif choix == 2:
        print("lancer les Des")
        print("objectif : obtenir un double")
        lancer = 0  # Compteur du nombre de lancers
        De1 = 0  # Premier dé
        De2 = 1  # Deuxième dé (différent pour entrer dans la boucle)
        App = input("Appuyer sur entrer pour commencer la simulation :")

        # Boucle tant qu’un double n’est pas obtenu
        while De1 != De2:
            lancer += 1
            De1 = random.randint(1, 6)  # Lancer du premier dé
            De2 = random.randint(1, 6)  # Lancer du deuxième dé
            print(f"lancer {lancer} :{De1} - {De2}")

        nbre_part_2 += 1  # Incrément du nombre de parties jouées
        print(f"Double obtenu en {lancer} lance(s)")


    # 3. Jeu : Quiz de calcul mental

    elif choix == 3:
        error = 0  # Compteur d'erreurs
        question = 0  # Compteur de questions posées
        score = 0  # Compteur de bonnes réponses

        print("💯 QUIZ DE CALCUL MENTAL")
        print("(Tapez 'p' pour passer une question)\n")

        # Boucle du quiz
        while error < 3:  # Tant que le joueur a moins de 3 erreurs
            nbre1 = random.randint(1, 50)
            nbre2 = random.randint(1, 50)
            operateur = random.choice("+-")  # Choix de l'opérateur aléatoire
            resultat = nbre1 + nbre2 if operateur == "+" else nbre1 - nbre2  # Calcul du résultat attendu

            question += 1
            reponse = input(f"Question {question}: Combien fait {nbre1} {operateur} {nbre2} ? ")

            if reponse == "p":  # Passer la question
                print("⏭️ Question passée.\n")
                continue

            if reponse.lstrip("-").isdigit():  # Vérifie que la réponse est un nombre (positif ou négatif)
                if int(reponse) == resultat:  # Bonne réponse
                    score += 1
                    nbre_gag_3 += 1
                    print(f"✅ Correct ! Score : {score} | Erreurs : {error}\n")
                else:  # Mauvaise réponse
                    error += 1
                    nbre_perd_3 += 1
                    print(f"❌ Faux ! C'était {resultat}. Erreurs : {error}\n")
            else:  # Entrée invalide
                print("⚠️ Entrée invalide (entrez un nombre ou 'p').\n")

        nbre_part_3 += 1  # Incrément du nombre de parties jouées
        print("💀 3 erreurs ! Fin du quiz.")
        print(f"Score final : {score} bonnes réponses")


    # 4. Jeu : Deviner la lettre

    elif choix == 4:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Liste des lettres possibles
        lettre_secrete = random.choice(alphabet)  # Choix aléatoire d'une lettre
        Essai = 0  # Compteur d'essais
        Essai_max = 10  # Nombre maximum d'essais

        print("🔤 DEVINER LA LETTRE")
        print("Je pense à une lettre entre A et Z.")
        print("Vous avez 10 essais maximum.\n")

        while Essai < Essai_max:  # Tant que le joueur n'a pas dépassé les essais
            proposition = input(f"Essai {Essai + 1}/{Essai_max} Quelle lettre ? ").upper()

            if len(proposition) != 1:  # Vérifie que l'entrée contient une seule lettre
                print("❌ Une seule lettre !")
                continue

            if not proposition.isalpha():  # Vérifie que l'entrée est bien une lettre
                print("❌ Doit être une lettre !")
                continue

            Essai += 1  # Incrément du nombre d’essais

            if proposition == lettre_secrete:  # Bonne lettre
                print(f"🎉 Bravo ! La lettre secrète était {lettre_secrete} !")
                nbre_gag_4 += 1
                break
            elif proposition < lettre_secrete:  # Lettre avant la lettre secrète
                print("📈 C'est après dans l'alphabet !")
            else:  # Lettre après la lettre secrète
                print("📉 C'est avant dans l'alphabet !")
        else:  # Si tous les essais sont utilisés
            print(f"❌ Nombre d'essais maximum atteint. La lettre secrète était {lettre_secrete}.")
            nbre_perd_4 += 1

        nbre_part_4 += 1  # Incrément du nombre de parties jouées


    # 5. Statistiques

    elif choix == 5:
        print("--"*55)
        print("Nombre de partie jouée par jeu ")
        print("--" * 55)
        print(f"Nombre de parties joué au jeu 1:{nbre_part_1}")
        print(f"Nombre de parties joué au jeu 2:{nbre_part_2}")
        print(f"Nombre de parties joué au jeu 3:{nbre_part_3}")
        print(f"Nombre de parties joué au jeu 4:{nbre_part_4}")

        # Calcul des taux de réussite pour chaque jeu
        taux_jeu1 = nbre_gag_1 / max((nbre_gag_1 + nbre_perd_1), 1) * 100
        taux_jeu2 = nbre_gag_2 / max((nbre_gag_2 + nbre_perd_2), 1) * 100
        taux_jeu3 = nbre_gag_3 / max((nbre_gag_3 + nbre_perd_3), 1) * 100
        taux_jeu4 = nbre_gag_4 / max((nbre_gag_4 + nbre_perd_4), 1) * 100

        # Taux global sur tous les jeux
        total_gagnes = nbre_gag_1 + nbre_gag_2 + nbre_gag_3 + nbre_gag_4
        total_perdus = nbre_perd_1 + nbre_perd_2 + nbre_perd_3 + nbre_perd_4
        taux_global = total_gagnes / max((total_gagnes + total_perdus), 1) * 100
        print("--" * 55)
        # Affichage des taux
        # --- Affichage ---
        print("\n📊 TAUX DE RÉUSSITE")
        print(f"Jeu 1 (Deviner un nombre) : {taux_jeu1:.2f}%")
        print(f"Jeu 2 (Lancer les dés) : {taux_jeu2:.2f}%")
        print(f"Jeu 3 (Quiz mental) : {taux_jeu3:.2f}%")
        print(f"Jeu 4 (Deviner la lettre) : {taux_jeu4:.2f}%")
        print(f"➡️ Taux global sur tous les jeux : {taux_global:.2f}%")
        print(f"➡️ Taux de réussite global sur tous les jeux : {taux_global:.2f}%")

    # 6. Quitter le jeu
    elif choix == 6:
        continuer = False # Arrête la boucle principale et donc le programme
