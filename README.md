# Jeu MasterMind avec CustomTkinter

Ce projet est un jeu MasterMind développé avec Python et la bibliothèque `customtkinter`, qui permet de créer des interfaces graphiques modernes et personnalisées.

## Objectif du projet

L'objectif de ce projet est de créer une application interactive pour jouer au jeu MasterMind, où le joueur doit deviner une combinaison de chiffres générée par l'ordinateur en un nombre limité de tentatives. Le jeu propose deux niveaux de difficulté : **Facile** et **Normal**. Actuellement, seule la version facile du jeu est implémentée.

## Fonctionnalités

### 1. **Niveau Facile :**
   - Le joueur doit deviner une combinaison de 4 chiffres générés aléatoirement.
   - Un message de résultat indique si les chiffres sont bien placés ou mal placés.
   - Le joueur peut entrer sa réponse via une zone de texte, et le jeu valide la réponse au fur et à mesure.
   - Si le joueur devine correctement la combinaison, un message de félicitations apparaît.
   
### 2. **Interface Utilisateur :**
   - L'interface graphique est réalisée avec `customtkinter`, une bibliothèque Python permettant de créer des interfaces modernes et personnalisables.
   - Des boutons et des champs de texte permettent de jouer et de fournir des informations sur le résultat de chaque tentative.

### 3. **Retour au Menu :**
   - Le jeu propose un bouton pour revenir au menu principal après avoir terminé une partie, que ce soit en gagnant ou en voulant redémarrer une nouvelle partie.

## Installation

### Prérequis
- Python 3.x
- `customtkinter`
- `random` (inclus dans Python)

### Installation des dépendances
Clonez le dépôt ou téléchargez les fichiers du projet, puis installez la bibliothèque nécessaire avec `pip` :

```bash
pip install customtkinter
````

## Utilisation

1. Lancez le fichier Python principal du projet. L'application s'ouvrira avec un menu principal où vous pourrez choisir la difficulté du jeu.
2. Une fois la difficulté choisie, le jeu démarre, et vous devez entrer une combinaison de chiffres dans la zone de texte.
3. Cliquez sur "Récupérer les chiffres" pour vérifier si la combinaison saisie est correcte.
4. Si vous devinez la bonne combinaison, un message de félicitations s'affichera. Vous pourrez alors revenir au menu principal.

### Commandes

* **Récupérer les chiffres :** Permet de vérifier la réponse donnée par l'utilisateur par rapport à la combinaison générée.
* **Retour au menu :** Permet de revenir à l'écran principal après une partie.

## Structure du code

Le projet est organisé en plusieurs classes :

* **Jeu :** Gère la logique du jeu (génération des chiffres à deviner, validation des réponses, affichage des résultats).
* **NiveauDifficulte :** Permet de choisir le niveau de difficulté (Facile ou Normal).
* **Menu :** Interface du menu principal pour démarrer une partie.
* **App :** Classe principale qui gère l'application et l'interface graphique.

## Exemple d'exécution

Après avoir lancé le fichier Python, l'interface s'affiche et vous permet de jouer :

```bash
python jeu_mastermind.py
```

## Contributions

Les contributions sont les bienvenues ! Si vous avez des idées pour améliorer ce projet, n'hésitez pas à proposer des améliorations en créant une **pull request**.

## Auteurs

* Clément Bernard (Développeur principal)
