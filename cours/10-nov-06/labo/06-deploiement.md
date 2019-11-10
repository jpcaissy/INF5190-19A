# Laboratoire 6

## Docker Compose

**L'utilisation de Docker nécessite des droits administrateurs (root). Malheureusement ce laboratoire ne peut
se faire sur les postes de l'UQAM. Je vous recommende de faire ce labo sur votre portable personnel.**

Référez-vous au labo de la semaine dernière (labo 6) pour l'installation de Docker.

Si vous êtes sous Windows ou Mac, il se peut que Docker Compose soit déjà installé.

Roulez la commande `docker-compose` pour valider :

```
$ docker-compose  version
docker-compose version 1.17.1, build unknown
docker-py version: 2.5.1
CPython version: 2.7.15+
OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
```

Si Docker Compose n'est pas installé, vous pouvez suivre les instructions ici : https://docs.docker.com/compose/install/#install-compose

### Exercice

#### Memcached

L'exercice est de rouler un environnement de développement qui contient la base de donnée PostgreSQL et Memcached (base de donnée clé-valeur).

Docker Compose récupère les images Docker à partir de Docker Hub. Nous pouvez aller chercher les versions actuel
de Postgers et Memcached :

* https://hub.docker.com/_/postgres
* https://hub.docker.com/_/memcached

Pour Postgres, nous allons utiliser `postgres:12-alpine` et pour Memcached : `memcached:1.5-alpine` (Alpine est une distro Linux populaire réputée pour faire des images très petites).

Commençons avec Memcached. Nous avons besoin d'exposer un port, mais nous n'avons pas besoin de volume car Memcached est une base de donnée qui ne persiste pas les données.

Créez un fichier `docker-compose.yml` avec le contenu suivant :

```yaml
version: "3"

services:
  cache:
    image: memcached:1.5-alpine
```

et roulez `docker-compose up -d` (l'option `-d` va rouler docker en arrière plan)

```
$ sudo docker-compose up -d
Starting labo_cache_1 ...
Starting labo_cache_1 ... done
```

Vous pouvez valider que Memcached roule avec `docker ps` :

```
$ sudo docker ps
CONTAINER ID        IMAGE                  COMMAND                  CREATED              STATUS              PORTS               NAMES
336983ddde21        memcached:1.5-alpine   "docker-entrypoint.s…"   About a minute ago   Up 53 seconds       11211/tcp           labo_cache_1
```

Par contre, nous n'avons pas exposé de port! Pour ce faire, nous allons rajouter

```yaml
    ports:
      - 11211:11211
```

au fichier yaml.

Le premier port est le port d'écoute de la machine, et le deuxième port est le port de l'application du conteneur docker.

```yaml
version: "3"

services:
  cache:
    image: memcached:1.5-alpine
    ports:
      - 11211:11211
```

On va ensuite recréer les conteneurs Docker. Il faut les arrêter avec `docker-compose stop` en premier.

```
$ sudo docker-compose down
Stopping labo_cache_1 ... done
Removing labo_cache_1 ... done
Removing network labo_default
$
$ sudo docker-compose up -d
Starting labo_cache_1 ...
Starting labo_cache_1 ... done
```

#### Postgres

Nous allons faire la même chose avec Postgres et le port 5432

```yaml
version: "3"

services:
  db:
    image: postgres:12-alpine
    ports:
      - 5432:5432
  cache:
    image: memcached:1.5-alpine
    ports:
      - 11211:11211
```

Et ensuite on va lancer les conteneurs

```
$ sudo docker-compose up -d
labo_cache_1 is up-to-date
Creating labo_db_1 ...
Creating labo_db_1 ... done
```

Par contre, pour PostgreSQL, nous avons besoin d'un peu plus de configuration. Nous avons besoin d'un
usager et d'une base de donnée. 

L'image Docker de postgres peut être configuré avec des variables d'environnements. Nous avons :

* `POSTGRES_PASSWORD`
* `POSTGRES_USER`
* `POSTGRES_DB`

Donc nous allons mettre ses variables d'environnements pour qu'un usager et une base de donnée soit instanciée.

```yaml
version: "3"

services:
  db:
    image: postgres:12-alpine
    ports:
      - 5432:5432
    environment:
        POSTGRES_USER: labo
        POSTGRES_PASSWORD: password
        POSTGRES_DB: labo_06
  cache:
    image: memcached:1.5-alpine
    ports:
      - 11211:11211
```

Et pour terminer, il nous faut une persistance! Dès qu'on arrête le conteneur Docker, nous perdons toutes les données.

Pour ce faire, nous allons définir un volume pointant sur `/var/lib/postgresql/data`, et nous allons dire à docker compose
de le gérer automatiquement

```yaml
version: "3"

volumes:
  volume-postgres:

services:
  db:
    image: postgres:12-alpine
    ports:
      - 5432:5432
    volumes:
      - volume-postgres:/var/lib/postgresql/data
    environment:
        POSTGRES_USER: labo
        POSTGRES_PASSWORD: password
        POSTGRES_DB: labo_06
  cache:
    image: memcached:1.5-alpine
    ports:
      - 11211:11211
```

Et si on roule un dernier docker compose up, tout devrait être mis en place :

```
$ sudo docker-compose down
Stopping labo_db_1    ... done
Stopping labo_cache_1 ... done
Removing labo_db_1    ... done
Removing labo_cache_1 ... done
Removing network labo_default
$ sudo docker-compose up -d
Creating network "labo_default" with the default driver
Creating volume "labo_volume-postgres" with default driver
Creating labo_db_1 ...
Creating labo_cache_1 ...
Creating labo_db_1
Creating labo_db_1 ... done
```

```
$ sudo docker ps
CONTAINER ID        IMAGE                  COMMAND                  CREATED             STATUS              PORTS                      NAMES
dbd7d6ac9fb9        memcached:1.5-alpine   "docker-entrypoint.s…"   42 seconds ago      Up 41 seconds       0.0.0.0:11211->11211/tcp   labo_cache_1
67cdfe2b58b5        postgres:12-alpine     "docker-entrypoint.s…"   42 seconds ago      Up 41 seconds       0.0.0.0:5432->5432/tcp     labo_db_1
```

#### Python

Une fois que nous avons les conteneurs Docker pour postgres et Memcached en place, on peut lancer l'application Flask sans problème.

Il nous faut installer `flask`,  `python-memcached` et `pg8000` (client postgres).

```
$ pip install flask python-memcached pg8000
```

On peut instancier la base de donnée :

```
$ flask init-db
```

et rouler l'application qui va utiliser Memcached et PostgreSQL :

```
$ FLASK_DEBUG=1 flask run
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 137-450-813
```
