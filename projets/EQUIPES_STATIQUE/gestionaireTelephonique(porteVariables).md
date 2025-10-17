# Mini Gestionnaire de Crédits Téléphoniques

## Projet d'une journée pour débutants Python C2P

**Objectif :** Créer un programme simple qui simule la gestion de crédit téléphonique, en utilisant les fonctions et les variables globales/locales.

---

## Ce que votre programme doit faire

Votre programme doit permettre à l'utilisateur de :
1. **Voir son solde** actuel
2. **Acheter du crédit** (recharger)
3. **Passer des appels** (consommer du crédit)
4. **Envoyer des SMS** (consommer du crédit)
5. **Quitter** le programme

---

## 🔧 Variables globales à utiliser

Créez ces variables globales au début de votre programme :

```python
# À créer au début du fichier
solde = 0.0                    # Le crédit actuel de l'utilisateur
tarif_appel_minute = 25.0      # Prix d'une minute d'appel (FCFA)
tarif_sms = 25.0              # Prix d'un SMS (FCFA)
nom_utilisateur = ""          # Nom de l'utilisateur
```

---

## Fonctions à créer

### 1. **`demander_nom()`**
- Demande le nom à l'utilisateur
- Met à jour la variable globale `nom_utilisateur`
- Affiche un message de bienvenue

### 2. **`afficher_solde()`**
- Affiche le solde actuel de l'utilisateur
- Format : "Bonjour [nom], votre solde est de [montant] FCFA"

### 3. **`acheter_credit()`**
- Demande à l'utilisateur le montant à recharger
- Vérifie que le montant est positif
- Ajoute le montant au solde global
- Affiche le nouveau solde

### 4. **`passer_appel()`**
- Demande la durée de l'appel en minutes
- Calcule le coût (durée × tarif par minute)
- Vérifie si l'utilisateur a assez de crédit
- Si oui : déduit le montant et affiche le nouveau solde
- Si non : affiche un message d'erreur

### 5. **`envoyer_sms()`**
- Demande le nombre de SMS à envoyer
- Calcule le coût (nombre × tarif SMS)
- Vérifie si l'utilisateur a assez de crédit
- Si oui : déduit le montant et affiche le nouveau solde
- Si non : affiche un message d'erreur

### 6. **`afficher_menu()`**
- Affiche les options disponibles
- Retourne le choix de l'utilisateur

---

## 💬 Ce qu'il faut demander à l'utilisateur

### Au démarrage :
- Son **nom** (une seule fois)

### Dans le menu principal :
- **Choix de l'action** (nombre de 1 à 5)

### Selon l'action choisie :
- **Montant à recharger** (pour achat de crédit)
- **Durée d'appel en minutes** (pour les appels)
- **Nombre de SMS** (pour les messages)

---

## Exemple complet d'exécution

```
=== GESTIONNAIRE DE CRÉDIT TÉLÉPHONIQUE ===

Comment vous appelez-vous ? Pascal PASKOD

Bienvenue Pascal PASKOD dans votre gestionnaire de crédit Moov !

=== MENU PRINCIPAL ===
Bonjour Pascal PASKOD, votre solde est de 0.0 FCFA

1. Acheter du crédit
2. Passer un appel
3. Envoyer des SMS
4. Voir mon solde
5. Quitter

Votre choix : 1

=== ACHAT DE CRÉDIT ===
Combien voulez-vous recharger (FCFA) ? 2000

✅ Recharge effectuée !
Votre nouveau solde est de 2000.0 FCFA

=== MENU PRINCIPAL ===
Bonjour Pascal PASKOD, votre solde est de 2000.0 FCFA

1. Acheter du crédit
2. Passer un appel
3. Envoyer des SMS
4. Voir mon solde
5. Quitter

Votre choix : 2

=== PASSER UN APPEL ===
Durée de votre appel (minutes) ? 5

Coût de l'appel : 5 minutes × 25 FCFA = 125.0 FCFA
✅ Appel effectué !
Votre nouveau solde est de 1875.0 FCFA

=== MENU PRINCIPAL ===
Bonjour Pascal PASKOD, votre solde est de 1875.0 FCFA

1. Acheter du crédit
2. Passer un appel
3. Envoyer des SMS
4. Voir mon solde
5. Quitter

Votre choix : 3

=== ENVOYER DES SMS ===
Combien de SMS voulez-vous envoyer ? 3

Coût des SMS : 3 SMS × 25 FCFA = 75.0 FCFA
✅ SMS envoyés !
Votre nouveau solde est de 1800.0 FCFA

=== MENU PRINCIPAL ===
Bonjour Pascal PASKOD, votre solde est de 1800.0 FCFA

1. Acheter du crédit
2. Passer un appel
3. Envoyer des SMS
4. Voir mon solde
5. Quitter

Votre choix : 2

=== PASSER UN APPEL ===
Durée de votre appel (minutes) ? 80

Coût de l'appel : 80 minutes × 25 FCFA = 2000.0 FCFA
❌ Crédit insuffisant ! Votre solde est de 1800.0 FCFA
Il vous manque 200.0 FCFA

=== MENU PRINCIPAL ===
Bonjour Pascal PASKOD, votre solde est de 1800.0 FCFA

1. Acheter du crédit
2. Passer un appel
3. Envoyer des SMS
4. Voir mon solde
5. Quitter

Votre choix : 4

Bonjour Pascal PASKOD, votre solde est de 1800.0 FCFA

=== MENU PRINCIPAL ===
Bonjour Pascal PASKOD, votre solde est de 1800.0 FCFA

1. Acheter du crédit
2. Passer un appel
3. Envoyer des SMS
4. Voir mon solde
5. Quitter

Votre choix : 5

Merci d'avoir utilisé votre gestionnaire de crédit !
À bientôt PASKOD ! 👋
```

---

## ✅ Points importants à respecter

### Variables globales vs locales :
- **Globales :** `solde`, `nom_utilisateur`, `tarif_appel_minute`, `tarif_sms`
- **Locales :** `montant_recharge`, `duree_appel`, `nombre_sms`, `cout`, `choix`

### Validations nécessaires :
- Vérifier que les montants/durées sont positifs
- Vérifier que le solde est suffisant avant de déduire
- Gérer le cas où l'utilisateur entre des lettres au lieu de nombres

### Structure du programme :
1. Définir les variables globales
2. Créer toutes les fonctions
3. Programme principal avec boucle pour le menu
4. Appeler `demander_nom()` une seule fois au début

---

## Critères de réussite

Votre programme fonctionne correctement si :
- 🟢 Il demande le nom une seule fois au démarrage
- 🟢 Le menu s'affiche en boucle jusqu'à ce que l'utilisateur quitte
- 🟢 Le solde se met à jour correctement après chaque opération  
- 🟢 Il refuse les opérations quand le crédit est insuffisant
- 🟢 Les messages sont clairs et en français
- 🟢 Le programme utilise des variables globales et locales
- 🟢 Chaque fonctionnalité est dans sa propre fonction

**Temps estimé :** 3-4 heures pour débutants

---

## Conseils pour débuter

1. **Commencez simple :** Créez d'abord juste le menu et l'affichage du solde
2. **Une fonction à la fois :** Implémentez et testez chaque fonction séparément  
3. **Testez souvent :** Après chaque fonction, lancez le programme pour vérifier
4. **Gérez les erreurs plus tard :** Focus d'abord sur le fonctionnement de base

**Bon travail à toutes les équipes !**