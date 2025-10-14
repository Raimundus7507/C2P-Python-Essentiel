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

# --- Initialisation des meilleurs scores ---
meilleur_score_1 = 0  # Moins d'essais = mieux
meilleur_score_2 = 0  # Moins de lancers = mieux
meilleur_score_3 = 0  # Plus de bonnes réponses = mieux
meilleur_score_4 = 0  # Moins d'essais = mieux

# Boucle principale du programme
continuer = True
while continuer:
    print("JEU DE DEVINETTE")
    print("--" * 55)
    print(menu)
    choix = int(input("Entrer entre 1 et 6 : "))  # L'utilisateur choisit un jeu


    # 1. Jeu : Deviner un nombre
    if choix == 1:
        nombre_secret = random.randint(1, 100)
        max_essais = 7
        trouve = False
        essais = 0

        print("🔢 DEVINER UN NOMBRE")
        print("Je pense à un nombre entre 1 et 100")
        print("Vous avez 7 essais (tapez 0 pour abandonner)\n")

        while essais < max_essais and not trouve:
            A = int(input(f"Essai {essais + 1}/{max_essais} : "))

            if A == 0:
                print(f"🏳 Vous avez abandonné. Le nombre secret était {nombre_secret}.")
                break
            elif A == nombre_secret:
                print(f"🎉 Bravo ! Vous avez trouvé le nombre secret {nombre_secret} en {essais + 1} essais.")
                nbre_gag_1 += 1
                trouve = True
                # Mise à jour du meilleur score
                if meilleur_score_1 == 0 or essais + 1 < meilleur_score_1:
                    meilleur_score_1 = essais + 1
            elif A > nombre_secret:
                print("📉 Plus petit !")
            else:
                print("📈 Plus grand !")

            essais += 1

        nbre_part_1 += 1
        if not trouve and A != 0:
            nbre_perd_1 += 1
            print(f"❌ Échec ! Le nombre secret était {nombre_secret}.")


    # 2. Jeu : Lancer les dés
    elif choix == 2:
        print("lancer les Des")
        print("objectif : obtenir un double")
        lancer = 0
        De1 = 0
        De2 = 1
        App = input("Appuyer sur entrer pour commencer la simulation :")

        while De1 != De2:
            lancer += 1
            De1 = random.randint(1, 6)
            De2 = random.randint(1, 6)
            print(f"lancer {lancer} :{De1} - {De2}")

        nbre_part_2 += 1
        print(f"Double obtenu en {lancer} lance(s)")

        # Mise à jour du meilleur score
        if meilleur_score_2 == 0 or lancer < meilleur_score_2:
            meilleur_score_2 = lancer


    # 3. Jeu : Quiz de calcul mental
    elif choix == 3:
        error = 0
        question = 0
        score = 0

        print("💯 QUIZ DE CALCUL MENTAL")
        print("(Tapez 'p' pour passer une question)\n")

        while error < 3:
            nbre1 = random.randint(1, 50)
            nbre2 = random.randint(1, 50)
            operateur = random.choice("+-")
            resultat = nbre1 + nbre2 if operateur == "+" else nbre1 - nbre2

            question += 1
            reponse = input(f"Question {question}: Combien fait {nbre1} {operateur} {nbre2} ? ")

            if reponse == "p":
                print("⏭️ Question passée.\n")
                continue

            if reponse.lstrip("-").isdigit():
                if int(reponse) == resultat:
                    score += 1
                    nbre_gag_3 += 1
                    print(f"✅ Correct ! Score : {score} | Erreurs : {error}\n")
                else:
                    error += 1
                    nbre_perd_3 += 1
                    print(f"❌ Faux ! C'était {resultat}. Erreurs : {error}\n")
            else:
                print("⚠️ Entrée invalide (entrez un nombre ou 'p').\n")

        nbre_part_3 += 1
        print("💀 3 erreurs ! Fin du quiz.")
        print(f"Score final : {score} bonnes réponses")

        # Mise à jour du meilleur score
        if score > meilleur_score_3:
            meilleur_score_3 = score


    # 4. Jeu : Deviner la lettre
    elif choix == 4:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lettre_secrete = random.choice(alphabet)
        Essai = 0
        Essai_max = 10

        print("🔤 DEVINER LA LETTRE")
        print("Je pense à une lettre entre A et Z.")
        print("Vous avez 10 essais maximum.\n")

        while Essai < Essai_max:
            proposition = input(f"Essai {Essai + 1}/{Essai_max} Quelle lettre ? ").upper()

            if len(proposition) != 1:
                print("❌ Une seule lettre !")
                continue

            if not proposition.isalpha():
                print("❌ Doit être une lettre !")
                continue

            Essai += 1

            if proposition == lettre_secrete:
                print(f"🎉 Bravo ! La lettre secrète était {lettre_secrete} !")
                nbre_gag_4 += 1
                # Mise à jour du meilleur score
                if meilleur_score_4 == 0 or Essai < meilleur_score_4:
                    meilleur_score_4 = Essai
                break
            elif proposition < lettre_secrete:
                print("📈 C'est après dans l'alphabet !")
            else:
                print("📉 C'est avant dans l'alphabet !")
        else:
            print(f"❌ Nombre d'essais maximum atteint. La lettre secrète était {lettre_secrete}.")
            nbre_perd_4 += 1

        nbre_part_4 += 1


    # 5. Statistiques
    elif choix == 5:
        print("--"*55)
        print("Nombre de parties jouées par jeu")
        print("--"*55)
        print(f"Jeu 1 : {nbre_part_1} parties")
        print(f"Jeu 2 : {nbre_part_2} parties")
        print(f"Jeu 3 : {nbre_part_3} parties")
        print(f"Jeu 4 : {nbre_part_4} parties")

        # Taux de réussite
        taux_jeu1 = nbre_gag_1 / max((nbre_gag_1 + nbre_perd_1), 1) * 100
        taux_jeu2 = nbre_gag_2 / max((nbre_gag_2 + nbre_perd_2), 1) * 100
        taux_jeu3 = nbre_gag_3 / max((nbre_gag_3 + nbre_perd_3), 1) * 100
        taux_jeu4 = nbre_gag_4 / max((nbre_gag_4 + nbre_perd_4), 1) * 100
        total_gagnes = nbre_gag_1 + nbre_gag_2 + nbre_gag_3 + nbre_gag_4
        total_perdus = nbre_perd_1 + nbre_perd_2 + nbre_perd_3 + nbre_perd_4
        taux_global = total_gagnes / max((total_gagnes + total_perdus), 1) * 100

        print("--"*55)
        print("\n📊 TAUX DE RÉUSSITE")
        print(f"Jeu 1 : {taux_jeu1:.2f}% | Meilleur score : {meilleur_score_1} essais")
        print(f"Jeu 2 : {taux_jeu2:.2f}% | Meilleur score : {meilleur_score_2} lancers")
        print(f"Jeu 3 : {taux_jeu3:.2f}% | Meilleur score : {meilleur_score_3} bonnes réponses")
        print(f"Jeu 4 : {taux_jeu4:.2f}% | Meilleur score : {meilleur_score_4} essais")
        print(f"Taux global sur tous les jeux : {taux_global:.2f}%")


    # 6. Quitter
    elif choix == 6:
        continuer = False