# Projet Python : Générateur de Motifs Visuels

## 📋 Cahier des Charges

### Objectif
Développer un programme Python qui génère différents motifs visuels en utilisant les structures de contrôle et les boucles.

### Compétences visées
- Maîtrise des structures conditionnelles (`if`/`elif`/`else`)
- Utilisation des boucles `for` avec `range()`
- Implementation de boucles imbriquées
- Application des expressions arithmétiques et logiques

---

## Fonctionnalités Requises

### 1. Menu Principal
Le programme doit proposer un menu interactif avec 5 options :

```
GÉNÉRATEUR DE MOTIFS
=======================
1. Rectangle d'étoiles
2. Triangle de nombres
3. Pyramide centrée
4. Damier alternant
5. Table multiplication visuelle
```

### 2. Rectangle d'étoiles
**Input :** Largeur et hauteur  
**Output :** Rectangle rempli d'étoiles

**Exemple :**
```
Largeur : 6
Hauteur : 4

Résultat :
******
******
******
******
```

### 3. Triangle de nombres
**Input :** Taille du triangle  
**Output :** Triangle croissant avec numérotation

**Exemple :**
```
Taille : 5

Résultat :
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
```

### 4. Pyramide centrée
**Input :** Hauteur de la pyramide  
**Output :** Pyramide d'étoiles centrée

**Exemple :**
```
Hauteur : 5

Résultat :
    *
   ***
  *****
 *******
*********
```

### 5. Damier alternant
**Input :** Taille du damier  
**Output :** Grille avec alternance de symboles

**Exemple :**
```
Taille : 4

Résultat :
■ □ ■ □ 
□ ■ □ ■ 
■ □ ■ □ 
□ ■ □ ■ 
```

### 6. Table multiplication visuelle
**Input :** Numéro de table et limite  
**Output :** Table avec représentation graphique

**Exemple :**
```
Table : 3
Limite : 4

Résultat :
3 x 1 = 3   •••
3 x 2 = 6   ••••••
3 x 3 = 9   •••••••••
3 x 4 = 12  ••••••••••••
```

---

## 💻 Spécifications Techniques

### Structures de données
- Variables simples (int, str)
- Pas d'utilisation de listes ou fonctions

### Logique de contrôle
```python
# Menu principal
choix = int(input("Votre choix : "))

if choix == 1:
    # Rectangle
elif choix == 2:
    # Triangle
# ... etc

# Exemple boucle imbriquée pour damier
for ligne in range(taille):
    for colonne in range(taille):
        if (ligne + colonne) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()
```

### Calculs requis
- **Pyramide :** `espaces = hauteur - ligne - 1`
- **Pyramide :** `etoiles = 2 * ligne + 1`
- **Damier :** `(ligne + colonne) % 2 == 0`

---

## 🎮 Exemples d'Exécution

### Exécution complète - Option 3 (Pyramide)
```
🎨 GÉNÉRATEUR DE MOTIFS
=======================
1. Rectangle d'étoiles
2. Triangle de nombres
3. Pyramide centrée
4. Damier alternant
5. Table multiplication visuelle

Votre choix : 3

🔺 PYRAMIDE CENTRÉE
Hauteur : 6

      *
     ***
    *****
   *******
  *********
 ***********

🎉 Merci d'avoir utilisé le générateur !
```

### Exécution complète - Option 4 (Damier)
```
🎨 GÉNÉRATEUR DE MOTIFS
=======================
1. Rectangle d'étoiles
2. Triangle de nombres
3. Pyramide centrée
4. Damier alternant
5. Table multiplication visuelle

Votre choix : 4

🏁 DAMIER
Taille : 6

■ □ ■ □ ■ □ 
□ ■ □ ■ □ ■ 
■ □ ■ □ ■ □ 
□ ■ □ ■ □ ■ 
■ □ ■ □ ■ □ 
□ ■ □ ■ □ ■ 

🎉 Merci d'avoir utilisé le générateur !
```

---

## 🔧 Contraintes Techniques

### Obligatoires
- Utilisation de `if`/`elif`/`else` pour le menu
- Minimum 2 niveaux de boucles imbriquées
- Application des 3 types de `range()` : `range(n)`, `range(a,b)`, `range(a,b,step)`
- Gestion du cas "choix invalide"

### Interdites
- Fonctions définies par l'utilisateur
- Imports de modules (sauf si nécessaire pour bonus)
- Structures de données avancées (listes, dictionnaires)

### Recommandées
- Formatage soigné avec `print()` et `end=""`
- Utilisation d'emojis pour l'interface
- Messages utilisateur clairs

---

## 🏆 Critères d'Évaluation

| Critère | Points | Description |
|---------|---------|------------|
| **Menu fonctionnel** | 20 | Navigation complète entre options |
| **Boucles simples** | 15 | Maîtrise des `for` avec `range()` |
| **Boucles imbriquées** | 25 | Implementation correcte ligne/colonne |
| **Conditions** | 20 | Logique `if`/`elif`/`else` appropriée |
| **Calculs** | 10 | Expressions arithmétiques justes |
| **Présentation** | 10 | Affichage soigné et professionnel |

**Total : 100 points**

---

## Extensions Possibles

### Niveau Intermédiaire
- Triangle inversé avec `range(n, 0, -1)`
- Losange (pyramide + pyramide inversée)
- Patterns avec lettres de l'alphabet

### Niveau Avancé  
- Sauvegarde des motifs créés
- Motifs colorés avec codes ANSI
- Génération de motifs aléatoires

---

## 📚 Ressources

### Concepts Clés
- **Boucles imbriquées :** Une boucle dans une autre boucle
- **range() :** Générateur de séquences numériques
- **Expressions modulo :** `%` pour alternance et patterns
- **Formatage d'affichage :** `end=""` pour contrôler les retours ligne

### Aide Mémoire
```python
# Les 3 types de range()
range(5)        # 0, 1, 2, 3, 4
range(2, 7)     # 2, 3, 4, 5, 6  
range(1, 10, 2) # 1, 3, 5, 7, 9

# Boucle imbriquée type
for ligne in range(hauteur):
    for colonne in range(largeur):
        # Traitement position (ligne, colonne)
```

---

**Durée estimée :** 4-6 heures  
**Niveau :** Débutant-Intermédiaire  
**Prérequis :** Variables, opérateurs, input/output