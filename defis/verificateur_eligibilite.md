# Projet Python : Vérificateur d'éligibilité aux tranches universitaires – UL

## Contexte
À l'Université de Lomé, certaines aides ou réductions sont accordées aux étudiants qui respectent **plusieurs critères**.
L'objectif de ce projet est de créer un programme Python qui permet de **vérifier automatiquement** si un étudiant remplit ces critères.

Ce projet est conçu pour les **débutants** et utilise uniquement les notions suivantes :
- Expressions arithmétiques simples
- Expressions de comparaison (`<`, `<=`, `>=`, `==`, `!=`)
- Expressions logiques (`and`, `or`, `not`)
- Opérateurs composés (`+=`, `-=`, etc.)
- Fonction `print()`

> ❌ Aucun `if`, `else`, boucle ou fonction personnalisée n’est autorisé.

---

## Objectif du programme
Le programme doit demander des informations à l'utilisateur, puis afficher pour **chaque critère** un résultat `True` ou `False`.

### Critères à vérifier
1. **Âge** : inférieur ou égal à 22 ans  
2. **Mention au bac** : `Assez Bien`, `Bien` ou `Très Bien`  
3. **Inscription** : réponse `oui`  
4. **Nationalité** : `togolaise`

En plus, le programme doit calculer l'éligibilité générale (tous les critères doivent être vrais).

---

## Étapes de réalisation
1. **Afficher** un titre clair avec `print()`
2. **Demander** les informations suivantes à l'utilisateur avec `input()` :
   - Âge
   - Mention au bac
   - Inscrit à l'UL (oui/non)
   - Nationalité
3. **Stocker** ces réponses dans des variables aux noms clairs
4. **Créer** une expression pour chaque critère (exemple : `age <= 22`)
5. **Combiner** les critères avec `and` pour l'éligibilité générale
6. **Afficher** tous les résultats avec `print()`

---

## Exemple d'exécution
```
=== Vérificateur d'éligibilité UL ===
Âge : 20
Mention au bac : Bien
Inscrit à l'UL (oui/non) : oui
Nationalité : togolaise

--- RÉSULTATS ---
Âge ≤ 22 ans : True
Mention Bien ou Très Bien : True
Inscription UL : True
Nationalité togolaise : True

Éligibilité générale (tous critères vrais) : True

```

---

## 🏆 Défi supplémentaire
- Tester avec différents profils (changer les valeurs et observer les résultats)
- Ajouter 1 ou 2 critères inventés par vous-mêmes  
  *(ex. frais universitaires payés, moyenne générale ≥ 12)*

---

## 💡 Conseils
- Choisissez des **noms de variables clairs** (`age`, `mention`, `inscription`, `nationalite`)
- Soignez la présentation avec des séparateurs (`print("---")`)
- Testez plusieurs fois pour vérifier que les `True` et `False` s’affichent comme prévu

---

✍️ Projet créé pour **C2P – Communauté de Partage de Compétences**  


