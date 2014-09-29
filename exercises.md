---
title: Exercises
layout: default
---
# Les Exercices

<p style="font-size:larger; color:red">ENVOYEZ VOS FICHIERS ZIP A JURIE@JURIE.ORG LE MATIN DU LUNDI LE 28 SEPTEMBRE</p>

## Exercice 1: "Livre dont vous etes êtes le héros", en ligne

Comme dans les annees 80, un "livre" virtuel avec des paragraphes et des choix qui menent vers des autres paragraphes. L'histoire commence avec le paragraphe de debut et se finit par un paragraphe d'échec ou de victoire.

### Client (dans le browser)

Le joueur peut jouer le jeu dans le browser. Elle voit le paragraphe et les choix actuels. Quand il click sur un choix, il avance vers le paragraphe qui correspond a ce choix.

### Serveur (en Python)

Le serveur lit la definition du livre (cf. Outil plus bas), et generent les pages HTML que le joueur voit dans le browser.

### Outils

L'utilisateur peut definir le livre, par exemple en changeant les fichiers qui sont lu par le serveur au lancement.

### A livrer

- Le code complet et toutes les donnees (dans un fichier ZIP, envoyé a jurie@jurie.org).
- Je peux executer le code moi-meme.
- Je n'arrive pas a faire planter le code facilement.
- Je peux modifier les donnees et faire mon propre livre.

(Si vous installez des packages en plus avec pip, dites-moi lesquels.)

### Ce que je regarderai

- Est-ce que ca marche (dans Firefox et Chrome).
- Est-ce que vous faites ce que j'ai dit :)
- Architecture et qualité du code.
- Qualité > Quantité.

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

## Exercice 2: Temps actuel a Lyon, en JavaScript

Un page HTML avec du JavaScript (et du CSS si vous voulez) qui montre la temperature actuelle a Lyon, en utilisant l'API de openweathermap.org.

L'utilisateur voit la temperature (en Celsius) et les autres elements du meteo actuel de Lyon dans une page web.

Vous pouvez utiliser [ce lien](http://api.openweathermap.org/data/2.5/find?q=Lyon,fr&units=metric) pour recuperer les données météo.

### A livrer

- Le code complet (dans un fichier ZIP, envoyé a jurie@jurie.org).
- Je peux lancer et regarder la page web moi-meme.

### Ce que je regarderai

- Est-ce que ca marche (dans Firefox et Chrome).
- Est-ce que vous faites ce que j'ai dit :)
- Architecture et qualité du code.
- Qualité > Quantité.

### Points bonus

- Reactions correctes sur des problemes avec l'API.
- Une page jolie.
- La page montre plus de données que juste la temperature.
- Des moyens qui permettent l'utilisateur de parametriser les données affichées (metrique/imperial, lieux différents, etc.)
- Une solution sans jQuery (mais avec une autre librairie ou completement sans).
- Un ou des APIs différents pour recuperer les données météo.

### Astuces

- Cette approche pour charger du code Javascript ne marche plus pour une page sans serveur:
```<script src="//code.jquery.com/jquery-1.11.0.min.js"></script>```
- Nous avons déja fait des choses tres similaires dans le projet blog_sqla et tweaker.
- Utilisez [JSONPrettyPrint](http://jsonprettyprint.com/) pour visualiser la structure du JSON.
