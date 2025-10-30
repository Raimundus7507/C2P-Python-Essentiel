# Projet Python : Menu Modules & Packages – Mini‑outils utiles

## Cahier des charges

### Objectif
Créer un programme avec un menu simple qui regroupe plusieurs mini‑outils basés sur des modules/packages. Chaque outil utilise des fonctions et des notions déjà vues. Le code reste lisible et basique.

### Compétences visées
- Importer et utiliser des modules (standards et tiers)
- Organiser le code avec des fonctions
- Valider des entrées utilisateur
- Afficher des résultats clairs
- Gérer des erreurs simples (try/except)

---

## Fonctionnalités requises

### 1) Menu principal persistant
Le programme tourne jusqu’à ce que l’utilisateur quitte.

Exemple d’affichage (texte) :

```
MENU – Modules & Packages
=========================
1. Scanner WiFi (Windows)
2. OCR (image -> texte)
3. Générateur de QR Code
4. Raccourcisseur de lien
5. Compresseur d’image
0. Quitter

Votre choix : _
```

Règles :
- Saisie d’un choix 0–5
- Redemander en cas d’entrée invalide
- Retour au menu après chaque outil

---

### 2) Outil A – Scanner WiFi (Windows)
But : lister les noms (SSID) des réseaux disponibles.

Modules : subprocess (commande système Windows)

Entrées :
- Aucune obligatoire (option : confirmation y/n)

Sorties :
- Liste numérotée des SSID
- Total de réseaux trouvés
- Message si aucun réseau

Validations :
- try/except si la commande échoue
- Afficher « Erreur de scan » si returncode ≠ 0

Exemple d’exécution :
```
=== Scanner WiFi ===
Scan en cours...
1. ALHN-0BC7
2. DEMONIO-BOX-5G
3. ETS LA GLOIRE WIFI 1
Total : 3 réseaux
```

---

### 3) Outil B – OCR (image -> texte)
But : extraire le texte d’une image locale.

Modules : Pillow (PIL), pytesseract (Tesseract installé)

Entrées :
- Chemin du fichier image (ex : texte.png)
- Langue OCR optionnelle (ex : fra)

Sorties :
- Texte détecté affiché en clair
- « Aucun texte détecté » si résultat vide

Validations :
- Fichier introuvable → message explicite
- try/except si ouverture/OCR échoue

Exemple d’exécution :
```
=== OCR (image -> texte) ===
Fichier : texte.png
Texte détecté :
Bonjour C2P
Apprendre Python simplement
```

---

### 4) Outil C – Générateur de QR Code
But : créer un QR code à partir d’un texte/lien.

Module : qrcode

Entrées :
- Texte ou URL
- Nom du fichier image de sortie (par défaut : qr.png)

Sorties :
- Fichier image généré (ex : qr.png)
- Message de succès

Validations :
- Entrée non vide
- try/except si sauvegarde échoue

Exemple d’exécution :
```
=== Générateur de QR ===
Texte ou lien : https://c2p.community
QR créé : qr.png
```

---

### 5) Outil D – Raccourcisseur de lien
But : transformer un lien long en lien court.

Module : requests (API is.gd)

Entrées :
- URL longue commençant par http:// ou https://

Sorties :
- Lien court retourné par is.gd
- Message d’erreur si API indisponible

Validations :
- Vérifier le préfixe http(s)
- try/except sur erreurs réseau et timeout

Exemple d’exécution :
```
=== Raccourcisseur de lien ===
Lien à raccourcir : https://exemple.com/long
Lien court : https://is.gd/AbCd12
```

---

### 6) Outil E – Compresseur d’image
But : réduire la taille d’une image (qualité plus basse).

Module : Pillow (PIL)

Entrées :
- Chemin fichier d’entrée (ex : photo.jpg)
- Nom de sortie (ex : out.jpg) – défaut : out.jpg
- Qualité (1–95) – défaut : 60

Sorties :
- Fichier compressé créé
- Message de succès

Validations :
- Fichier d’entrée existant
- Qualité dans [1, 95] (sinon valeur par défaut)
- try/except sur erreurs d’ouverture/sauvegarde

Exemple d’exécution :
```
=== Compresseur d’image ===
Entrée : photo.jpg
Sortie : out.jpg
Qualité : 60
Image compressée : out.jpg
```

---

## Spécifications techniques

Notions autorisées :
- Variables, print, input, f‑strings
- Opérateurs (arithmétiques, comparaisons, logiques)
- Conditions if/elif/else
- Fonctions (avec/sans paramètres, avec/sans retour)
- try/except (simples)
- Modules / packages, import, __init__.py si vous structurez en package

Interdit :
- Listes, dictionnaires
- POO
- Manipulation de fichiers complexes (hors images simples)
- Logique inutilement avancée

Organisation recommandée :
- Un fichier principal (ex : main.py) avec le menu propre
- Une fonction par outil (ex : run_wifi(), run_ocr(), …)
- Imports au début du fichier
- Messages clairs au terminal

Validation des entrées :
- Choix du menu : vérifier 0–5
- Chemins : non vides
- URL : commence par http:// ou https://
- Valeurs numériques (qualité) : vérifier entier valide

Gestion d’erreurs :
- Encadrer les zones à risque (I/O, réseau, OCR) avec try/except
- Messages explicites (pas d’erreur brute)

---

## Exemple d’exécution (complet)

```
MENU – Modules & Packages
=========================
1. Scanner WiFi (Windows)
2. OCR (image -> texte)
3. Générateur de QR Code
4. Raccourcisseur de lien
5. Compresseur d’image
0. Quitter

Votre choix : 1

=== Scanner WiFi ===
Scan en cours...
1. ALHN-0BC7
2. DEMONIO-BOX-5G
Total : 2 réseaux

Revenir au menu (Entrée) …

Votre choix : 4

=== Raccourcisseur de lien ===
Lien à raccourcir : https://exemple.com/abc
Lien court : https://is.gd/QxY7ZK

Revenir au menu (Entrée) …

Votre choix : 0
Au revoir.
```

---

## Contraintes et attendus

Obligatoires :
- Menu persistant (boucle) avec sortie propre
- Au moins 1 fonction par outil
- Imports corrects des modules
- Validation des entrées et try/except
- Messages clairs et résultats visibles

Interdit :
- Listes et dictionnaires
- Concepts non vus

Livrables d’équipe :
- Dossier d’équipe avec un fichier principal (ex : main.py)
- README d’équipe (but en 2 lignes, comment lancer, extrait d’exécution)

---

## Évaluation (100 points)

| Critère                 | Points | Description                                  |
|-------------------------|--------|----------------------------------------------|
| Menu persistant         | 20     | Boucle correcte, sortie propre               |
| Modules/packages        | 20     | Imports corrects, usage pertinent            |
| Fonctions               | 15     | 1+ fonction par outil, appels propres        |
| Validation/erreurs      | 15     | Entrées vérifiées, try/except efficaces      |
| Clarté de l’affichage   | 10     | Messages lisibles, résultats compréhensibles |
| Présentation (Meet)     | 20     | Objectif clair, démo courte, Q/R             |

Total : 100 points

Présentation (Google Meet) – 20 points :
- Objectif et démo du menu + 1 outil : 6 pts
- Explication simple des modules utilisés : 6 pts
- Respect du temps (≤ 5 min) et fluidité : 4 pts
- Réponses à 2 questions (entrées, erreurs) : 4 pts

---

## Aide rapide (mémo)

- Imports : `import subprocess`, `from PIL import Image`, `import pytesseract`, `import qrcode`, `import requests`
- Lancement : `python main.py`
- Tesseract pour OCR : installer Tesseract sur votre OS, puis utiliser pytesseract

Durée estimée : 3–5 heures
Niveau : Débutant