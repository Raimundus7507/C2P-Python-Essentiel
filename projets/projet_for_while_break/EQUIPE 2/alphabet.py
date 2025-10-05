import random
while True :
    chances = 3
    cnt = 1
    score = 0
    error = 0
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



    user_choice = input("\nVoulez-vous refaire une partie ? (y/n) : ")
    if user_choice != "y" and user_choice != "Y":
        print(f"""
                                    {'-' * 4}A la prochaine !{'-' * 4}""")
        break