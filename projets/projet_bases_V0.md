# Projet Python : Calculateur de Budget Personnel

Aujourd'hui, nous allons créer ensemble un **calculateur de budget personnel** ! C'est un projet parfait pour mettre en pratique tout ce que vous avez appris jusqu'ici.

## Ce que notre programme va faire

Notre calculateur va :
- Demander vos revenus mensuels
- Demander vos différentes dépenses 
- Calculer votre budget restant
- Calculer le pourcentage d'épargne
- Afficher un résumé détaillé de votre budget

### F-strings pour un affichage dynamique
```python
print(f"💰 Revenus totaux : {revenus_total:.0f} FCFA")
```
Le `:.0f` affiche sans décimales !

### Opérations mathématiques
- Addition : `+`
- Soustraction : `-`
- Multiplication : `*`
- Division : `/`
- Puissance : `**` (pour calculer les pourcentages)

### Caractères d'échappement
- `\n` : nouvelle ligne pour aérer l'affichage

### Input pour récupérer les données
```python
salaire = float(input("Entrez votre salaire mensuel (FCFA) : "))
```

## Exemple d'exécution

```
🏦 Bienvenue dans votre Calculateur de Budget Personnel ! 🏦
=======================================================

💰 ÉTAPE 1 : Vos revenus
Entrez votre salaire mensuel (FCFA) : 150000
Autres revenus mensuels (FCFA) : 25000

💸 ÉTAPE 2 : Vos dépenses  
Loyer/Location (FCFA) : 45000
Nourriture et marché (FCFA) : 35000
Transport (taxi, moto, essence) (FCFA) : 20000
Loisirs et sorties (FCFA) : 15000
Autres dépenses (santé, vêtements...) (FCFA) : 10000

=======================================================
📊 RÉSUMÉ DE VOTRE BUDGET
=======================================================
💰 Revenus totaux    : 175000 FCFA
💸 Dépenses totales  : 125000 FCFA
📈 Budget restant    : 50000 FCFA
📊 Pourcentage épargné : 28.6%

📋 RÉPARTITION DE VOS DÉPENSES :
🏠 Loyer        : 45000 FCFA (25.7% du revenu)
🛒 Nourriture   : 35000 FCFA (20.0% du revenu)
🛵 Transport    : 20000 FCFA (11.4% du revenu)
🎉 Loisirs      : 15000 FCFA (8.6% du revenu)
💼 Autres       : 10000 FCFA (5.7% du revenu)

🔢 CALCULS UTILES :
💵 Budget disponible par jour : 1667 FCFA
💎 Économies potentielles par an : 600000 FCFA
```

## 🎓 Ce vous allez retenir

Variables, calculs, affichage, f-strings, input... tout y est ! Et surtout, vous serai capable de creer votre premier vrai programme utile.

**GoooOO codezzzzzz ?**