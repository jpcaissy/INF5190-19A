# Laboratoire 1

Pré-requis : [installer Python](../01-sept-04/installer-python.md)

Le laboratoire a pour objectif de vous familiariser avec Python, et de créer une appliction web simple.

## Python

```python
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

1. Récpuérer le 3e élément de la liste
2. Avec la syntaxe `for ... in` itérer sur la liste et afficher le double de l'entier
    2.1 Afficher l'entier à l'intérieur d'une string (i.e.: `La valeur est 2`, `La valeur est 4`, etc)
    2.2 Même chose que 2.1, mais utiliser la fonction de _slice_ des listes pour itérer du 4e élément de la liste à la fin
    2.3 Grace à la méthode `range`, rajouter les éléments 10 à 19 à `ma_liste`.

```python
cours = {
    "INF5190": {
        "nom": "Programmation Web avancé",
        "groupe": "030",
    },
    "INF3190": {
        "nom": "Introduction à la programmation Web",
        "groupe": "020",
    }
}
```

3. À partir du dictionnaire `cours`, afficher le nom du cours de INF5190 et INF3190
4. Modifier le groupe de INF3190 pour `030`
5. Pour chacun des cours, rajouter l'horaire à la structure de donnée (INF5190: mercredi soir, INF3190: mardi soir)
6. Rajouter le cours INF4170 - Architecture des ordinateurs pour le groupe 040 avec un horaire le jeudi soir

----

7. Créer un fichier texte et mettez y quelques lignes. Créer un script python qui va ouvrir le fichier avec la
    méthode `open` et lire puis afficher chacune des lignes du fichier.

    Indice : utilisez la méthode `readline` avec a syntaxe `with`.
8. Rajouter une gestion d'exception qui gère un fichier qui n'existe pas `try/except`

----

9. Créer un module nommé operations qui contien la méthode `lire_toutes_les_lignes`. Cette méthode prend en argument
    un nom de fichier et va retourner une liste de toutes les lignes du fichiers.

    ```python
    >>> from operations import lire_toutes_les_lignes
    >>> lire_toutes_les_lignes("un fichier existant")
    >>> ['ligne 1', 'ligne 2', 'ligne 3']
    ```

## Application web

### Environnement de développement

Avec `pip`, installez `virtualenv`

```
$ pip install virtualenv
```

Si vous rencontrez des erreurs de permissions, installez le globalement avec `sudo` :

```
$ sudo pip install virtualenv
```

Dans un nouveau dossier, initialisez l'environnement de développement pour ce laboratoire :

```
$ virtualenv -p python3 env/
```

Si vous utilisez l'exécutable `python` au lieu de `python3` changer `-p python3` pour `-p python`

Initialiser l'environnement de développement pour votre shell :

```
$ source env/bin/activate
```

`which python` devrait vous retourner l'exécutable dans votre environnement. Dans mon cas, c'est 

```
(env) $ which python
/home/jpcaissy/src/INF5190/cours/02-sept-11/labo/env/bin/python
```

Si je ne suis pas dans l'environnement virtuel, je vais avoir la valeur de mon système :

```
$ which python
/usr/bin/python
$ which python3
/usr/bin/python3
```

Pour désactiver l'environnement virtuel, tappez la commande `deactivate` :

```
$ source env/bin/activate
(env) $ which python
/home/jpcaissy/src/INF5190/cours/02-sept-11/labo/env/bin/python
(env) $ which python3
/home/jpcaissy/src/INF5190/cours/02-sept-11/labo/env/bin/python3
(env) $ which pip
/home/jpcaissy/src/INF5190/cours/02-sept-11/labo/env/bin/pip
(env) $ which pip3
/home/jpcaissy/src/INF5190/cours/02-sept-11/labo/env/bin/pip3
(env) $ deactivate
$ which python
/usr/bin/python
$ which pip
$ which pip3
/usr/bin/pip3
```

## Exercice

1. Installer le serveur WSGI `waitress`:
    ```
    (env) $ pip install waitress
    ```
    1.1 Assurez-vous que `waitress` est installé :
    ```
    (env) $ waitress-serve
    $ waitress-serve -h
    Error: option -h not recognized

    Usage:

        waitress-serve [OPTS] MODULE:OBJECT

    Standard options:

        --help
            Show this information.

    [.....]
    ```

2. **À Venir** : Compléter le fichier [`app-web.py](./app-web.py)

