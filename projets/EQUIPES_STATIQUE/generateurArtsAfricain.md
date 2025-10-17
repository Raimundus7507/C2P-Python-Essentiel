# AfrikArt Generator 🌍

> **Quiz culturel africain + Générateur de motifs ASCII**  
> Projet pédagogique Python pour débutants - Spécial Afrique

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![Niveau](https://img.shields.io/badge/Niveau-D%C3%A9butant-brightgreen.svg)]()
[![Afrique](https://img.shields.io/badge/Th%C3%A8me-Afrique-orange.svg)]()
[![Éducatif](https://img.shields.io/badge/Type-%C3%89ducatif-purple.svg)]()

---

## Cahier des Charges

### **Objectif du Projet**

Créer un programme interactif en deux parties :
1. **Quiz culturel** qui identifie le pays de l'utilisateur et affiche son drapeau
2. **Générateur de motifs** ASCII personnalisables

Le programme doit être **engageant**, **éducatif** et **culturellement pertinent** pour les apprenants africains.

---

## 📝 Description Générale

**AfrikArt Generator** est un programme qui combine découverte culturelle et création artistique. L'utilisateur répond à des questions personnelles, découvre le drapeau de son pays dessiné en ASCII, puis peut créer des motifs géométriques personnalisés.

### **Vision du Projet**
- Valoriser la **culture africaine** dans l'apprentissage
- Rendre la programmation **concrète et motivante**
- Créer un lien entre **technologie et identité culturelle**

---

## Fonctionnalités Attendues

### **Phase 1 : Quiz Culturel et Identification**

#### Collecte d'Informations
Le programme doit demander à l'utilisateur :
- **Nom complet**
- **Pays de résidence**
- **Ville de résidence** 
- **Âge**
- **Langue principale parlée**
- **Plat africain préféré**

#### 🏳️ Identification et Affichage du Drapeau
Le programme doit :
- **Analyser** la réponse du pays (gestion casse, espaces, variantes)
- **Identifier** automatiquement le pays parmi 4 options
- **Afficher** le drapeau correspondant en ASCII art
- **Gérer** les pays non reconnus avec un message approprié

#### 🌍 Pays Supportés (drapeaux simples)
1. **🇹🇬 Togo** - Bandes horizontales avec carré rouge et étoile
2. **🇳🇬 Nigeria** - 3 bandes verticales (vert-blanc-vert)
3. **🇧🇫 Burkina Faso** - 2 bandes horizontales avec étoile centrale
4. **🇲🇱 Mali** - 3 bandes verticales (vert-jaune-rouge)

### **Phase 2 : Générateur de Motifs Artistiques**

#### Menu Interactif
Le programme doit proposer :
1. **Triangle** (forme pointue vers le haut)
2. **Rectangle** (forme rectangulaire pleine ou avec bordures)
3. **Pyramide** (triangle avec base large)
4. **Pyramide inversée** (triangle pointu vers le bas)

#### ⚙️ Paramètres Personnalisables
Pour chaque forme, l'utilisateur peut choisir :
- **Taille/Hauteur** (avec limites min/max)
- **Caractère de dessin** (*, #, @, +, etc.)
- **Style** (plein ou bordures uniquement - bonus)

#### 🔄 Fonctionnalités Additionnelles
- **Validation** des entrées utilisateur
- **Valeurs par défaut** si entrée invalide
- **Possibilité** de créer plusieurs motifs successifs
- **Messages encourageants** personnalisés

---

## Prérequis Techniques

### **Concepts Python Requis**
- **Variables** : string, int, stockage des réponses
- **Entrées utilisateur** : fonction `input()`
- **Sorties formatées** : fonction `print()` avec mise en forme
- **Structures conditionnelles** : `if`, `elif`, `else`
- **Conditions imbriquées** : `if` dans `if` pour analyses fines
- **Opérateurs de comparaison** : `==`, `!=`, `>`, `<`, etc.
- **Opérateurs logiques** : `and`, `or`, `not`
- **Boucles `for`** : avec `range()` pour répétitions
- **Manipulation de chaînes** : `.lower()`, `.strip()`, `len()`

### 🚫 **Concepts NON Autorisés**
- Fonctions personnalisées (`def`)
- Listes et dictionnaires
- Boucles `while`
- Instructions `break` ou `continue`
- Gestion d'exceptions (`try/except`)
- Modules externes

---

## 💻 Interface Utilisateur

### **Exigences d'Affichage**
- **Messages de bienvenue** clairs et chaleureux
- **Questions** numérotées et bien formatées
- **Emojis** pour rendre l'interface attrayante
- **Séparateurs visuels** entre les sections
- **Récapitulatif** des informations saisies
- **Messages de félicitations** personnalisés

### 📱 **Expérience Utilisateur**
- **Navigation intuitive** entre les phases
- **Instructions claires** pour chaque étape
- **Feedback immédiat** sur les choix utilisateur
- **Gestion des erreurs** avec messages explicites
- **Possibilité de quitter** à tout moment

---

## 🎮 Exemple d'Utilisation

### **Scénario Complet**

```
🌍 === AFRIKART GENERATOR ===
Bienvenue dans votre générateur d'art africain !

=== QUIZ CULTUREL ===
Quel est votre nom ? Kossi Kossivi
Dans quel pays vivez-vous ? Togo
Dans quelle ville ? Lomé  
Quel est votre âge ? 22
Quelle langue parlez-vous le mieux ? Français
Quel est votre plat africain préféré ? Garri + Kolikoo #🤣🚶‍♀️

=== RÉCAPITULATIF ===
👤 Nom : Kossi Kossivi
🌍 Pays : Togo
🏙️ Ville : Lomé
🎂 Âge : 22 ans
🗣️ Langue : Français
🍽️ Plat préféré : Garri + Kolikoo

🇹🇬 Magnifique ! Voici le drapeau du Togo ! 🇹🇬

[Affichage du drapeau en ASCII avec emojis colorés]

=== GÉNÉRATEUR DE MOTIFS ===
Kossi, voulez-vous créer des motifs artistiques ? (oui/non) : oui

Choisissez votre forme :
1. 🔺 Triangle
2. ⬜ Rectangle  
3. 🔺 Pyramide
4. 🔻 Pyramide inversée

Votre choix (1-4) : 1
Hauteur du triangle (3-10) : 5
Caractère de dessin : *

[Affichage du triangle généré]

🎉 Magnifique création !
Voulez-vous créer un autre motif ? (oui/non) : non

Merci Kossi ! 🌍 Vive l'Afrique et sa créativité ! 🎨
```

---

## ✅ Critères de Validation

### **Phase 1 : Quiz (40 points)**
- [ ] Collecte des 6 informations requises **(10 pts)**
- [ ] Identification correcte des 4 pays **(10 pts)**
- [ ] Affichage des 4 drapeaux en ASCII **(15 pts)**
- [ ] Gestion des pays non reconnus **(5 pts)**

### **Phase 2 : Générateur (40 points)**
- [ ] Menu avec 4 formes géométriques **(10 pts)**
- [ ] Paramètres personnalisables (taille, caractère) **(10 pts)**
- [ ] Génération correcte des 4 formes **(15 pts)**
- [ ] Validation des entrées utilisateur **(5 pts)**

### **Interface et Code (20 points)**
- [ ] Interface claire et attrayante **(5 pts)**
- [ ] Messages personnalisés avec le nom **(5 pts)**
- [ ] Code bien structuré et lisible **(5 pts)**
- [ ] Conditions imbriquées utilisées **(5 pts)**

---

## Objectifs Pédagogiques

### **Compétences Techniques**
- Maîtriser les **structures conditionnelles complexes**
- Utiliser les **boucles for** de manière créative
- Gérer les **entrées utilisateur** avec validation
- Combiner **logique** et **créativité** dans le code

### **Compétences Transversales**
- **Pensée algorithmique** : décomposer un problème complexe
- **Attention aux détails** : gestion des cas particuliers
- **Créativité** : design des motifs et de l'interface
- **Culture générale** : découverte des drapeaux africains

### **Valeurs Ajoutées**
- **Fierté culturelle** : valorisation de l'identité africaine
- **Engagement** : projet concret et motivant
- **Autonomie** : capacité à étendre le projet
- **Confiance** : réussite d'un projet complet

---

## Extensions Possibles

### **Niveau Intermédiaire**
- Ajouter plus de drapeaux africains
- Créer des motifs plus complexes (losanges, hexagones)
- Intégrer des informations culturelles (langues, monnaies)
- Proposer des quiz sur les capitales africaines

### **Niveau Avancé**
- Sauvegarder les créations dans des fichiers
- Créer une galerie de motifs
- Ajouter des couleurs réelles aux drapeaux
- Interface graphique simple

---

## 📊 Planning de Développement

### **(2h) : Structure de Base**
- Messages d'accueil et collecte d'informations
- Logique d'identification des pays
- Premier drapeau (Togo)

### **(2h) : Drapeaux et Validation**
- Compléter les 3 autres drapeaux
- Gestion des cas d'erreur
- Récapitulatif personnalisé

### **(2h) : Générateur de Motifs**
- Menu et saisie des paramètres
- Génération des 4 formes géométriques
- Validation et messages de fin

### **(1h) : Finitions**
- Tests et corrections
- Amélioration de l'interface
- Documentation du code

---

## 🏆 Conseils de Réussite

### **Pour les Étudiants**
- **Testez** votre programme après chaque étape
- **Commencez simple** puis ajoutez les détails
- **Utilisez des variables** avec des noms clairs
- **Commentez** votre code pour vous souvenir
- **Amusez-vous** avec les emojis et les messages !

### **Pour les Formateurs**
- **Encouragez** la créativité dans les messages
- **Valorisez** les références culturelles locales
- **Aidez** sur la logique des boucles pour les motifs
- **Partagez** les créations réussies avec la classe
- **Célébrez** les projets terminés !

---

## 📞 Support et Ressources

### **Ressources Utiles**
- [Emojis drapeaux](https://emojipedia.org/flags/) pour l'inspiration
- [ASCII Art Generator](https://www.asciiart.eu/) pour les idées
- [Python.org](https://python.org) pour la documentation

### **Communauté**
- **Discord** : https://discord.gg/JuEbGcFC
- **GitHub** : partage des créations
- **WatsApp** : https://chat.whatsapp.com/GNtDfxG6SzEHmDXRpovN3m

---

**Objectif Final :** Chaque étudiant repart avec un programme complet, fonctionnel, et dont il peut être fier ! Un projet qui célèbre à la fois ses compétences en programmation et son identité africaine.

**🌍 Slogan du projet :** *"Programmer avec fierté, créer avec identité !"*

---

 **Ce projet transforme l'apprentissage en aventure culturelle !**