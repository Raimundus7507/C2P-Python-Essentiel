import random
while True :
    chances = 3
    cnt = 1
    score = 0
    error = 0
    print("""
                                    💯 QUIZ DE CALCUL MENTAL 💯 \n
                                (Tapez 'p' pour passer une question)\n""")
    while chances > 0 :
        firstNum = random.randint(2,50)
        secondNum = random.randint(2, 50)
        user_choice = input(f"Question {cnt} : {firstNum} * {secondNum} = ")
        if user_choice == 'p' or user_choice == 'P':
            print("⏭️ Question passée.\n")
        elif int(user_choice) == firstNum * secondNum :
            score += 1
            print(f"✅ Correct ! Score : {score} | Erreur : {error}\n")
        else :
            error += 1
            print(f"❌ Faux ! C'était {firstNum * secondNum}. Erreur : {error}\n")
            if error == chances :
                print(f"""
                            {"💀"*3} {chances} erreurs ! Fin du quiz. {"💀"*3}\n
                                Score final : {score} bonnes réponses """)
                break
    user_choice = input("\nVoulez-vous refaire une partie ? (y/n) : ")
    if user_choice != "y" and user_choice != "Y":
        print(f"""
                                    {'-' * 4}A la prochaine !{'-' * 4}""")
        break