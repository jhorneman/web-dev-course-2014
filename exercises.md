---
title: Exercises
layout: default
---
# Exercises

## Option 1: "Livre dont vous etes êtes le héros", en ligne

Comme dans les annees 80, un "livre" virtuel avec des paragraphes et des choix qui menent vers des autres paragraphes. L'histoire commence avec le paragraphe de debut et se finit par un paragraphe d'échec ou de victoire.

### Client (dans le browser)

Le joueur peut jouer le jeu dans le browser. Elle voit le paragraphe et les choix actuels. Quand il click sur un choix, il avance vers le paragraphe qui correspond a ce choix.

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

### Liens

Ce genre de jeu, ca se joue encore? Oui! Voici quelques examples:

- Les [jeux](http://twinehub.weebly.com/) fait avec [Twine](http://twinery.org/).
- [howling dogs](http://aliendovecote.com/uploads/twine/howlingdogs/howlingdogs.html), un jeu indie qui a gagné des prix.
- Les jeux de [Inkle Studios](http://www.inklestudios.com/).
- Les jeux de [Choice of Games](https://www.choiceofgames.com/).
- [Coin of Destiny](http://molyjam12.herokuapp.com), le jeu que j'avais programmé avec Python et Flask en 48 heures pour un game jam.

Bien sur, ces sont en partie des jeux commerciaux developpés avec plus de moyens que vous, mais c'est juste pour montrer que c'est un type de jeu qui reste populaire aujourd'hui.

## Option 2: Jeu d'arcade simple dans le browser avec high scores

Un jeu d'arcade simple, genre Breakout, qu'on peut jouer dans le browser, avec une liste de high scores persistante.

### Client (dans le browser)

Le joueur peut jouer un jeu d'arcade simple dans le browser. Quand le jeu est terminé il peut entrer son nom pour ajouter son score dans la liste des high scores, qui est affiché.

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
