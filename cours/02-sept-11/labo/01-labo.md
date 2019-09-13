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

Les méthodes `keys()`, `values()` d'un dictionnaire retournent respectivement la liste des clés et la liste des
valeurs du dictionnaire :

La méthode `items()` retourne une liste liste de tuple clé-valeur du dictionnaire.

```python
>>> print(list(cours.keys()))
['INF5190', 'INF3190']
>>> print(list(cours.values()))
[{'nom': 'Programmation Web avancé', 'groupe': '030'}, {'nom': 'Introduction à la programmation Web', 'groupe': '020'}]
>>> print(list(cours.items()))
[('INF5190', {'nom': 'Programmation Web avancé', 'groupe': '030'}), ('INF3190', {'nom': 'Introduction à la programmation Web', 'groupe': '020'})]
```

Comme toutes les listes, on peut donc itérer sur les clés, les valeurs ou les items d'un dictionnaire.

```python
>>> for cle, valeur in cours.items():
...   print("Sigle: {0} - {1}".format(cle, valeur['nom']))
...
Sigle: INF5190 - Programmation Web avancé
Sigle: INF3190 - Introduction à la programmation Web
```

3. À partir du dictionnaire `cours`, afficher le nom du cours de INF5190 et INF3190
4. Modifier le groupe de INF3190 pour `030`
5. Pour chacun des cours, rajouter l'horaire à la structure de donnée (INF5190: mercredi soir, INF3190: mardi soir)
6. Rajouter le cours INF4170 - Architecture des ordinateurs pour le groupe 040 avec un horaire le jeudi soir
7. Itérer sur les cours, et afficher le sigle et le groupe du cours

----

8. Créer un fichier texte et mettez y quelques lignes. Créer un script python qui va ouvrir le fichier avec la
    méthode `open` et lire puis afficher chacune des lignes du fichier.

    Indice : utilisez la méthode `readline` avec a syntaxe `with`.
9. Rajouter une gestion d'exception qui gère un fichier qui n'existe pas `try/except`

----

10. Créer un module nommé operations qui contien la méthode `lire_toutes_les_lignes`. Cette méthode prend en argument
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

1. Le premier exercice revient sur les retours d'envoies (_callbacks_).

Dans l'exemple montré en classe avec WSGI :

```python
def mon_application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"<html><body><h1>Hello World</h1></body></html>"]
```

Il est important de comprendre que le deuxième argument `start_response` est en fait un pointeur de fonction.

En Python, tout est une méthode. Voici un exemple:

```python
>>> def ma_methode(input, autre_methode):
        return autre_methode(input)

>>> ma_methode
<function ma_methode at 0x7f842d583bf8>
>>> print
<built-in function print>
>>> print("test")
test
>>> ma_methode("test", print)
test
```

Dans cet exemple on peut voir que `ma_methode` sans paranthèses est une syntaxe valide. Cela ne fait
que pointer vers la méthode. On peut passer cette méthode en argument.

C'est la même chose avec `print`. `print` seul pointe vers la référence de la méthode, et `print("test")` appelle
la méthode avec l'argument passé en paramètre.

Voici un autre exemple :

```python
>>> def addition(a, b):
...     return a + b
>>> def multiplication(a, b):
...     return a * b
```

J'ai deux méthodes `addition` et multiplication` que je peux appeler moi-même :
```python
>>> addition
<function addition at 0x7f842d583c80>
>>> addition(2, 5)
7
```

Je peux également les passer en paramètre à ma méthode operation :

```python
>>> def operation(a, b, operation):
        return operation(a, b)

>>> operation(2, 5, addition)
7
>>> operation(2, 5, multiplication)
10
```

Si on revient à notre exemple avec WSGI : 

```python
def mon_application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"<html><body><h1>Hello World</h1></body></html>"]
```

C'est le même principe. `start_response` est un argument qui point vers une méthode du serveur WSGI, tel que 
définit par la spécification [PEP 3333](https://www.python.org/dev/peps/pep-0333/#the-start-response-callable) :

> The second parameter passed to the application object is a callable of the form start_response(status, response_headers, exc_info=None). 
> The start_response callable is used to begin the HTTP response, and it must return a write(body_data) callable (see the Buffering and Streaming section, below).

Donc lorsque la méthode `start_response` est appelé, le début de la réponse HTTP est envoyé au client.

2. Installer le serveur WSGI `waitress`:
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

3. Compléter le fichier [`app_web.py/](./app_web.py)

Vous pouvez lancer l'application avec la commande suivante :

```
$ python3 app_web.py
Serving on http://0.0.0.0:8080
```

Et l'application web sera disponible à l'adresse [http://127.0.0.1:8080/](http://127.0.0.1:8080)
