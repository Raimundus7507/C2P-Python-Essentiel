nombre = int(input("entrer un nombre strictement supérieur à 1 : "))
print("entrer un nombre strictement supérieur à 1 ")
while nombre <= 1:

    nombre =int(input("valeur invalide veuillez saisir un nombre supérieur à 1  :")) 

somme = 0
i=1
while i <=nombre:
    somme = somme + i
    i = i + 1
print("la somme des entiers de 1 jusqu'à", nombre,"est :", somme)


