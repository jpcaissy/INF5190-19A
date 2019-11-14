# Laboratoire 7

## Déploiement Heroku

Dans le cadre de ce laboratoire nous allons déployer une application Flask sur Heroku.

### Création de l'application

1. Si vous n'avez pas de compte déjà, inscrivez-vous sur Heroku : [https://signup.heroku.com/](https://signup.heroku.com/)
2. Connectez-vous à votre nouveau compte : [https://id.heroku.com/login](https://id.heroku.com/login)
3. Créez une nouvelle application
![Nouvelle application](./img/new-app.png)
4. Le nom de l'application doit être unique à travers Heroku. C'est le temps d'être original!
![](./img/new-app-2.png)
5. L'application que nous allons déployer utilise une base de donnée. Allez sur [https://elements.heroku.com/addons/heroku-postgresql](https://elements.heroku.com/addons/heroku-postgresql) et installer l'ajout en appuyant sur le bouton `Install Heroku Postgres`. Vous pouvez prendre le plan de base gratuit.
![](./img/heroku-postgres.png)

### Installation du CLI de Heroku

Si vous êtes sur votre poste personnel, suivez les instructions ici : https://devcenter.heroku.com/articles/heroku-cli#download-and-install

Si vous êtes sur les postes du laboratoire, suivez les instructions du `Standalone installation` : [https://devcenter.heroku.com/articles/heroku-cli#standalone-installation](https://devcenter.heroku.com/articles/heroku-cli#standalone-installation)

Une fois que c'est fait, connectez-vous à votre compte à partir de la ligne de commande avec `heroku login` :

```bash
$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/browser/[...]
Logging in... done
Logged in as [email]
```

### Premier déploiement

Nous allons déployer un exemple de ma station de vote.

1. Sur Github, créez un fork de [https://github.com/jpcaissy/poll-station](https://github.com/jpcaissy/poll-station)
2. Clonez le fork (`git clone`)
3. Dans le dépôt cloné, on peut configurer le déploiement Heroku avec la commande
```
heroku git:remote -a [nom de votre application Heroku]
```
e.g.: `heroku git:remote -a inf5190-flying-monkey`

Nous devons spécifier à Heroku comment lancer l'application Flask. Pour se faire, il faut créer un fichier `Procfile` et rajouter la ligne suivante:

```
web: FLASK_APP=poll flask run --host=0.0.0.0 --port=$PORT
```

`web` représente le nom de la ressource. Ça peut être n'importe quoi.

`FLASK_APP=poll flask run --host=0.0.0.0 --port=$PORT` représente la commande pour lancer l'application. En précisant `--host=0.0.0.0`, l'application n'écoutera pas sur localhost et le port d'écoute est aléatoire et géré par Heroku. Il est passé en variable d'environnement avec `$PORT`.

4. Ensuite il faut préciser à Heroku quelles sont les dépendances requises pour rouler l'application (flask, peewee, etc).

Créez un fichier `requirements.txt` et mettez-y les quatres dépendances suivantes :

```
flask
peewee
psycopg2
```

N.B.: `psycopg2` est la librairie pour PostgreSQL.

5. Il faut commiter les deux fichier sur votre fork:

```
$ git add Procfile requirements.txt
$ git commit -m "Ajout du fichier Procfile et requirements.txt"
$ git push
```

6. On peut tester le premier déploiement sur Heroku!

```
$ git push heroku
Counting objects: 3, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 293 bytes | 293.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
[...]
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 46.1M
remote: -----> Launching...
remote:        Released v6
remote:        https://inf5190-flying-monkey.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/inf5190-flying-monkey.git
 + b3a0843...3c1a212 solution -> master (forced update)
```

Et voilà, votre application est déployé! Vous pouvez la visiter avec 

```
https://[votre nom d'application heroku].herokuapp.com/
```

e.g: `https://inf5190-flying-monkey.herokuapp.com/`

Si vous recevez une erreur 500 (Internal Server Error), c'est normal! Nous devons configurer la base de donnée.

Vous pouvez voir le message d'erreur avec `heroku logs` :

```
$ heroku logs
2019-11-14T21:37:41.679379+00:00 app[web.1]: [2019-11-14 21:37:41,678] ERROR in app: Exception on / [GET]
2019-11-14T21:37:41.679407+00:00 app[web.1]: Traceback (most recent call last):
2019-11-14T21:37:41.679410+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/flask/app.py", line 2446, in wsgi_app

[...]

2019-11-14T21:41:06.274545+00:00 app[web.1]: File "/app/.heroku/python/lib/python3.6/site-packages/psycopg2/__init__.py", line 126, in connect
2019-11-14T21:41:06.274548+00:00 app[web.1]: conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
2019-11-14T21:41:06.274550+00:00 app[web.1]: peewee.OperationalError: could not connect to server: Connection refused
2019-11-14T21:41:06.274552+00:00 app[web.1]: Is the server running on host "localhost" (127.0.0.1) and accepting
2019-11-14T21:41:06.274554+00:00 app[web.1]: TCP/IP connections on port 3306?
2019-11-14T21:41:06.274557+00:00 app[web.1]: 
2019-11-14T21:41:06.275411+00:00 app[web.1]: 10.9.213.124 - - [14/Nov/2019 21:41:06] "GET / HTTP/1.1" 500 -
2019-11-14T21:41:06.276922+00:00 heroku[router]: at=info method=GET path="/" host=inf5190-flying-monkey.herokuapp.com request_id=c61a25fe-f353-48d2-8f31-95db2c5e4aba fwd="132.208.12.65" dyno=web.1 connect=2ms service=8ms status=500 bytes=449 protocol=https

```

On va clairement l'exception : `peewee.OperationalError: could not connect to server: Connection refused`

7. Configuration de la base de donnée.

Lorsque vous avez installé l'ajout Postgres, Heroku a rajouté une variable d'environnement nommé `DATABASE_URL`.

Sur votre panneau de contrôle Heroku, cliquez sur le tab `Settings`, puis `Reveal Config Vars`

![](./img/heroku-settings.png)

La valeur de DATABASE_URL devrait être quelque chose du genre :

```
postgres://huadneteefyqxb:[password]@ec2-54-197-238-238.compute-1.amazonaws.com:5432/d1tneov3bh37m8
```

* `huadneteefyqxb` est le nom d'usager
* `ec2-54-197-238-238.compute-1.amazonaws.com` est l'hôte
* `5432` est le port (par défaut)
* `d1tneov3bh37m8` est le nom de la base donnée.

Les informations pour se connecter à la base de donnée sont prises ici dans l'application : [https://github.com/jpcaissy/poll-station/blob/8c977181d2928c961ca3caf524f3d05300aae137/poll/models.py#L11-L14](https://github.com/jpcaissy/poll-station/blob/8c977181d2928c961ca3caf524f3d05300aae137/poll/models.py#L7-L14)

```python
DATABASE_NAME = os.environ.get('DB_DATABASE', 'poll')

def get_db():
    return {
        "user": os.environ.get('DB_USER', 'root'),
        "password": os.environ.get('DB_PASSWORD', 'password'),
        "host": os.environ.get('DB_HOST', 'localhost'),
        "port": int(os.environ.get('DB_PORT', '5432')),
    }
```

Il faut donc créer 4 nouvelles `Config Vars` dans heroku:

* `DB_USER` est le nom d'usager (huadneteefyqxb)
* `DB_PASSWORD` est le mot de passe
* `DB_HOST` est l'hôte (ec2-54-197-238-238.compute-1.amazonaws.com)
* `DB_PORT` est le port, on peut le laisser vide puisque par défaut c'est 5432
* `DB_DATABASE` est le nom de la base de donnée (d1tneov3bh37m8)

![](./img/heroku-db-settings.png)

8. Une fois que les variables d'environnements sont configurées, il faut redémarrer l'application:

![](./img/heroku-restart.png)

9. Par défaut la base de donnée est vide, donc il faut l'initialiser!

Pour rouler une commande sur heroku, on peut utiliser la commande `heroku run` :

```
$ heroku run "FLASK_DEBUG=1 FLASK_APP=poll flask init-db"
Running FLASK_DEBUG=1 FLASK_APP=poll flask init-db on ⬢ inf5190-flying-monkey... up, run.5982 (Free)
Initialized the database.
```

10. Et voilà, l'application est déployée!

![](./img/heroku-deployed.png)
