---
title: Exercises
layout: default
---
# Exercises

## Option 1: "Livre dont vous etes êtes le héros", en ligne

Comme dans les annees 80, un "livre" virtuel avec des paragraphes et des choix qui menent vers des autres paragraphes. L'histoire commence avec le paragraphe de debut et se finit par un paragraphe d'échec ou de victoire.

### Client (dans le browser)

Le joueur peut jouer le jeu dans le browser. Elle voit le paragraphe et les choix actuels. Quand elle click sur un choix, elle avance vers le paragraphe qui correspond a ce choix.

### Serveur (en Python)

Le serveur lit la definition du livre (cf. Outil plus bas), et generent les pages HTML que le joueur voit dans le browser.

### Outils

L'utilisateur peut definir le livre, par exemple en changeant les fichiers qui sont lu par le serveur au lancement.

### A livrer

- Le code et toutes les donnees.
- Je peux executer le code moi-meme.
- Je n'arrive pas a faire planter le code facilement.
- Je peux modifier les donnees et faire mon propre livre.

(Si vous installez des packages en plus avec pip, dites-moi lesquels.)

### Ce que je regarderai

- Est-ce que ca marche
- Est-ce que vous faites ce que j'ai dit :)
- Architecture et qualité du code
- Qualité > Quantité

### Points bonus

- Un workflow facile, pour les non-programmeurs.
- Des paragraphes avec du texte 'riche' (pensez HTML ou Markdown).
- Des images dans les paragraphes.
- Une page plus jolie.
- Des jolis effets en JavaScript.
- Une histoire interessante.
- Les tests automatiques.
- Ca tourne sur un serveur sur l'internet (donnez-moi l'URL dans ce cas-la).
- Il y a des effets aleatoires dans l'histoire ("Tentez le coup (25% de chance de reussite)").
- Le joueur a des attributs qui peuvent changer.
- On peut editer le livre directement dans le browser.

### Astuces

- Il est facile de lire des fichiers text ligne par ligne en Python, et de mélanger des formats.
- Le format YAML est bien pour les meta-donnees, mais il y aussi XML ou JSON.
- Regardez Heroku pour mettre le serveur sur internet.


## Option 2: Jeu d'arcade simple dans le browser avec high scores

Un jeu d'arcade simple, genre Breakout, qu'on peut jouer dans le browser, avec une liste de high scores persistante.

### Client (dans le browser)

Le joueur peut jouer un jeu d'arcade simple dans le browser. Quand le jeu est terminé elle peut entrer son nom pour ajouter son score dans la liste des high scores, qui est affiché.

### Serveur (en Python)

Le serveur sert a gerer les high scores.

### A livrer

- Le code et toutes les donnees.
- Je peux executer le code moi-meme.
- Je n'arrive pas a faire planter le code facilement.

(Si vous installez des packages en plus avec pip, dites-moi lesquels.)

### Ce que je regarderai

- Est-ce que ca marche.
- Est-ce que vous faites ce que j'ai dit :)
- Architecture et qualité du code.
- Qualité > Quantité.

### Points bonus

- Complexité du jeu.
- Effets audio et graphiques en JavaScript.
- Achievements, en plus des high scores.
- Les tests automatiques.
- Ca tourne sur un serveur sur l'internet (donnez-moi l'URL dans ce cas-la).
- On peut tweaker les parametres du jeu dans le browser.
- Le jeu est multi-joueur (tour par tour est OK).

### Astuces

- Je vous conseille d'utiliser l'element HTML canvas pour faire le jeu. Vous pouvez utiliser des librairies JavaScript open source pour faire le rendu etc.
- N'utilisez pas des generateurs de jeu HTML5 ou des librairies commercielles pour le cote JavaScript.
