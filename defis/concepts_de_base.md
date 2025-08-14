# Défis Python - Niveau Débutant

## Prérequis Techniques
- Variables et affectation
- Fonction `input()` pour la saisie
- Fonction `print()` pour l'affichage
- Règles de nommage des variables
- Affectation multiple
- Conversion de types : `str()` et `int()`

## Défi 1 : Calculateur d'Économies Personnel

**Objectif :** Créer un programme de gestion financière personnelle

**Fonctionnalités requises :**
- Saisir nom utilisateur, revenus et dépenses mensuels
- Calculer les économies mensuelles
- Calculer le taux d'épargne en pourcentage
- Afficher un bilan financier formaté

**Données d'entrée :**
- Nom (texte)
- Revenus mensuels (nombre entier en FCFA)
- Dépenses mensuelles (nombre entier en FCFA)

**Calculs à effectuer :**
```
Économies = Revenus - Dépenses
Taux d'épargne = (Économies × 100) ÷ Revenus
```

**Sortie attendue :**
```
Calculateur d'économies - Version 1.0
=====================================

Quel est votre nom ? Aminata
Revenus mensuels (FCFA) : 150000
Dépenses mensuelles (FCFA) : 120000

=== BILAN MENSUEL ===
Aminata - Revenus : 150000 FCFA
Dépenses : 120000 FCFA
Économies : 30000 FCFA
Taux d'épargne : 20%

Félicitations Aminata !
Vous économisez 30000 FCFA par mois.
```

## Défi 2 : Créateur de Profil Personnel

**Objectif :** Développer un questionnaire interactif générant un profil personnalisé

**Fonctionnalités requises :**
- Collecter des informations personnelles (nom, âge, ville)
- Recueillir les préférences (couleur, plat, sport, musique)
- Identifier les projets (métier souhaité, objectif annuel)
- Documenter les loisirs (lecture, activités weekend)
- Générer un profil structuré et personnalisé

**Structure des données :**
- **Informations de base :** 3 variables
- **Préférences personnelles :** 4 variables
- **Projets et ambitions :** 2 variables
- **Loisirs :** 3 variables

**Organisation du code :**
1. Présentation du programme
2. Collecte des informations de base
3. Collecte des préférences
4. Collecte des projets et ambitions
5. Collecte des loisirs
6. Traitement des données (affectation multiple)
7. Affichage du profil complet
8. Message de conclusion personnalisé

**Techniques utilisées :**
- Affectation multiple pour organiser les données
- Concaténation de chaînes pour les messages
- Variables intermédiaires pour l'affichage
- Séparation visuelle avec `print()`

## Critères d'Évaluation

### Code (40%)
- Variables nommées correctement
- Utilisation appropriée de `str()` et `int()`
- Structure logique du programme
- Commentaires explicatifs

### Fonctionnalité (35%)
- Toutes les saisies fonctionnent
- Calculs corrects
- Affichage conforme aux spécifications
- Programme s'exécute sans erreur

### Présentation (25%)
- Affichage propre et organisé
- Messages personnalisés
- Séparation visuelle des sections
- Expérience utilisateur claire

## Instructions de Développement

### Étapes recommandées :
1. **Analyser** le défi et identifier les variables nécessaires
2. **Structurer** le programme en sections commentées
3. **Développer** section par section
4. **Tester** après chaque section ajoutée
5. **Valider** avec différents jeux de données

### Bonnes pratiques :
- Nommer les variables de façon explicite
- Grouper les `input()` par thème
- Utiliser `print()` vide pour aérer l'affichage
- Tester avec des données réalistes
- Documenter les choix techniques

### Erreurs courantes à éviter :
- Oublier `str()` pour convertir les nombres
- Variables mal nommées (`a`, `x`, `data`)
- Affichage non structuré
- Manque de messages explicatifs pour l'utilisateur