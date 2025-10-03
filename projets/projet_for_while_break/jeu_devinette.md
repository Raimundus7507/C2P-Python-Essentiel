# Projet Python : Jeu de Devinettes Interactif

## 📋 Cahier des Charges

### Objectif
Développer un jeu de devinettes multi-niveaux utilisant les boucles `while`, et les instructions de contrôle `break`, `continue` et `pass`.

### Compétences visées
- Maîtrise de la boucle `while`
- Utilisation des instructions `break`, `continue`, `pass`
- Gestion des menus persistants
- Validation des entrées utilisateur
- Comptage et statistiques en temps réel

---

##  Fonctionnalités Requises

### 1. Menu Principal Persistant
Le programme doit tourner en boucle jusqu'à ce que l'utilisateur choisisse de quitter.

```
🎮 JEU DE DEVINETTES
====================
1. 🔢 Deviner un nombre
2. 🎲 Lancer les dés
3. 💯 Quiz de calcul mental
4. 🔤 Deviner la lettre
5. 📊 Voir mes statistiques
6. ❌ Quitter

Votre choix : _
```

### 2. Deviner un nombre (1-100)
**Principe :** L'ordinateur choisit un nombre, le joueur devine avec des indices.

**Règles :**
- Nombre entre 1 et 100
- Maximum 7 essais
- Indices : "Plus grand" ou "Plus petit"
- Option d'abandon avec "0"

**Exemple d'exécution :**
```
🔢 DEVINER UN NOMBRE
Je pense à un nombre entre 1 et 100
Vous avez 7 essais (tapez 0 pour abandonner)

Essai 1/7 : 50
📈 Plus grand !

Essai 2/7 : 75
📉 Plus petit !

Essai 3/7 : 60
📉 Plus petit !

Essai 4/7 : 55
🎉 Bravo ! Trouvé en 4 essais !
```

### 3. Lancer les dés
**Principe :** Simuler des lancers de dés jusqu'à obtenir un double.

**Règles :**
- 2 dés de 6 faces
- Continue jusqu'à obtenir un double (ex: 3-3, 5-5)
- Compte le nombre de lancers nécessaires
- Affiche chaque lancer

**Exemple d'exécution :**
```
🎲 LANCER LES DÉS
Objectif : Obtenir un double !

Lancer 1 : 🎲 4 - 🎲 2
Lancer 2 : 🎲 1 - 🎲 6
Lancer 3 : 🎲 5 - 🎲 3
Lancer 4 : 🎲 2 - 🎲 2
🎉 Double obtenu en 4 lancers !
```

### 4. Quiz de calcul mental
**Principe :** Répondre à des opérations jusqu'à faire 3 erreurs.

**Règles :**
- Additions et soustractions aléatoires
- Continue tant que moins de 3 erreurs
- Possibilité de passer une question (tapez "p")
- Affiche le score en continu

**Exemple d'exécution :**
```
💯 QUIZ DE CALCUL MENTAL
(Tapez 'p' pour passer une question)

Question 1 : 15 + 23 = ? 38
✅ Correct ! Score : 1 | Erreurs : 0

Question 2 : 45 - 12 = ? 30
❌ Faux ! C'était 33. Erreurs : 1

Question 3 : 8 + 17 = ? p
⏭️ Question passée.

Question 4 : 34 - 9 = ? 25
✅ Correct ! Score : 2 | Erreurs : 1

[... continue jusqu'à 3 erreurs]

💀 3 erreurs ! Fin du quiz.
Score final : 8 bonnes réponses
```

### 5. Deviner la lettre
**Principe :** Deviner une lettre de l'alphabet avec des indices.

**Règles :**
- Lettre entre A et Z
- Indices : "Avant" ou "Après" dans l'alphabet
- Maximum 10 essais
- Validation des entrées (une seule lettre)

**Exemple d'exécution :**
```
🔤 DEVINER LA LETTRE
Je pense à une lettre entre A et Z

Essai 1/10 : M
📈 C'est après dans l'alphabet !

Essai 2/10 : T
📉 C'est avant !

Essai 3/10 : P
📈 C'est après !

Essai 4/10 : R
🎉 Bravo ! La lettre était R !
```

### 6. Statistiques
**Affichage :**
- Nombre de parties jouées par jeu
- Taux de réussite
- Meilleur score pour chaque jeu

---

## 💻 Spécifications Techniques

### Utilisation du `while`
```python
# Menu principal - boucle infinie jusqu'au choix 6
continuer = True
while continuer:
    # Afficher menu
    choix = int(input("Votre choix : "))
    
    if choix == 6:
        continuer = False  # Sortie propre
    # ... autres options

# Jeu avec nombre d'essais limité
essais = 0
max_essais = 7
trouve = False

while essais < max_essais and not trouve:
    # Logique du jeu
    essais += 1
```

### Utilisation du `break`
```python
# Sortie immédiate de la boucle
while True:
    reponse = int(input("Votre nombre : "))
    
    if reponse == 0:
        print("Abandon !")
        break  # Sort immédiatement
    
    # Suite du code...

# Quiz avec limite d'erreurs
erreurs = 0
while True:
    # Poser question
    
    if erreurs >= 3:
        print("Trop d'erreurs !")
        break  # Fin du quiz
```

### Utilisation du `continue`
```python
# Passer à l'itération suivante
while True:
    reponse = input("Votre réponse (ou 'p' pour passer) : ")
    
    if reponse == 'p':
        print("Question passée")
        continue  # Saute le reste et reboucle
    
    # Vérification de la réponse...

# Validation d'entrée
while True:
    lettre = input("Entrez une lettre : ").upper()
    
    if len(lettre) != 1:
        print("❌ Une seule lettre !")
        continue  # Redemande sans exécuter la suite
    
    if not lettre.isalpha():
        print("❌ Doit être une lettre !")
        continue
    
    # Entrée valide, on continue
    break
```

### Utilisation du `pass`
```python
# Placeholder pour code futur
if choix == 5:
    # TODO: Implémenter les statistiques plus tard
    pass

# Dans une validation complexe
while True:
    entree = input("Votre choix : ")
    
    if entree.isdigit():
        pass  # Entrée valide, on continue
    else:
        print("Doit être un nombre !")
        continue
    
    # Traitement de l'entrée valide
```

---

## 🎮 Exemple d'Exécution Complète

```
🎮 JEU DE DEVINETTES
====================
1. 🔢 Deviner un nombre
2. 🎲 Lancer les dés
3. 💯 Quiz de calcul mental
4. 🔤 Deviner la lettre
5. 📊 Voir mes statistiques
6. ❌ Quitter

Votre choix : 3

💯 QUIZ DE CALCUL MENTAL
(Tapez 'p' pour passer une question)

Question 1 : 23 + 15 = ? 38
✅ Correct ! Score : 1 | Erreurs : 0

Question 2 : 45 - 18 = ? p
⏭️ Question passée.

Question 3 : 12 + 31 = ? 43
✅ Correct ! Score : 2 | Erreurs : 0

Question 4 : 67 - 29 = ? 40
❌ Faux ! C'était 38. Erreurs : 1

Question 5 : 8 + 14 = ? 22
✅ Correct ! Score : 3 | Erreurs : 1

Question 6 : 51 - 27 = ? 20
❌ Faux ! C'était 24. Erreurs : 2

Question 7 : 19 + 33 = ? 52
✅ Correct ! Score : 4 | Erreurs : 2

Question 8 : 78 - 45 = ? 30
❌ Faux ! C'était 33. Erreurs : 3

💀 3 erreurs ! Fin du quiz.
Score final : 4 bonnes réponses

🎮 JEU DE DEVINETTES
====================
1. 🔢 Deviner un nombre
2. 🎲 Lancer les dés
3. 💯 Quiz de calcul mental
4. 🔤 Deviner la lettre
5. 📊 Voir mes statistiques
6. ❌ Quitter

Votre choix : 6

👋 Merci d'avoir joué ! À bientôt !
```

---

## 🔧 Contraintes Techniques

### Obligatoires
- **Menu principal** : Boucle `while` infinie avec sortie propre
- **Au moins 2 utilisations de `break`** : Sortie anticipée de boucle
- **Au moins 2 utilisations de `continue`** : Passage d'itération
- **Au moins 1 utilisation de `pass`** : Placeholder ou logique vide
- **Validation des entrées** : Vérifier les inputs utilisateur
- **Compteurs et statistiques** : Variables pour tracker les performances

### Interdites
- Fonctions définies par l'utilisateur
- Structures de données avancées (listes, dictionnaires)
- Modules externes sauf `random` (voir section dédiée)

### Recommandées
- Messages d'erreur explicites
- Affichage coloré avec emojis
- Retour au menu après chaque jeu
- Confirmations pour les actions importantes

---

## 🏆 Critères d'Évaluation

| Critère | Points | Description |
|---------|---------|------------|
| **Boucle while** | 25 | Menu persistant et jeux fonctionnels |
| **Break** | 20 | Sorties anticipées appropriées |
| **Continue** | 20 | Sauts d'itération logiques |
| **Pass** | 10 | Utilisation correcte (placeholder) |
| **Validation** | 15 | Gestion des entrées incorrectes |
| **Logique jeu** | 10 | Règles respectées et fonctionnelles |

**Total : 100 points**

---

##  Extensions Possibles

### Niveau Intermédiaire
- Système de vies avec régénération
- Niveaux de difficulté (facile/moyen/difficile)
- Chronomètre pour les réponses

### Niveau Avancé
- Sauvegarde des statistiques entre sessions
- Classement des meilleurs scores
- Mode multijoueur à tour de rôle

---

## 🎲 Utilisation de `random` - Guide Simplifié

### Qu'est-ce que `random` ?
`random` est un outil Python qui génère des nombres aléatoires (au hasard). Pour l'utiliser, ajoutez cette ligne **au début** de votre programme :

```python
import random
```

### Les fonctions dont vous avez besoin

#### 1. `random.randint(a, b)` - Nombre entier au hasard
Génère un nombre entier entre `a` et `b` (inclus).

```python
import random

# Nombre entre 1 et 100
nombre_secret = random.randint(1, 100)
print(nombre_secret)  # Exemple : 47

# Lancer un dé (1 à 6)
de = random.randint(1, 6)
print(f"🎲 {de}")  # Exemple : 🎲 3
```

#### 2. `random.choice()` - Choisir dans une séquence
Choisit un élément au hasard dans une chaîne ou séquence.

```python
import random

# Lettre aléatoire de A à Z
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettre = random.choice(alphabet)
print(lettre)  # Exemple : M

# Opérateur aléatoire
operateur = random.choice("+-")
print(operateur)  # Exemple : +
```

### Exemples pour votre projet

#### Deviner un nombre
```python
import random

# Au début du jeu
nombre_secret = random.randint(1, 100)
print("Je pense à un nombre entre 1 et 100...")

# Le joueur devine
proposition = int(input("Votre nombre : "))

if proposition == nombre_secret:
    print("🎉 Gagné !")
elif proposition < nombre_secret:
    print("📈 Plus grand !")
else:
    print("📉 Plus petit !")
```

#### Lancer deux dés
```python
import random

de1 = random.randint(1, 6)
de2 = random.randint(1, 6)

print(f"🎲 {de1} - 🎲 {de2}")

if de1 == de2:
    print("🎉 Double !")
```

#### Quiz de calcul
```python
import random

# Générer une question aléatoire
nombre1 = random.randint(1, 50)
nombre2 = random.randint(1, 50)
operateur = random.choice("+-")

# Calculer la bonne réponse
if operateur == "+":
    resultat = nombre1 + nombre2
else:
    resultat = nombre1 - nombre2

# Poser la question
print(f"Combien fait {nombre1} {operateur} {nombre2} ?")
reponse = int(input("Votre réponse : "))

if reponse == resultat:
    print("✅ Correct !")
else:
    print(f"❌ Faux ! C'était {resultat}")
```

#### Deviner une lettre
```python
import random

# Choisir une lettre au hasard
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettre_secrete = random.choice(alphabet)

# Le joueur devine
proposition = input("Quelle lettre ? ").upper()

if proposition == lettre_secrete:
    print("🎉 Trouvé !")
elif proposition < lettre_secrete:
    print("📈 C'est après dans l'alphabet")
else:
    print("📉 C'est avant dans l'alphabet")
```

### 💡 Points importants

1. **Mettez `import random` une seule fois** au tout début du programme
2. **Chaque appel génère un nouveau nombre** aléatoire
3. **`randint(1, 6)` inclut 1 ET 6** dans les possibilités
4. **Les lettres se comparent** : `"A" < "M" < "Z"`

### ⚠️ Erreurs fréquentes

```python
# ❌ FAUX - Oubli de import
nombre = random.randint(1, 100)  # Erreur !

# ✅ BON - Import au début
import random
nombre = random.randint(1, 100)

# ❌ FAUX - Mauvaise syntaxe
nombre = random.randint(1-100)

# ✅ BON - Virgule entre les nombres
nombre = random.randint(1, 100)
```

---

## 📚 Aide Mémoire

### Structure de base avec while
```python
# Boucle avec condition
compteur = 0
while compteur < 10:
    # Code
    compteur += 1

# Boucle infinie avec break
while True:
    action = input("Action : ")
    if action == "quitter":
        break

# Boucle avec continue
tentatives = 0
while tentatives < 5:
    reponse = input("Réponse : ")
    tentatives += 1
    
    if reponse == "":
        continue  # Saute si vide
    
    # Traite la réponse
```

### Différences clés
- **break** : Sort complètement de la boucle
- **continue** : Passe directement à l'itération suivante
- **pass** : Ne fait rien, permet d'avoir un bloc vide

---

**Durée estimée :** 5-7 heures  
**Niveau :** Débutant-Intermédiaire  
**Prérequis :** Variables, boucles for, conditions, expressions