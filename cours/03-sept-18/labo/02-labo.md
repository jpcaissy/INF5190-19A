# Laboratoire 2

## Sérialisation

Voici un tableau avec 3 livres. 

Numéro | Titre | Auteur | Editeur | Nombre de pages | Année de parution
--- | --- | --- | --- | --- | ---
1 | Compilers: Principles, Techniques, and Tool | Alfred V. Aho, Ravi Sethi & Jeffrey D. Ullman | Addison Wesley | 500 | 1986
2 | Computer Organization and Design: The Hardware/Software Interface | David A. Patterson , John L. Hennessy |  Morgan Kaufmann | 914 | 2011
3 | C Programming Language |  Brian W. Kernighan, Dennis M. Ritchie | Prentice Hall | 274 | 1988

Modéliser un fichier JSON valide représentant ces 3 livres. Les auteurs peuvent être représentés par une liste.

Ce site est très utile pour formater et valider JSON : https://jsonformatter.org/

## Flask

Le fichier [flask/address_book.py](./flask/address_book.py) contient un début d'application Web non complété.

L'application lit le contenu d'un fichier JSON. Le fichier JSON est un carnet d'adresse.

* `/` -> Liste le nom des personnes du carnet d'adresse
* `/<id>` -> Affiche les informations de la personne représenté par son identifiant (`id`).

Pour rouler l'application, vous devez avoir `flask` et `pytest` d'installé dans votre environnement virtuel :

```
$ pip install flask pytest
```

Ensuite à partir du répertoire qui contient `address_book.py`, vous pouvez lancer l'application Web avec la commande
`FLASK_DEBUG=1 FLASK_APP=address_book flask run` :

```
$ cd cours/03-sept-18/labo/flask
$ FLASK_DEBUG=1 FLASK_APP=address_book flask run
 * Serving Flask app "address_book" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 137-450-813
```

L'application Web sera disponible à l'adresse suivante : [http://127.0.0.1:5000](http://127.0.0.1:5000)

À faire :

1. Compléter la méthode `address`

La méthode `address` doit retourner une page HTML qui contient les informations de la personne du carnet d'adresse.

Si l'objet n'existe pas, la page doit retourner un 404.

2. Compléter les tests dans le fichier [test.py](./flask/test_app.py)

Pour rouler les tests, il suffit de rouler la commande `pytest` :

```
$ pytest
================================================================================================================================================================================= test session starts ==================================================================================================================================================================================
platform linux -- Python 3.6.8, pytest-5.1.2, py-1.8.0, pluggy-0.13.0
sensitiveurl: .*
rootdir: /home/jpcaissy/src/INF5190/cours/03-sept-18/labo/flask
plugins: flask-0.15.0, metadata-1.8.0, selenium-1.17.0, variables-1.8.0, base-url-1.4.1, html-2.0.0
collected 5 items                  
[...]
```
