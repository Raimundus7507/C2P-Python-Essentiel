# Deviner un nombre
import random
while True :
    chances = 7
    cnt = 1
    CPU_Guess = random.randint(1, 100)
    print(f"""\n
                           {'_'*4} Je pense a un nombre entre 0 et 100 {'_'*4} \n
                            Vous avez 7 essais (tapez 0 pour abandonner)\n""")
    while cnt < chances+1:
        user_answer = int(input(f"essais {cnt}/{chances} : "))
        if user_answer == 0 or user_answer == 0 :
            print("""
                            :( Oupssss Vous abandonez ): """)
            break
        elif user_answer < CPU_Guess :
            print("Vous etes en dessous du nombre mystere !\n")
        elif user_answer > CPU_Guess :
            print("Vous etes au dessus du nombre mystere !\n")
        else :
            print(f"""
                        {'🎉'*3} Bravo ! Trouvé en {cnt} essais ! {'🎉'*3}""")
            break
        cnt += 1
        if cnt > chances :
            print(f"""  
                            Vous aves atteint les {chances} essais \n
                            Dommage le nombre mystere etait {CPU_Guess}\n
                    {'-'*4} Bonne chance pour une prochaine fois {'-'*4}
                    """)

    user_choice = input("\nVoulez-vous refaire une partie ? (y/n) : ")
    if user_choice != "y" and user_choice != "Y" :
        print(f"""
                                {'-'*4}A la prochaine !{'-'*4}""")
        break
