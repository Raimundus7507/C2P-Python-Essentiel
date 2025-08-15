### Exercice : Système de recommandation film Nollywood
```python
# Profil utilisateur
age = 25
genre_prefere = "drame"
note_minimum = 7.5
duree_maximum = 120  # minutes

# Caract#  Les Expressions et Opérateurs en Python
*Cours destiné à la communauté C2P - Niveau Débutant*

---

## 📋 Introduction

Bienvenue dans ce nouveau chapitre de votre apprentissage Python ! Aujourd'hui, nous allons explorer les **expressions** - ces formules magiques qui permettent à Python de calculer, comparer et prendre des décisions logiques.

Imaginez Python comme une calculatrice ultra-puissante : elle peut non seulement faire des calculs mathématiques, mais aussi comparer des valeurs et raisonner logiquement. C'est exactement ce que nous allons apprendre !

### Ce que vous saurez faire à la fin de ce cours :
- Effectuer tous types de calculs mathématiques
- Comparer des valeurs entre elles  
- Combiner des conditions logiques
- Utiliser des raccourcis pour modifier vos variables
- Résoudre des problèmes concrets du quotidien

---

## 1. Les Expressions Arithmétiques

### Objectif
Maîtriser les opérations mathématiques de base pour résoudre des problèmes concrets.

### Les opérateurs de base

#### ➕ Addition (`+`)
L'addition fonctionne exactement comme vous l'imaginez :

```python
# Calcul simple
resultat = 10 + 5
print(resultat)  # Affiche : 15

# Exemple concret : addition de prix
prix_livre = 2500  # en FCFA
prix_stylo = 500   # en FCFA
total = prix_livre + prix_stylo
print(f"Total à payer : {total} FCFA")  # Affiche : Total à payer : 3000 FCFA
```

#### ➖ Soustraction (`-`)
```python
# Calcul de monnaie rendue
argent_donne = 5000  # en FCFA
prix_achat = 3200    # en FCFA
monnaie = argent_donne - prix_achat
print(f"Votre monnaie : {monnaie} FCFA")  # Affiche : Votre monnaie : 1800 FCFA

# Calcul d'âge
annee_actuelle = 2025
annee_naissance = 1995
age = annee_actuelle - annee_naissance
print(f"Vous avez {age} ans")  # Affiche : Vous avez 30 ans
```

#### ✖️ Multiplication (`*`)
```python
# Calcul de surface
longueur = 5.5
largeur = 3.2
surface = longueur * largeur
print(f"Surface : {surface} m²")  # Affiche : Surface : 17.6 m²

# Prix total pour plusieurs articles
prix_unitaire = 1500  # Prix d'un pagne en FCFA
quantite = 3
prix_total = prix_unitaire * quantite
print(f"Prix total : {prix_total} FCFA")  # Affiche : Prix total : 4500 FCFA
```

#### ➗ Division (`/`)
⚠️ **Important** : La division en Python donne toujours un nombre décimal (float)

```python
# Partage équitable
attieke_portions = 8  # Portions d'attiéké
nb_personnes = 3
portions_par_personne = attieke_portions / nb_personnes
print(f"Portions par personne : {portions_par_personne}")  # Affiche : 2.6666666666666665

# Calcul de moyenne
note1 = 15
note2 = 12
note3 = 18
moyenne = (note1 + note2 + note3) / 3
print(f"Moyenne : {moyenne}")  # Affiche : 15.0
```

#### 🔢 Division entière (`//`)
Cette division ne garde que la partie entière du résultat :

```python
# Nombre de groupes complets
total_eleves = 23
eleves_par_groupe = 4
nb_groupes_complets = total_eleves // eleves_par_groupe
print(f"Groupes complets : {nb_groupes_complets}")  # Affiche : 5

# Conversion heures en jours
total_heures = 50
heures_par_jour = 24
nb_jours = total_heures // heures_par_jour
print(f"Nombre de jours : {nb_jours}")  # Affiche : 2
```

#### 🔄 Modulo (`%`)
Le modulo donne le **reste** de la division :

```python
# Élèves restants après formation des groupes
total_eleves = 23
eleves_par_groupe = 4
eleves_restants = total_eleves % eleves_par_groupe
print(f"Élèves sans groupe : {eleves_restants}")  # Affiche : 3

# Heures restantes
total_heures = 50
heures_par_jour = 24
heures_restantes = total_heures % heures_par_jour
print(f"Heures restantes : {heures_restantes}")  # Affiche : 2
```

#### 📈 Puissance (`**`)
```python
# Calcul d'aire d'un carré
cote = 5
aire = cote ** 2
print(f"Aire du carré : {aire} cm²")  # Affiche : 25

# Calcul d'intérêts composés (simple)
capital = 500000  # 500,000 FCFA
taux = 1.03  # 3% d'intérêt
annees = 5
capital_final = capital * (taux ** annees)
print(f"Capital après {annees} ans : {capital_final:.0f} FCFA")  # Affiche : 579,637 FCFA
```

### 🔍 Ordre des opérations (priorité)
Python respecte l'ordre mathématique traditionnel :

```python
# Sans parenthèses
resultat = 2 + 3 * 4  # 3 * 4 d'abord, puis + 2
print(resultat)  # Affiche : 14

# Avec parenthèses pour changer l'ordre
resultat2 = (2 + 3) * 4  # (2 + 3) d'abord, puis * 4
print(resultat2)  # Affiche : 20

# Exemple concret : calcul TVA
prix_ht = 50000  # Prix HT (Hors Taxe) en FCFA 
taux_tva = 18    # 18% (TVA(taxe sur la valeur ajoutée) au Togo)
prix_ttc = prix_ht * (1 + taux_tva / 100) # ttc(toutes taxes comprises)
print(f"Prix TTC : {prix_ttc:.0f} FCFA")  # Affiche : 59,000 FCFA
```

### Exercice Pratique 1
**Situation** : Vous organisez une fête à Lomé. Calculez le coût total :
- 12 invités
- 750 FCFA par personne pour les boissons  
- 35000 FCFA de location de salle
- 2000 FCFA par personne pour le repas

```python
# Votre code ici :
nb_invites = 12
cout_boisson_pp = 750    # FCFA
cout_repas_pp = 2000     # FCFA
location_salle = 35000   # FCFA

<details>
<summary>Solution</summary>
```python
# Solution :
cout_boissons = nb_invites * cout_boisson_pp
cout_repas = nb_invites * cout_repas_pp
cout_total = cout_boissons + cout_repas + location_salle
print(f"Coût total de la fête : {cout_total} FCFA")  # Affiche : 68,000 FCFA
```
</details>
```

---

##  2. Les Opérateurs Arithmétiques Composés

### Objectif
Apprendre les raccourcis pour modifier des variables existantes de manière élégante et efficace.

### Le principe
Au lieu d'écrire `variable = variable + valeur`, Python propose des raccourcis !

### ➕ Addition assignée (`+=`)
```python
# Méthode longue
score = 100
score = score + 50
print(score)  # 150

# Méthode courte (équivalente)
score = 100
score += 50  # Exactement pareil que : score = score + 50
print(score)  # 150

# Exemple concret : compteur de points
points_joueur = 0
print(f"Points initiaux : {points_joueur}")

points_joueur += 10  # Premier niveau réussi
print(f"Après niveau 1 : {points_joueur}")  # 10

points_joueur += 25  # Deuxième niveau réussi
print(f"Après niveau 2 : {points_joueur}")  # 35

points_joueur += 15  # Bonus collecté
print(f"Score final : {points_joueur}")  # 50
```

### ➖ Soustraction assignée (`-=`)
```python
# Gestion d'un compte bancaire
solde = 250000  # Solde en FCFA
print(f"Solde initial : {solde} FCFA")

solde -= 15000  # Retrait distributeur
print(f"Après retrait : {solde} FCFA")  # 235,000 FCFA

solde -= 8500   # Achat au marché
print(f"Après courses : {solde} FCFA")  # 226,500 FCFA

# Gestion de stock
stock_ignames = 50
stock_ignames -= 12  # Vente de 12 ignames
print(f"Ignames restantes : {stock_ignames}")  # 38
```

### ✖️ Multiplication assignée (`*=`)
```python
# Calcul d'intérêts
capital = 500000  # Capital en FCFA
capital *= 1.05   # Augmentation de 5%
print(f"Capital après 1 an : {capital:.0f} FCFA")  # 525,000 FCFA

# Doublement de production
production_quotidienne = 100  # Sacs de riz par jour
production_quotidienne *= 2   # Production doublée
print(f"Nouvelle production : {production_quotidienne} sacs/jour")  # 200
```

### ➗ Division assignée (`/=`)
```python
# Réduction de moitié
budget = 400000  # Budget en FCFA
budget /= 2      # Division par 2
print(f"Nouveau budget : {budget:.0f} FCFA")  # 200,000 FCFA

# Calcul de moyenne progressive
total_notes = 60  # Total sur 4 notes
total_notes /= 4  # Moyenne
print(f"Moyenne : {total_notes}")  # 15.0
```

### 🔢 Division entière assignée (`//=`)
```python
# Partage en groupes
participants = 47
participants //= 5  # Nombre de groupes de 5
print(f"Groupes de 5 : {participants}")  # 9
```

### 🔄 Modulo assigné (`%=`)
```python
# Système cyclique (jour de la semaine)
jour = 15  # 15ème jour du mois
jour %= 7   # Quel jour de la semaine ? (0-6)
print(f"Jour de la semaine : {jour}")  # 1 (lundi si on commence à 0=dimanche)
```

### 📈 Puissance assignée (`**=`)
```python
# Croissance exponentielle
population = 1000
population **= 2  # Population au carré
print(f"Population théorique : {population}")  # 1000000

# Plus réaliste : taille d'un fichier qui double
taille_fichier = 1.5  # En MB
taille_fichier **= 2  # Quadruple la taille
print(f"Nouvelle taille : {taille_fichier} MB")  # 2.25 MB
```

### Exercice Pratique 2
**Situation** : Simulez l'évolution d'un compte épargne chez Ecobank :

```python
# État initial
epargne = 125000  # FCFA

# Mois 1 : dépôt de 50,000 FCFA
epargne += 50000
print(f"Après dépôt : {epargne} FCFA")

# Mois 2 : intérêts de 0.5%
epargne *= 1.005
print(f"Après intérêts : {epargne:.0f} FCFA")

# Mois 3 : retrait de 25,000 FCFA
epargne -= 25000
print(f"Après retrait : {epargne:.0f} FCFA")

# Résultat attendu : environ 150,875 FCFA
```

---

## ⚖️ 3. Les Expressions de Comparaison

### Objectif
Apprendre à comparer des valeurs pour prendre des décisions (base de la logique informatique).

### Le principe
Les comparaisons donnent toujours un résultat `True` (vrai) ou `False` (faux).

### 🟰 Égalité (`==`)
⚠️ **Attention** : `=` assigne, `==` compare !

```python
# Tests d'égalité
age = 18
print(age == 18)    # True
print(age == 20)    # False

# Exemple concret : vérification de mot de passe
mot_de_passe_saisi = "python123"
mot_de_passe_correct = "python123"
print("Mot de passe correct :", mot_de_passe_saisi == mot_de_passe_correct)  # True

# Comparaison de prix
prix_concurrent_a = 15000  # FCFA
prix_concurrent_b = 15000  # FCFA
print("Même prix :", prix_concurrent_a == prix_concurrent_b)  # True
```

### ❌ Différence (`!=`)
```python
# Tests de différence
nom_utilisateur = "Kossi"
print(nom_utilisateur != "Kossivi")  # True
print(nom_utilisateur != "Kossi")   # False

# Exemple concret : détection d'erreur
resultat_calcul = 42
resultat_attendu = 40
print("Erreur détectée :", resultat_calcul != resultat_attendu)  # True
```

### 📏 Comparaisons numériques

#### Plus petit que (`<`)
```python
# Vérifications d'âge
age_client = 16
print("Mineur :", age_client < 18)  # True

# Contrôle de stock
stock_actuel = 5
seuil_alerte = 10
print("Stock faible :", stock_actuel < seuil_alerte)  # True

# Contrôle de vitesse
vitesse = 45
limite = 50
print("Dans la limite :", vitesse < limite)  # True
```

#### Plus grand que (`>`)
```python
# Vérification de performance
score = 85
score_minimum = 60
print("Performance suffisante :", score > score_minimum)  # True

# Contrôle température
temperature = 22
temperature_confort = 20
print("Température élevée :", temperature > temperature_confort)  # True
```

#### Plus petit ou égal (`<=`)
```python
# Limite de poids bagages
poids_bagage = 23.0
limite_poids = 23.0
print("Bagage accepté :", poids_bagage <= limite_poids)  # True

# Budget respecté
depense = 75000   # FCFA
budget = 100000   # FCFA
print("Budget respecté :", depense <= budget)  # True
```

#### Plus grand ou égal (`>=`)
```python
# Accès autorisé selon l'âge
age = 18
age_minimum = 18
print("Accès autorisé :", age >= age_minimum)  # True

# Note suffisante
note = 12
note_passage = 10
print("Examen réussi :", note >= note_passage)  # True
```

### 🔤 Comparaisons de chaînes
```python
# Comparaisons de chaînes
print("apple" < "banana")    # True (a avant b)
print("Python" == "python")  # False (majuscules différentes)

# Exemple concret : tri de noms 
nom1 = "Akossi"
nom2 = "Kokou"
print(f"{nom1} vient avant {nom2} :", nom1 < nom2)  # True
```

### Exercice Pratique 3
**Situation** : Contrôles d'accès à un parc d'attractions:

```python
# Données du visiteur
age = 16
taille = 1.65  # en mètres
ticket = "standard"

# Contrôles (testez différentes valeurs)
print("Assez âgé pour la grande roue :", age >= 12)
print("Assez grand pour les montagnes russes :", taille >= 1.40)
print("Ticket valide :", ticket == "standard" or ticket == "premium")
print("Tarif réduit (moins de 12 ans) :", age < 12)

# Testez avec : age=8, taille=1.20, ticket="enfant"
```

---

## 🧠 4. Les Expressions Logiques

### Objectif
Combiner plusieurs conditions pour créer une logique complexe et prendre des décisions sophistiquées.

### Le principe
Les opérateurs logiques permettent de combiner plusieurs conditions `True` ou `False`.

### L'opérateur ET (`and`)
`and` est vrai seulement si **TOUTES** les conditions sont vraies.

```python
# Exemple simple
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Exemple concret : accès sécurisé
age = 25
permis = True
assurance = True

peut_conduire = age >= 18 and permis and assurance
print("Peut conduire :", peut_conduire)  # True

# Exemple : promotion commerciale
achat_minimum = 50000    # FCFA
client_fidele = True
code_promo = True

prix_achat = 65000  # FCFA
reduction_applicable = prix_achat >= achat_minimum and client_fidele and code_promo
print("Réduction applicable :", reduction_applicable)  # True
```

#### Table de vérité AND
```
Condition A | Condition B | A and B
    True    |    True     |   True
    True    |    False    |   False
    False   |    True     |   False
    False   |    False    |   False
```

### 🤔 L'opérateur OU (`or`)
`or` est vrai si **AU MOINS UNE** condition est vraie.

```python
# Exemple simple
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False

# Exemple concret : méthodes de paiement
paiement_mobile_money = True   # Moov Money
paiement_especes = False
paiement_carte = False

peut_payer = paiement_mobile_money or paiement_especes or paiement_carte
print("Peut payer :", peut_payer)  # True

# Exemple : conditions météo pour sortir
temps_sec = False
parapluie = True
vetements_impermeable = True

peut_sortir = temps_sec or parapluie or vetements_impermeable
print("Peut sortir :", peut_sortir)  # True
```

#### Table de vérité OR
```
Condition A | Condition B | A or B
    True    |    True     |   True
    True    |    False    |   True
    False   |    True     |   True
    False   |    False    |   False
```

### 🙅 L'opérateur NON (`not`)
`not` inverse le résultat : `True` devient `False` et vice-versa.

```python
# Exemple simple
print(not True)   # False
print(not False)  # True

# Exemple concret : jours ouvrés
weekend = True
jour_ouvre = not weekend
print("Jour ouvré :", jour_ouvre)  # False

# Exemple : stock disponible
stock_vide = False
stock_disponible = not stock_vide
print("Stock disponible :", stock_disponible)  # True

# Exemple : utilisateur connecté
utilisateur_connecte = True
utilisateur_anonyme = not utilisateur_connecte
print("Utilisateur anonyme :", utilisateur_anonyme)  # False
```

### 🔗 Combinaisons complexes
```python
# Exemple : accès à une salle de sport
age = 16
accord_parental = True
certificat_medical = True
abonnement_jour = False
abonnement_soir = True

# Mineur avec autorisation OU majeur
autorisation_age = (age < 18 and accord_parental) or (age >= 18)

# Documents OK ET abonnement valide
documents_ok = certificat_medical and (abonnement_jour or abonnement_soir)

# Accès final
acces_autorise = autorisation_age and documents_ok
print("Accès autorisé :", acces_autorise)  # True

# Décomposition du calcul :
print("Autorisation d'âge :", autorisation_age)  # True (mineur avec accord)
print("Documents OK :", documents_ok)  # True (certificat + abonnement soir)
print("Résultat final :", acces_autorise)  # True
```

### 📊 Priorités des opérateurs logiques
1. `not` (le plus prioritaire)
2. `and`
3. `or` (le moins prioritaire)

```python
# Sans parenthèses
resultat = True or False and not True
# Équivaut à : True or (False and (not True))
# Équivaut à : True or (False and False)
# Équivaut à : True or False
print(resultat)  # True

# Avec parenthèses pour clarifier
resultat2 = (True or False) and (not True)
# Équivaut à : True and False
print(resultat2)  # False
```

### Exercice Pratique 4
**Situation** : Système d'admission Université de Lomé

```python
# Profil étudiant
moyenne_generale = 14.5
note_math = 16
note_francais = 12
sport_haut_niveau = False
boursier = True

# Critères d'admission (testez différentes valeurs)
moyenne_suffisante = moyenne_generale >= 12
excellent_math = note_math >= 15
francais_correct = note_francais >= 10

# Admission possible si :
# (Moyenne suffisante ET français correct) ET (excellent en math OU sport haut niveau OU boursier)
condition_base = moyenne_suffisante and francais_correct
condition_bonus = excellent_math or sport_haut_niveau or boursier
admission = condition_base and condition_bonus

print("Moyenne suffisante :", moyenne_suffisante)
print("Français correct :", francais_correct)
print("Excellent math :", excellent_math)
print("Condition base :", condition_base)
print("Condition bonus :", condition_bonus)
print("ADMISSION :", admission)

# Résultat attendu avec ces valeurs : True
```

---

## Exercices Récapitulatifs

### Exercice 1 : Calculateur de facture restaurant
```python
# Données
prix_plat1 = 3500   # Fufu sauce arachide
prix_plat2 = 4200   # Poisson braisé
prix_dessert = 1500 # Fruits de saison
nb_couverts = 2
prix_couvert = 500  # FCFA
taux_service = 10   # 10% au Togo

# Votre code ici :
# 1. Calculez le total des plats
# 2. Ajoutez les couverts
# 3. Calculez le service (10% du total)
# 4. Calculez le total final

<details>
<summary> Solution </summary>
```python
# Solution :
total_plats = prix_plat1 + prix_plat2 + prix_dessert
total_couverts = nb_couverts * prix_couvert
sous_total = total_plats + total_couverts
service = sous_total * taux_service / 100
total_final = sous_total + service

print(f"Total plats : {total_plats} FCFA")
print(f"Couverts : {total_couverts} FCFA")
print(f"Sous-total : {sous_total} FCFA")
print(f"Service ({taux_service}%) : {service:.0f} FCFA")
print(f"TOTAL À PAYER : {total_final:.0f} FCFA")
```
</details>

### Exercice 2 : Système de recommandation film
```python
# Profil utilisateur
age = 25
genre_prefere = "action"
note_minimum = 7.5
duree_maximum = 120  # minutes

# Caractéristiques du film
film_age_minimum = 16
film_genre = "action"
film_note = 8.2
film_duree = 105

# Votre code ici :
# Déterminez si le film correspond aux critères

<details>
<summary> Solution </summary>
```python
# Solution :
age_ok = age >= film_age_minimum
genre_ok = genre_prefere == film_genre
note_ok = film_note >= note_minimum
duree_ok = film_duree <= duree_maximum

film_recommande = age_ok and genre_ok and note_ok and duree_ok

print("Critères d'âge :", age_ok)
print("Genre correspondant :", genre_ok)
print("Note suffisante :", note_ok)
print("Durée acceptable :", duree_ok)
print("FILM RECOMMANDÉ :", film_recommande)
```
</details>
```

### Exercice 3 : Gestionnaire de budget mensuel
```python
# Budget initial
budget_mensuel = 2000.0

# Dépenses du mois
budget_mensuel -= 23000   # Loyer
budget_mensuel -= 30000   # Courses
budget_mensuel -= 15000   # Transports
budget_mensuel *= 0.95  # Réduction 5% (économie)
budget_mensuel += 20000   # Prime exceptionnelle

# Analyses
print(f"Budget restant : {budget_mensuel}FCFA")
print("Budget positif :", budget_mensuel > 0)
print("Peut épargner (>50000 FCFA) :", budget_mensuel >= 50000)
print("Situation critique (<10000 FCFA) :", budget_mensuel < 10000)
```

---

## 🏆 Récapitulatif et Points Clés

### ✅ Ce que vous maîtrisez maintenant :

1. **Expressions arithmétiques** :
   - Opérations de base : `+`, `-`, `*`, `/`
   - Opérations avancées : `//`, `%`, `**`
   - Ordre des opérations et parenthèses

2. **Opérateurs composés** :
   - Raccourcis élégants : `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`
   - Modification directe de variables

3. **Comparaisons** :
   - Égalité et différence : `==`, `!=`
   - Comparaisons numériques : `<`, `>`, `<=`, `>=`
   - Résultat toujours `True` ou `False`

4. **Logique booléenne** :
   - Combinaison avec `and`, `or`, `not`
   - Tables de vérité et priorités
   - Conditions complexes

### Applications pratiques maîtrisées :
- Calculs financiers (factures, budgets, intérêts)
- Systèmes de contrôle (âge, stock, performance)
- Logic métier (recommandations, admissions)
- Gestion de données quantitatives

### Prochaines étapes suggérées :
Vous êtes maintenant prêts pour apprendre :
- Les structures conditionnelles (`if`, `elif`, `else`)
- Les boucles (`for`, `while`)
- Les fonctions personnalisées

### Conseil pour la suite :
Pratiquez ces concepts en résolvant des problèmes concrets de votre quotidien. Plus vous utilisez ces outils, plus ils deviennent naturels !

---

*Ce cours fait partie de la formation C2P (https://chat.whatsapp.com/GNtDfxG6SzEHmDXRpovN3m). Pour plus de ressources et d'exercices, consultez notre groupe watsapp 👆*

---

**🔄 N'hésitez pas à :**
- Tester tous les exemples dans votre environnement Python
- Modifier les valeurs pour voir les différents résultats
- Créer vos propres exemples basés sur vos centres d'intérêt
- Poser des questions si quelque chose n'est pas clair
