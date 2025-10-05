#Application console de quiz
print("\nETAPE 1\n")
print("*"*60)
print("Quel est le nom du plus petit pays au monde? ")
Q1 = str(input("Reponse : "))
print("Quelle est la superficie du Togo?")
Q2 = float(input("Reponse : "))
print("Quel est le plus haut sommet du Togo?")
Q3 = str(input("Reponse : "))

#Traitement des donnés
Reponse1 = "Vatican"
Reponse2 = 56600
Reponse3 = "Mont Agou"
score = 0
if Q1 == Reponse1 :
    score +=1
else:
    score = 0

if Q2 == Reponse2 :
    score +=1
else:
    score -=0

if Q3 == Reponse3 :
    score +=1
else:
    score -=0

#Affichage du score
print(f"Tu as eu {score } bonnes reponse(s) sur 3")
if score == 3 :
    print("Excellent !")
elif score == 2 :
    print("Bien joué !")
else :
    print("Continue à t'entraîner !")