# Laboratoire 3

## Intégration d'API

Pour cet exercice, nous allons intégrer une API REST distante en Python. L'application est la même que celle utilisée
la semaine dernière.

Dans le dossier [**flask**](./flask), il y a une application Flask représentant des comptes bancaires.

Si vous ne l'avez pas déjà d'installer, il  faut installer [**peewee**](https://pypi.org/project/peewee/) avec

```
    pip install peewee
```

* Initialiser la base de donnée avec 
    ```
    FLASK_DEBUG=1 python -m flask init-db
    ```
* Rouler l'application avec
    ```
    FLASK_DEBUG=1 python -m flask run
    ```

### Python

Voici un exemple avec `urllib` pour récupérer la liste des comptes :

```python
from urllib.request import urlopen

with urlopen('http://localhost:5000/accounts') as response:
     data = response.read()
     headers = response.headers
     http_code = response.code

data #b'[]\n'
 ```

Pour désérialiser le contenu, vous pouvez utiliser `json`

```python
import json
data = {"test": "Hello World", "balance": 100, "active": True}

print data['test']

serialized_json = json.dumps(data)

deserialized_json = json.loads("""
    '{"test": "Hello World", "balance": 100, "active": true}'
""")

print deserialized_json['test']
```

### Exercice 1

Intégrer les 5 routes de l'application Flask:

1. `GET /accounts`
2. `GET /accounts/<int:id>`
3. `GET /accounts/<int:id>/transactions`
3. `GET /accounts/<int:id>/transactions/<int:transaction_id>`
4. `POST /accounts`

    Exemple :

    ```json
    {
        "account": {
            "owner": "Toto Foobar",
            "current_balance": 1000
        }
    }
    ```

5. `POST /transactions`

    Exemple :

    ```json
    {
        "transaction": {
            "from_account": 1,
            "to_account": 2,
            "amount": 500
        }
    }
    ```

### Exercice 2

`urlopen` va lancer une exception si la requête retourne un code d'erreur 40X (404, 422, etc).

Il est possible de récupérer l'exception avec un `try/except` :

```
from urllib.error import HTTPError
from urllib.request import urlopen

try:
    with urlopen('http://localhost:5000/does-not-exist') as response:
         html = response.read()
         headers = response.headers
         http_code = response.code
except HTTPError as e:
    code = e.code
    headers = e.headers
    data = e.read()
```

Pour cet exercice, gérer les 2 erreurs de `POST /transactions` lorsque l'un des compte n'existe pas et lorsque
les fonds sont insuffisants.
