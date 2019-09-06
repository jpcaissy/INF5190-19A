## Installation de Python

Dans le cadre du cours, nous allons utiliser Python 3.6+ (3.7 et 3.8 sont supportés).

Tu peux l'installer nativement sur votre machine : Windows, Macos et Linux sont tous supportés.

### Linux (Ubuntu/Debian)

Par défaut Ubuntu 18.04 vient avec Python 2 d'installé. On peut utiliser apt pour installer la version 3:

```
sudo apt-get install python3
```

Ensuite `python3` sera disponible sur la ligne de commande :

```
$ python3
Python 3.6.8 (default, Jan 14 2019, 11:02:34)
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello World!")
Hello World!
>>>
```

Il faut s'assurer de rouler la version 3, et non pas la version 2! Sur mon système, j'ai les deux versions :

```
jpcaissy@jpcaissy-xps (master)$ python -V
Python 2.7.15+
jpcaissy@jpcaissy-xps (master)$ python3 -V
Python 3.6.8
```

### MacOS

La manière la plus simple d'installer Python3 sous MacOS est d'utiliser Homebrew.

Les instructions sont disponibles ici : [https://brew.sh/](https://brew.sh/), mais il suffit de rouler cette commande :

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Une fois que Homebrew est installé, il suffit d'installer Python 3 :

```
brew install python
```

Comme pour Ubuntu, la version 2 et la version 3 sera installé sur votre poste. Assurez-vous d'utiliser la commande `python3` et non pas `python`.

### Windows

Malheureusement je n'ai pas de poste Windows, alors je n'ai pas pu tester les instructions.

Sous Windows, il semble exister plusieurs manières d'installer Python. Si vous avez déjà [Chocolatey](https://chocolatey.org/install) d'installé, vous pouvez l'installer directement avec 

```
choco install python
```

Sinon, il est également possible d'utiliser l'installeur disponible sur le site officiel : [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/).

Il faut s'assurer d'installer la version 3. Une fois installé, tu peux confirmer la version avec la commande

```
python -V
```

ou

```
python3 -V
```

## IDE

Je n'utilise personellement pas d'IDE, mais tu es libre (et même encouragé!) d'utiliser l'environement de dévelopement qui te convient le mieux.

J'ai eu des bons commentaires du support Python dans VSCode et de Sublime Text. Il existe également PyCharm qui est un IDE propre à Python.

## Hello World

Assurez-vous que le tout fonctionne.

Enregistrer un fichier nommé `hello-world.py` avec le contenu suivant :

```python
text = "World"
i = 0
while i < 10:
    print("Hello {0}".format(text))
    i += 1
    if i == 5:
        print("Déjà rendu à 5!")
```

Une fois roulé, voilà ce que ce petit script va afficher :

```
$ python3 hello-world.py
Hello World
Hello World
Hello World
Hello World
Hello World
Déjà rendu à 5!
Hello World
Hello World
Hello World
Hello World
Hello World
```
