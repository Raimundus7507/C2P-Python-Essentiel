# Definition de la fonction de la fonction saisie
def saisi(position = "premier"):
    while True:
        try:
            nombre = int(input(f"Entrer un {position} nombre : "))
            return nombre
        except ValueError:
            print("Veuillez saisir un entier")

# Definition de la fonction signe
def signe(A , B):
    if (A * B > 0):
        print(f"{A} et {B} sont de même signe.")
    elif ( A * B == 0):
        if (A == 0 and B != 0) :
           print(f"{A} est nul")
        elif (B == 0 and A != 0) :
            print(f"{B}  est nul")
        else :
            print(f"{A} et {B} sont nuls.")
    else :
        print(f"{A} et {B} sont de signe contraire.")

# Definition de la fonction minimum
def minimum(X,Y):
    min = X
    if X > Y :
        min = Y
    return min

# Definition de la fonction maximum
def maximum(X,Y):
    max = X
    if X < Y :
        max = Y
    return max

# Appel de la fonction saisi
X = saisi()
Y = saisi("second")

# Appel de la fonction signe
signe(X, Y)

# Appel de la fonction minimum
min_num = minimum(X, Y)
print(f"Le minimum est : {min_num}")

# Appel de la fonction maximum
max_num = maximum(X, Y)
print(f"Le maximum est : {max_num}")


