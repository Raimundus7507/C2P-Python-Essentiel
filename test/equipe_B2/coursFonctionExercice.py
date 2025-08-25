# Fonction de détermination si A et B sont de meme signe
def signe ( A, B) :
    if A * B > 0 :
        print(f'{A} et {B} sont de meme signe')
    else :
        print(f'{A} et {B} sont de signe contraire')

# Fonction pour déterminer le minimum entre A et B
def minimum ( A, B) :
    if A < B :
        return A
    else :
        return B

# Fonction pour déterminer le maximum entre A et B
def maximum ( A, B) :
    if A > B :
        return A
    else :
        return B

# Affichage de l'utilité su programme
print('\n\n=== DETERMINONS SI VOS DEUX VARIABLES SONT DE MEME SIGNE, MINIMUM ET MAXIMUM DES DEUX ===\n')

# Saisie des deus variables de l'utilisateur
A = int(input("Veuillez entrer la valeur de A: "))
B = int(input("Veuillez entrer la valeur de B: "))

print()
# Appel de la fonction Signe
signe (A, B)

# Appel et affichage personnalisé de la fonction minimum
print(f'\nLe minimum entre {A} et {B} est {minimum (A, B)}')

# Appel et affichage personnalisé de la fonction maximum
print(f'\nLe maximum entre {A} et {B} est {maximum (A, B)}')