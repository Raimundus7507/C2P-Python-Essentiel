# Calculateur de Taxi-Moto - Défi Simple (15 minutes)

## Objectif

Créer **3 fonctions seulement** pour calculer le prix d'une course de taxi-moto, en utilisant les 3 types de paramètres vus en cours.

---

## ⚙️ Les 3 fonctions à créer

### 1. **`calculer_prix_base(distance)`**
- **Paramètre REQUIS** : `distance` en km
- Prix fixe : 100 FCFA par km
- Retourne le prix de base

### 2. **`ajouter_supplements(prix_base, heure_pointe=False, bagages=0)`**
- **Paramètre REQUIS** : `prix_base`  
- **Paramètres PAR DÉFAUT** : `heure_pointe` et `bagages`
- Si `heure_pointe=True` : +50% du prix
- Bagages : +100 FCFA par bagage
- Retourne le prix avec suppléments

### 3. **`afficher_facture(distance, prix_final, avec_details=True)`**
- **Paramètres REQUIS** : `distance` et `prix_final`
- **Paramètre PAR DÉFAUT** : `avec_details`
- Si `avec_details=True` : affiche le détail du calcul
- Sinon : affiche juste le prix final

---

## Exemple d'exécution

```python
# Ce que votre programme doit pouvoir faire :

# Test 1: Course simple (paramètre requis seulement)
prix1 = calculer_prix_base(5)
prix1_final = ajouter_supplements(prix1)
afficher_facture(5, prix1_final)

# Test 2: Course avec suppléments (paramètres par défaut modifiés)  
prix2 = calculer_prix_base(8)
prix2_final = ajouter_supplements(prix2, heure_pointe=True, bagages=2)
afficher_facture(8, prix2_final)

# Test 3: Utilisation des paramètres nommés dans le désordre
prix3 = calculer_prix_base(distance=3)
prix3_final = ajouter_supplements(bagages=1, prix_base=prix3, heure_pointe=False)
afficher_facture(prix_final=prix3_final, distance=3, avec_details=False)
```

**Sortie attendue :**
```
═══ FACTURE TAXI-MOTO ═══
Distance: 5 km
Prix de base: 500 FCFA (100 FCFA/km)
Suppléments: 0 FCFA
TOTAL À PAYER: 500 FCFA
═══════════════════════

═══ FACTURE TAXI-MOTO ═══
Distance: 8 km  
Prix de base: 800 FCFA (100 FCFA/km)
Heure de pointe: +400 FCFA
Bagages (2): +200 FCFA
TOTAL À PAYER: 1400 FCFA
═══════════════════════

TOTAL À PAYER: 400 FCFA
```

---

## ✅ Ce que vous devez démontrer

### Paramètres REQUIS :
- `calculer_prix_base(5)` ✅
- Essayer `calculer_prix_base()` sans paramètre → ERREUR ✅

### Paramètres PAR DÉFAUT :
- `ajouter_supplements(prix)` → utilise les valeurs par défaut ✅
- `ajouter_supplements(prix, heure_pointe=True)` → modifie un paramètre ✅

### Paramètres NOMMÉS :
- `afficher_facture(distance=3, prix_final=300)` → ordre différent ✅
- `ajouter_supplements(bagages=2, prix_base=500)` → noms explicites ✅

---

## 🏆 Critères de réussite

**Vous avez réussi si :**
- 🟢 Les 3 fonctions fonctionnent correctement
- 🟢 Vous utilisez au moins 1 fois chaque type de paramètre
- 🟢 Le programme affiche des résultats cohérents
- 🟢 Vous pouvez appeler les fonctions dans le désordre avec les noms

**Temps estimé : 15 minutes maximum**

---

## Pour aller plus loin (bonus)

Si vous finissez rapidement :
- Tester avec des distances négatives
- Ajouter un paramètre `reduction_etudiant=False`
- Créer 2-3 courses différentes

---

*Défi simple mais complet pour maîtriser les types de paramètres !*