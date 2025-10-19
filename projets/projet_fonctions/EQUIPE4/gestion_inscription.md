# 🎓 Projet Fonctions : Gestionnaire d'Inscription Scolaire

## Objectif
Créer un système de gestion d'inscription pour un établissement scolaire qui utilise les fonctions Python.

## Fonctionnalités requises

### 1. Menu principal persistant
```
GESTIONNAIRE D'INSCRIPTION SCOLAIRE
===================================
1. Inscrire un élève
2. Consulter l'élève actuel
3. Modifier les informations
4. Calculer les frais
5. Voir les statistiques
6. Quitter
```

### 2. Inscription d'un élève
- Nom, prénom, âge
- Classe (6ème, 5ème, 4ème, 3ème, 2nde, 1ère, Terminale)
- Type d'établissement (public, privé, technique)
- Type de bourse (excellence, sociale, familiale, aucune)

### 3. Consulter l'élève actuel
- Afficher toutes les informations de l'élève inscrit
- Montrer les frais calculés
- Indiquer si l'inscription est complète

### 4. Modifier les informations
- Changer le nom, prénom, âge
- Modifier la classe ou l'établissement
- Changer le type de bourse
- Recalculer automatiquement les frais

### 5. Calculer les frais
- Afficher le détail des frais
- Montrer les réductions appliquées
- Calculer le total à payer
- Proposer des options de paiement

### 6. Voir les statistiques
- Nombre total d'inscrits
- Effectif par classe
- Recettes totales
- Répartition des bourses
- Graphique simple des effectifs

## Contraintes techniques

### Fonctions obligatoires
- **4 types de fonctions** : avec/sans argument, avec/sans retour
- **Paramètres par défaut** : bourse="aucune"
- **Paramètres mot-clé** : nom="", classe=""
- **Variables globales** : compteurs, effectifs
- **Mot-clé global** : pour modifier les variables globales dans les fonctions

### Exemple de fonctions
```python
def inscrire_eleve(nom, prenom, age, classe, etablissement, bourse="aucune"):
    # Inscription avec paramètre par défaut

def calculer_frais(classe, etablissement, bourse):
    # Calcul et retour des frais
    return total_frais

def afficher_menu():
    # Affichage sans argument ni retour

def verifier_disponibilite(classe):
    # Vérification avec retour booléen
    return disponible
```

### Gestion des données
- Variables simples (pas de listes)
- Compteurs globaux pour les statistiques
- Effectif maximum par classe : 45 élèves

### Gestion d'exception obligatoire
- **try/except ValueError** pour toutes les saisies numériques
- Validation des entrées utilisateur
- Messages d'erreur explicites

### Exemple de gestion d'exception
```python
def saisir_age():
    while True:
        try:
            age = int(input("Âge : "))
            if age < 10 or age > 25:
                print("Âge invalide ! Entre 10 et 25 ans.")
                continue
            return age
        except ValueError:
            print("Erreur ! Entrez un nombre valide.")
```

## Astuces et exemples de code

### Variables globales à déclarer
```python
# Variables globales
nombre_total_inscrits = 0
effectif_6eme = 0
effectif_5eme = 0
effectif_4eme = 0
effectif_3eme = 0
effectif_2nde = 0
effectif_1ere = 0
effectif_terminale = 0
recettes_totales = 0
```

### Exemple de fonction avec global
```python
def inscrire_eleve(nom, prenom, age, classe, etablissement, bourse="aucune"):
    global nombre_total_inscrits, recettes_totales
    global effectif_6eme, effectif_5eme, effectif_4eme, effectif_3eme
    global effectif_2nde, effectif_1ere, effectif_terminale
    
    # Inscription de l'élève
    nombre_total_inscrits += 1
    
    # Mise à jour de l'effectif par classe
    if classe == "6ème":
        effectif_6eme += 1
    elif classe == "5ème":
        effectif_5eme += 1
    # ... etc pour chaque classe
    
    # Calcul des frais et mise à jour des recettes
    frais = calculer_frais(classe, etablissement, bourse)
    recettes_totales += frais
```

### Exemple de fonction de modification
```python
def modifier_eleve(nouvelle_classe, ancienne_classe):
    global effectif_6eme, effectif_5eme, effectif_4eme, effectif_3eme
    global effectif_2nde, effectif_1ere, effectif_terminale
    
    # Diminuer l'effectif de l'ancienne classe
    if ancienne_classe == "6ème":
        effectif_6eme -= 1
    elif ancienne_classe == "5ème":
        effectif_5eme -= 1
    # ... etc
    
    # Augmenter l'effectif de la nouvelle classe
    if nouvelle_classe == "6ème":
        effectif_6eme += 1
    elif nouvelle_classe == "5ème":
        effectif_5eme += 1
    # ... etc
```

### Exemple de fonction de calcul
```python
def calculer_frais(classe, etablissement, bourse):
    global recettes_totales
    
    # Calcul des frais
    frais_base = 35000 if etablissement == "privé" else 0
    reduction = 0.5 if bourse == "excellence" else 0.3 if bourse == "sociale" else 0.2 if bourse == "familiale" else 0
    frais_final = frais_base * (1 - reduction) + 2000  # + frais APE
    
    # Mise à jour des recettes
    recettes_totales += frais_final
    
    return frais_final
```

### 📋 Règle importante pour global
**Utilisez `global` SEULEMENT quand vous voulez MODIFIER une variable globale dans une fonction.**

- ✅ **Avec global** : `global nombre_total_inscrits` puis `nombre_total_inscrits += 1`
- ❌ **Sans global** : `print(nombre_total_inscrits)` (juste lecture)

### Exemples de fonctions SANS global
```python
def afficher_menu():
    # Pas de global nécessaire - juste affichage

def consulter_eleve():
    # Pas de global nécessaire - juste consultation

def verifier_disponibilite(classe):
    # Pas de global nécessaire - juste vérification
    return effectif_6eme < 45  # Utilise la variable globale sans la modifier
```

## Critères d'évaluation

| Critère | Points | Description |
|---------|--------|-------------|
| **Fonctions** | 30 | 4 types + paramètres + variables globales |
| **Logique métier** | 25 | Calculs, validations, statistiques |
| **Interface** | 15 | Menu, affichage, interaction |
| **Gestion erreurs** | 10 | try/except + messages d'erreur |
| **Documentation** | 10 | Fichier Documentation.md du projet |
| **Présentation** | 10 | Présentation orale en ligne |

**Total : 100 points**

### 📋 **Détail des critères**

#### **Fonctions (30 points)**
- 4 types de fonctions implémentés
- Paramètres par défaut et mot-clé
- Variables globales et mot-clé `global`
- Appels de fonctions corrects

#### **Logique métier (25 points)**
- Calculs des frais selon les règles
- Gestion des bourses et réductions
- Statistiques et compteurs
- Validation des données métier

#### **Interface (15 points)**
- Menu principal fonctionnel
- Affichage clair et organisé
- Navigation entre les options
- Messages utilisateur explicites

#### **Gestion erreurs (10 points)**
- try/except ValueError pour les saisies
- Messages d'erreur appropriés
- Gestion des cas limites
- Robustesse du programme

#### **Documentation (10 points)**
- Fichier `Documentation.md` présent
- Description complète du projet
- Processus de travail expliqué
- Difficultés et solutions

#### **Présentation (10 points)**
- Démonstration en direct
- Explication du code
- Réponses aux questions
- Qualité de la présentation

## Exemple d'exécution complète

```
GESTIONNAIRE D'INSCRIPTION SCOLAIRE
===================================

1. Inscrire un élève
2. Consulter l'élève actuel
3. Modifier les informations
4. Calculer les frais
5. Voir les statistiques
6. Quitter

Votre choix : 1

INSCRIPTION D'UN NOUVEL ÉLÈVE
Nom : PASCAL
Prénom : Paskod
Âge : 16
Classe : 1ère
Établissement : privé
Type de bourse : excellence

FRAIS CALCULÉS
Frais de base : 35000 FCFA
Réduction bourse : -17500 FCFA
Frais APE : 2000 FCFA
Total : 19500 FCFA

Élève inscrit avec succès !

GESTIONNAIRE D'INSCRIPTION SCOLAIRE
===================================

1. Inscrire un élève
2. Consulter l'élève actuel
3. Modifier les informations
4. Calculer les frais
5. Voir les statistiques
6. Quitter

Votre choix : 2

CONSULTATION DE L'ÉLÈVE ACTUEL
==============================
Nom : PASCAL
Prénom : Paskod
Âge : 16 ans
Classe : 1ère
Établissement : privé
Type de bourse : excellence
Frais totaux : 19500 FCFA
Statut : Inscription complète

GESTIONNAIRE D'INSCRIPTION SCOLAIRE
===================================

1. Inscrire un élève
2. Consulter l'élève actuel
3. Modifier les informations
4. Calculer les frais
5. Voir les statistiques
6. Quitter

Votre choix : 3

MODIFICATION DES INFORMATIONS
============================
Nom actuel : PASCAL
Nouveau nom : PASS
Prénom actuel : Paskod
Nouveau prénom : Kod
Âge actuel : 16
Nouvel âge : 17
Classe actuelle : 1ère
Nouvelle classe : Terminale
Établissement actuel : privé
Nouvel établissement : privé
Type de bourse actuel : excellence
Nouveau type de bourse : sociale

INFORMATIONS MODIFIÉES AVEC SUCCÈS !

GESTIONNAIRE D'INSCRIPTION SCOLAIRE
===================================

1. Inscrire un élève
2. Consulter l'élève actuel
3. Modifier les informations
4. Calculer les frais
5. Voir les statistiques
6. Quitter

Votre choix : 4

CALCUL DÉTAILLÉ DES FRAIS
=========================
Classe : Terminale
Établissement : privé
Type de bourse : sociale

DÉTAIL DES FRAIS :
- Frais de base : 40000 FCFA
- Réduction bourse (30%) : -12000 FCFA
- Frais APE : 2000 FCFA
- Cantine : 1500 FCFA
- Transport : 1000 FCFA
- Total à payer : 30500 FCFA

GESTIONNAIRE D'INSCRIPTION SCOLAIRE
===================================

1. Inscrire un élève
2. Consulter l'élève actuel
3. Modifier les informations
4. Calculer les frais
5. Voir les statistiques
6. Quitter

Votre choix : 5

STATISTIQUES GÉNÉRALES
======================
Nombre total d'inscrits : 1
Effectif par classe :
- 6ème : 0 élèves
- 5ème : 0 élèves
- 4ème : 0 élèves
- 3ème : 0 élèves
- 2nde : 0 élèves
- 1ère : 0 élèves
- Terminale : 1 élève

Recettes totales : 30500 FCFA
Répartition des bourses :
- Excellence : 0 élèves
- Sociale : 1 élève
- Familiale : 0 élèves
- Aucune : 0 élèves

GESTIONNAIRE D'INSCRIPTION SCOLAIRE
===================================

1. Inscrire un élève
2. Consulter l'élève actuel
3. Modifier les informations
4. Calculer les frais
5. Voir les statistiques
6. Quitter

Votre choix : 6

Merci d'avoir utilisé le gestionnaire d'inscription !
```

## Conseils
- Testez chaque fonction séparément
- Utilisez des noms de variables clairs
- Gérer les cas d'erreur (âge invalide, classe pleine)
- Afficher des messages explicites

**Bon codage !**