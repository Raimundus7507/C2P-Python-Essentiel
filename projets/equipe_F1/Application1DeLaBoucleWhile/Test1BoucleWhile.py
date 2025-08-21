# Ce programme demande a l'user d'entrer un entier compris entre 10 et 20
# Affiche le message "Plus petit" si l'entier est < 10 et "Plus grand" si l'entier > 20

#  Message d'entrée 
nombre = int(input("Veuillez saisir un nombre compris entre 10 et 20 : ")) 

while nombre < 10 or nombre > 20 :
    if nombre < 10 :
        nombre = int(input(" Plus petit : "))   # Demande à l'user d'entrer à nouveau
    else :
        nombre = int(input(" Plus grand : "))   # Demande à l'user d'entrer à nouveau 

print(" \n Félicitation ta reponse est valide !!\n T'es un(e) sacré(e) génie !!\n")