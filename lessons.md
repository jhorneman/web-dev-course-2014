---
title: Lessons
layout: default
---

# Ce que nous avons vu pendant les cours

Nous avons regardé et modifié le code que vous pouvez trouver [ici](https://github.com/jhorneman/web-dev-course-2014/tree/gh-pages/code).

## web_server

Nous avons discuté pas à pas les bases des serveurs web en Python avec le micro-framework Flask:

### web_server_1_1.py

Un serveur minimal. Notez le @app.route. Les fonctions avec un route comme ça s'appellent les view functions.

### web_server_1_2.py

Deux routes.

### web_server_1_3.py

Un troisième route qui montre le debugger interactif de Flask (en mode debug).

### web_server_1_4.py

Les variables dans les routes.

### web_server_1_5.py

Comment faire si on ne met pas le nom?

### web_server_1_6.py

Une solution meilleure avec un valeurs par défaut pour le paramètre.

### web_server_1_global_variables.py

Un essai raté pour demontrer que les variables ne gardent pas leur état dans un serveur web, parce que le protocol HTTP est stateless. Le code dans ce fichier ne marchera pas sur un vrai serveur web!

### web_server_2_1.py

Comment envoyer un fichier HTML en lieu des chaines simples.

### web_server_2_2.py

Comment utiliser Jinja2, le système de gabarit inclut dans Flask, pour modifier les fichiers HTML avant de les envoyer au browser.

## blog

Un petit moteur de blog qui utilise des instructions SQL brutes pour acceder à une base de données.

C'était pour montrer comment c'est ennuyant de faire ça à la main, ignorez-le.

Comme tout les autres examples nous utilisons SQLite comme moteur de base de données.

# blog_sqla

Un moteur de blog qui utilise la librairie SQLAlchemy pour faire la traducation entre la base de données SQL et les objets en Python. Ce type de librairie s'appele un ORM.

Les classes qui répresentent les tableaux dans la base de données se trouve dans models.py. Les view functions se trouvent dans views.py.

On peut faire tourner le blog en appellant blog.py. On crée la base de données avec db.py.

Nous avons vu comment faire des tests automatisés dans blog_full_tests.py.

Dans static il y a plusieurs moyens pour generer le blog en JavaScript en lieu d'utiliser Python. Une fois à la main et une fois avec une librairie de gabarit pour JavaScript qui s'appelle Handlebars.

# forms

Comment faire des formulaires en utilisant la librairie WTForms.

# tictactoe

Un petit jeu multi-joueur et tour par tour que nous avons codé live pendant le cours.

# excel_import

Comment utiliser Python pour lire et transformer des données d'un fichier Excel.

# scraper

Comment lire une page web avec Python.

# tweaker

Comment faire une petite interface dynamique en JavaScript pour régler des variables - pratique pour faire le réglage dans un jeu.

# requirements.txt

La liste avec les packages Python utilisé, que vous pouvez installer dans un seul coup avec la commande

` pip install -r requirements.txt `
