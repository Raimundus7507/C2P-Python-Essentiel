import random

NbrPartieDevineNombre = 0
NbrPartieDevineNombreGagne = 0
MeilleurePartieDevineNombre = 0

NbrPartieDevineLettre = 0
NbrPartieDevineLettreGagne = 0
MeilleurePartieDevineLettre = 0

NbrPartieQuiz = 0
MeilleurePartieQuiz = 0

NbrPartieDees = 0
MeilleurePartieDees = 0

while True:
    print("""
                                        \n🎮 JEU DE DEVINETTES')
                                        ====================
                                        1. 🔢 Deviner un nombre
                                        2. 🎲 Lancer les dés
                                        3. 💯 Quiz de calcul mental
                                        4. 🔤 Deviner la lettre
                                        5. 📊 Voir mes statistiques
                                        6. ❌ Quitter """)

    Menu_choice = input("\nVotre choix : ")
    if Menu_choice == '':
        print("❌ Entrez un nombre entre 1 et 6")
        continue

    if not Menu_choice.isdigit():
        print("❌ Veuillez entrer un nombre (1-6).")
        continue

    Menu_choice = int(Menu_choice)

    # ❌ Quitter
    if Menu_choice == 6:
        print("\n👋 Merci d'avoir joué ! À bientôt !")
        break

    # 🔢 Deviner un nombre
    elif Menu_choice == 1:
        while True:
            NbrPartieDevineNombre += 1
            chances = 7
            cnt = 1
            CPU_Guess = random.randint(1, 100)
            print(f"""\n
                                   {'_' * 4} Je pense a un nombre entre 0 et 100 {'_' * 4} \n
                                    Vous avez {chances} essais (tapez 0 pour abandonner)\n""")
            while cnt <= chances:
                while True:
                    user_answer = input(f"essais {cnt}/{chances} : ")
                    if not user_answer.isdigit():
                        print("Veuillez entrer une reponse valide !")
                        continue
                    else:
                        user_answer = int(user_answer)
                        break
                if user_answer == 0:
                    NbrPartieDevineNombre -= 1
                    print("""
                                    :( Oupssss Vous abandonez ): """)
                    break
                elif user_answer < CPU_Guess:
                    print("Vous etes en dessous du nombre mystere !\n")
                elif user_answer > CPU_Guess:
                    print("Vous etes au dessus du nombre mystere !\n")
                else:
                    NbrPartieDevineNombreGagne += 1
                    if MeilleurePartieDevineNombre < cnt :
                        MeilleurePartieDevineNombre = cnt
                    print(f"""
                                {'🎉' * 3} Bravo ! Trouvé en {cnt} essais ! {'🎉' * 3}""")
                    break
                cnt += 1
                if cnt > chances:
                    print(f"""  
                                    Vous aves atteint les {chances} essais \n
                                    Dommage le nombre mystere etait {CPU_Guess}\n
                            {'-' * 4} Bonne chance pour une prochaine fois {'-' * 4}
                            """)

            user_choice = input("\nVoulez-vous refaire une partie ? (y/n) : ")
            if user_choice.upper() != "Y":
                print(f"""
                                        {'-' * 4}Au prochain GAME champion{'-' * 4}""")
                break

    # 🎲 Lancer les dés
    elif Menu_choice == 2 :
        while True:
            NbrPartieDees += 1
            lancer = 0
            print('\n🎲 LANCER LES DÉS')
            print('Objectif : Obtenir un double !')

            while True:
                user_choice = input("\nAppuyez sur Entrée pour lancer les dés ( '0' pour abandonner ) ↩️ ")
                if user_choice == '0':
                    MeilleurePartieDees -= 1
                    print("""
                                        :( Oupssss Vous abandonez ): """)
                    break
                else:
                    lancer += 1
                    de1 = random.randint(1, 6)
                    de2 = random.randint(1, 6)
                    print(f"Lancer {lancer} : 🎲 {de1} - 🎲 {de2} {"Domnage réessayez" if de1 != de2 else ''}")
                    if de1 == de2:
                        print(f"🎉 Double obtenu en {lancer} lancers !")
                        if MeilleurePartieDees < lancer:
                            MeilleurePartieDees = lancer
                        break

            user_choice = input("\nVoulez-vous refaire une partie ? (y/n) : ")
            if user_choice != "y" and user_choice != "Y":
                print(f"""
                                            {'-' * 4}Au prochain GAME champion{'-' * 4}""")
                break

    # 💯 Quiz de calcul mental
    elif Menu_choice == 3 :
        while True:
            NbrPartieQuiz += 1
            chances = 3
            cnt = 1
            score = 0
            error = 0
            parties = 10
            print("""
                                            💯 QUIZ DE CALCUL MENTAL 💯 \n
                                        (Tapez 'p' pour passer une question)\n""")
            while error < chances and cnt <= parties:
                firstNum = random.randint(2, 50)
                secondNum = random.randint(2, 50)
                operator = random.choice("-+")
                result = 0
                if operator == '-':
                    result = firstNum - secondNum
                else:
                    result = firstNum + secondNum

                while True:
                    user_choice = input(f"Question {cnt} : {firstNum} {operator} {secondNum} = ")
                    if user_choice != 'p' and not user_choice.isdigit():
                        print("Veuillez entrer une reponse valide !")
                        continue
                    else:
                        break
                if user_choice == 'p' or user_choice == 'P':
                    print(f"⏭️ Question {cnt} passée.\n")
                elif int(user_choice) == result:
                    score += 1
                    print(f"✅ Correct ! Score : {score} | Erreur : {error}\n")
                else:
                    error += 1
                    print(f"❌ Faux ! C'était {result}. Erreur : {error}\n")
                    if error == chances:
                        print(f"""
                                    {"💀" * 3} {chances} erreurs ! Fin du quiz. {"💀" * 3}\n
                                        Score final : {score} bonnes réponses """)
                        break
                if MeilleurePartieQuiz < score :
                    MeilleurePartieQuiz += 1
                cnt += 1
            user_choice = input("\nVoulez-vous refaire une partie ? (y/n) : ")
            if user_choice != "y" and user_choice != "Y":
                print(f"""
                                            {'-' * 4}Au prochain GAME champion{'-' * 4}""")
                break

    # 🔤 Deviner la lettre
    elif Menu_choice == 4 :
        while True:
            NbrPartieDevineLettre += 1
            chances = 10
            cnt = 1
            score = 0
            error = 0
            ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            user_choice_value = 0
            CPU_Guess_value = 0
            CPU_Guess = random.choice(ALPHABET)
            print(f"""\n
                                       {'_' * 4} Je pense a une lettre entre A et Z {'_' * 4} \n
                                        Vous avez {chances} essais (tapez 0 pour abandonner)\n""")
            while cnt <= chances:
                i = 0
                while True:
                    user_choice = input(f"Essai {cnt}/{chances} : ").upper()
                    Alpha_counter = 0
                    for alphabet in user_choice:
                        Alpha_counter += 1
                    if not user_choice == '0' and not user_choice in ALPHABET or Alpha_counter != 1:
                        print("Veuillez entrer une lettre valide de l'alfabet !")
                        continue
                    else:
                        break

                if user_choice == '0':
                    NbrPartieDevineLettre -= 1
                    print("""
                                        :( Oupssss Vous abandonez ): """)
                    break

                for letter in ALPHABET:
                    if user_choice == letter:
                        user_choice_value = i
                    if CPU_Guess == letter:
                        CPU_Guess_value = i
                    i += 1
                if user_choice_value == CPU_Guess_value:
                    NbrPartieDevineLettreGagne += 1
                    if MeilleurePartieDevineLettre < cnt :
                        MeilleurePartieDevineLettre = cnt
                    print(f"""🎉 Bravo ! La lettre était {CPU_Guess} !""")
                    break
                elif user_choice_value < CPU_Guess_value:
                    print(f"""Allez encore devant ! 📈\n""")
                else:
                    print(f"""📉 Revenez en arriere ! \n""")
                cnt += 1
                if cnt > chances:
                    print(f"""  
                                   💀 Vous aves atteint les {chances} essais 💀\n
                                     Dommage la lettre mystere etait '{CPU_Guess}'\n
                                {'-' * 4} Bonne chance pour une prochaine fois {'-' * 4}
                            """)

            user_choice = input("\nVoulez-vous refaire une partie ? (y/n) : ")
            if user_choice != "y" and user_choice != "Y":
                print(f"""
                                            {'-' * 4}Au prochain GAME champion{'-' * 4}""")
                break

    # 📊 Voir mes statistiques
    elif Menu_choice == 5 :
        print("""\n
                            📊 STATISTIQUES DE LA SESSION""")
        print("""\n
                                — Deviner un nombre —""")
        print(f"Parties jouées : {NbrPartieDevineNombre}")
        if NbrPartieDevineNombre > 0:
            taux = (NbrPartieDevineNombre * 100) / NbrPartieDevineNombre
            print(f"Taux de réussite : {taux:.1f}%")
            if MeilleurePartieDevineNombre is not None:
                print(f"Meilleur (moins d'essais) : {MeilleurePartieDevineNombre}")

        print("""\n
                                — Lancer les dés —""")
        print(f"Parties jouées : {NbrPartieDees}")
        if NbrPartieDees > 0 and MeilleurePartieDees is not None:
            print(f"Meilleur (moins de lancers) : {MeilleurePartieDees}")

        print("""\n
                                — Quiz de calcul —""")
        print(f"Parties jouées : {NbrPartieQuiz}")
        if NbrPartieQuiz > 0:
            print(f'Meilleur score : {MeilleurePartieQuiz}')

        print("""\n
                                — Deviner la lettre —""")
        print(f'Parties jouées : {NbrPartieDevineLettre}')
        if NbrPartieDevineLettre > 0:
            taux_lettre = (NbrPartieDevineLettreGagne * 100) / NbrPartieDevineLettre
            print(f"Taux de réussite : {taux_lettre:.1f}%")
            if MeilleurePartieDevineLettre is not None:
                print(f"Meilleur (moins d'essais) : {MeilleurePartieDevineLettre}")

    else:
        print(Menu_choice)
        print("❌ Choix invalide, choisissez entre 1 et 6.")