 # nom du programme
print("\n=== COMPTEUR MAGIQUE ===\n")

# objectif 
print("Comptage de 1 à 20 avec des règles spéciales...\n")

# commter de 1 à 20 avec une boucle for
for i in range(1, 21, 1):
    if i % 3 == 0:
       # print(f"{i + 1} ({i} ignoré - multiple de 3)")
        continue
    if i % 3 == 1 and i != 1 and i!= 13:
        print(f"{i } ({i - 1} ignoré - multiple de 3)")
        continue
    elif i == 13:
        print(f"{i} (Nombre mystère - on ne fait rien)")
        pass
        continue
    elif i == 17:
        print("\nSTOP ! Nombre 17 trouvé - arrêt du compteur !")
        break 
    print(i)
