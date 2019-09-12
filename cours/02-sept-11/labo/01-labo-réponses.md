## Python

```python
ma_liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

1. Récpuérer le 3e élément de la liste

```python
print(ma_liste[2]) # 0 est le 1er élément, 1 est le 2e élément, 2 est le 3 élément, etc
```

2. Avec la syntaxe `for ... in` itérer sur la liste et afficher le double de l'entier
```python
for n in ma_liste:
    print(n * 2)
```

    2.1 Afficher l'entier à l'intérieur d'une string (i.e.: `La valeur est 2`, `La valeur est 4`, etc)
    ```python
    for n in ma_liste:
        print("La valeur est {0}".format(n))
    ```
    2.2 Même chose que 2.1, mais utiliser la fonction de _slice_ des listes pour itérer du 4e élément inclusivement de la liste à la fin
    ```python
    for n in ma_liste[3:]:
        print("La valeur est {0}".format(n))
    ```
    2.3 Grace à la méthode `range`, rajouter les éléments 10 à 19 à `ma_liste`.
    ```python
    for n in range(10, 20):
        ma_liste.append(n)
    ```

```python
cours = {
    "INF5190": {
        "nom": "Programmation Web avancé",
        "groupe": "020",
    },
    "INF3190": {
        "nom": "Introduction à la programmation Web",
        "groupe": "020",
    }
}
```

3. À partir du dictionnaire `cours`, afficher le nom du cours de INF5190 et INF3190
```python
print("Le groupe est {0}".format(cours['INF5190']['groupe']))
```

4. Modifier le groupe de INF3190 pour `030`
```python
cours['INF5190']['groupe'] = "030"
```

5. Pour chacun des cours, rajouter l'horaire à la structure de donnée (INF5190: mercredi soir, INF3190: mardi soir)
```python
cours['INF5190']['horaire'] = "mercredi soir"
cours['INF3190']['horaire'] = "mardi soir"
```

ou

```python
cours['INF5190']['horaire'] = {"jour": "mercredi", "heure": "18h"}
cours['INF3190']['horaire'] = {"jour": "mardi", "heure": "18h"}
```

6. Rajouter le cours INF4170 - Architecture des ordinateurs pour le groupe 040 avec un horaire le jeudi soir

```python
cours['INF4170'] = {
    "nom": "Architecture des ordinateurs",
    "groupe": "040",
    "horaire": {
        "jour": "jeudi",
        "heure": "18h"
    }
}
print(cours)
```

----

7. Créer un fichier texte et mettez y quelques lignes. Créer un script python qui va ouvrir le fichier avec la
    méthode `open` et lire puis afficher chacune des lignes du fichier.

    Indice : utilisez la méthode `readline` avec a syntaxe `with`.
    ```python
    with open("mon_fichier.text", "r") as f:
        ligne = f.readline()
        while ligne:
            print(ligne)
            ligne = f.readline()
    ```

8. Rajouter une gestion d'exception qui gère un fichier qui n'existe pas `try/except`
    ```python
    try:
        with open("mon_fichier.txt", "r") as f:
            ligne = f.readline()
            while ligne:
                print(ligne)
                ligne = f.readline()
    except FileNotFoundError:
        print("Le fichier n'existe pas")
    ```


----

9. Créer un module nommé operations qui contien la méthode `lire_toutes_les_lignes`. Cette méthode prend en argument
    un nom de fichier et va retourner une liste de toutes les lignes du fichiers.

    ```python
    >>> from operations import lire_toutes_les_lignes
    >>> lire_toutes_les_lignes("un fichier existant")
    >>> ['ligne 1', 'ligne 2', 'ligne 3']
    ```

    Fichier `operations.py`:
    ```python
    def lire_toutes_les_lignes(fichier):
        lignes = []
        try:
            with open("mon_fichier.txt", "r") as f:
                ligne = f.readline()
                lignes.append(line)
                while ligne:
                    ligne = f.readline()
                    lignes.append(line)
        except FileNotFoundError:
            print("Le fichier n'existe pas")

        return lignes
    ```

    À partir de la console Python :
    ```python
    from operations import lire_toutes_les_lignes
    lire_toutes_les_lignes("mon_fichier.txt")
    ```

