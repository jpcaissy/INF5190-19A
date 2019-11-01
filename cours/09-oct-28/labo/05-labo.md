# Laboratoire 5

## Docker

**L'utilisation de Docker nécessite des droits administrateurs (root). Malheureusement ce laboratoire ne peut
se faire sur les postes de l'UQAM. Je vous recommende de faire ce labo sur votre portable personnel.**

### Installation

Docker est disponible en eux versions : Community Edition (CE) et Enterprise Edition (EE). Nous allons utiliser **Docker CE**

Détails complets d'installation : https://docs.docker.com/v17.09/engine/installation/


#### Windows

Suivez les instructions et installez le *Stable Channel*

https://docs.docker.com/v17.09/docker-for-windows/install/

#### Mac

Suivez les instructions et installez le *Stable Channel*

https://docs.docker.com/v17.09/docker-for-mac/install/

#### Ubuntu

Les détails de l'installation pour Ubuntu sont disponible ici : https://docs.docker.com/v17.09/engine/installation/linux/docker-ce/ubuntu/#install-docker-ce

Installez Docker EE avec les instructions suivantes : 

1. Assurez-vous de supprimer touets les anciennes versions

```
    $ sudo apt-get remove docker docker-engine docker-ce docker.io
```

2. Mettez à jour apt

```
    $ sudo apt-get update
```

3. Installez les dépendances

```
    $ sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
```

4. Ajoutez la clé GPG de Docker

```
    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```

5. Ajoutez le dépôt APT de Docker

```
    $ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
```

6. Mettez à jour apt

```
    $ apt-get update
```

7. Installez Docker CE

```
    $ sudo apt-get install docker-ce
```

#### Autre Linux

Vous trouverez les instructions pour installer Docker sur d'autres plateformes Linux ici : https://docs.docker.com/v17.09/engine/installation/#server

### Hello World

Assurez-vous que Docker fonctionne:

    $ docker -v
    Docker version 19.03.4, build 9013bf583a

Nous allons rouler le Hello World de Docker disponible ici : https://hub.docker.com/_/hello-world

Roulez l'image Hello World avec la commande suivante :

    $ docker run hello-world

    Hello from Docker!
    This message shows that your installation appears to be working correctly.

    [...]

**Si vous avez des problèmes de permission, roulez la commande avec `sudo docker run hello-world`**

### BusyBox

Maintenant que vous avez Docker qui fonctionne, nous allons faire quelques exercice avec [BusyBox](https://en.wikipedia.org/wiki/BusyBox).

Récupérez l'image de BusyBox

    $ docker pull busybox

La commande `pull` va télécharger l'image de busybox à partir du registre de Docker : https://hub.docker.com/_/busybox/

Maintenant, on va instancier un conteneur avec l'image de busybox

    $ docker run busybox
    $

Il ne se passe rien et c'est normale! La commande `docker run` a démarré le conteneur, mais puisqu'aucune commande
n'a été exécuté, le conteneur s'est arrêté immédiatement.

    $ docker run busybox echo "Hello World, à partir du conteneur!"
    Hello World, à partir du conteneur!

Comme vous avez pu le constater, la commande roule très rapidement. Et pourtant, un conteneur avec busybox a été
instancié, et la commande `echo` a bien roulé. Imaginez si on avait du lancer une machine virtuelle, démarrer l'OS et
exécuté cette commande. Ça aurait pris une bonne minute au moins.

La commande `docker ps` affiche tous les conteneurs qui sont entrain d'être roulé.

    $ docker ps
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES

Évidemment puisque le conteneur ne roule pas, la commande `docker ps` n'affiche rien. Avec `docker ps -a` on peut
voir un historique des conteneurs 

    $ docker ps -a
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
    a71f239309ab        busybox             "echo 'Hello World, …"   3 minutes ago       Exited (0) 3 minutes ago                        cool_lovelace
    546d9f5ebafe        busybox             "echo 'Hello World!'"    4 minutes ago       Exited (0) 4 minutes ago                        unruffled_engelbart
    e9ee9e58fa9a        busybox             "sh"                     5 minutes ago       Exited (0) 5 minutes ago                        cocky_villani
    5e5f01d6ed53        busybox             "sh"                     5 minutes ago       Exited (0) 5 minutes ago                        gallant_vaughan
    b329e2b02f2e        hello-world         "/hello"                 10 minutes ago      Exited (0) 10 minutes ago                       happy_hellman
    cba449732410        nginx               "nginx -g 'daemon of…"   44 hours ago        Exited (0) 44 hours ago                         recursing_khayyam
    dc0300f0d7d5        ubuntu              "/bin/bash"              44 hours ago        Exited (0) 44 hours ago                         nervous_franklin
    f0b3c71cf8c2        ubuntu              "/bin/bash"              44 hours ago        Exited (130) 44 hours ago                       eager_ellis
    469aaa8ebc00        ubuntu              "/bin/bash"              44 hours ago        Exited (127) 44 hours ago                       stupefied_bohr
    a3a356b2d997        ubuntu              "/bin/bash"              44 hours ago        Exited (0) 44 hours ago                         elated_greider
    d8f07ad803b8        ubuntu              "/bin/bash"              44 hours ago        Exited (0) 44 hours ago                         modest_tu

    [...]

Vous remarquerez le statut `Exited (0) ...`

On peut également attacher un terminal à un conteneur avec les options `-ti` :

    $ docker run -ti busybox
    / # ls
    bin   dev   etc   home  proc  root  sys   tmp   usr   var
    / #

Si vous ouvrez un autre terminal, vous verrez le conteneur qui roule :

    $ docker ps
    CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
    2b505c2df5f9        busybox             "sh"                9 seconds ago       Up 7 seconds                            cranky_heisenberg

Pour quitter le conteneur, simplement rouler la commande exit

    $ docker run -ti busybox
    / # ls
    bin   dev   etc   home  proc  root  sys   tmp   usr   var
    / # exit

Docker garde des artéfacts des conteneurs qui ont été roulé. C'est une bonne pratique de nettoyer le tout de temps
à autre avec `docker rm`. Il suffit de prendre l'identifiant du conteneur.

    $ docker rm a71f239309ab 546d9f5ebafe 2b505c2df5f9
    $

Ou pour tout supprimer :

    $ docker rm $(docker ps -a -q -f status=exited)

### Construire une image

Cet exercice consiste à construire et lancer une image Docker.

Créez un fichier `hello.py` avec le contenu suivant :

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
```


1. Créez un fichier `Dockerfile`
2. La commande `FROM` indique l'image de base que nous allons utiliser `3.7-buster`, tel que définit ici : https://hub.docker.com/_/python

```dockerfile
FROM python:3.7-buster
```

3. Puisqu'il s'agit d'une application flask, nous devons installer les dépendances dans l'image

```dockerfile
RUN pip install flask
```

4. Par défaut Flask va rouler sur le port 5000. Pour transférer la connexion, nous devons exposer le port

```dockerfile
EXPOSE 5000
```

5. Ensuite on doit inclure notre application dans l'image

```dockerfile
COPY hello.py /hello.py
```

6. Et finalement, on doit fournir un point d'entrée à notre image. Il s'agit de la commande qui sera roulé par `docker run`

```dockerfile
CMD python /hello.py
```

7. La comande `docker build` permet de construire l'image. Pour nous aider, nous allons utiliser l'option `-t` pour nommer l'image avec un tag.

```
$ docker build -t labo5 .
Sending build context to Docker daemon  40.96kB
Step 1/5 : FROM python:3.7-buster
3.7-buster: Pulling from library/python
c7b7d16361e0: Pull complete
b7a128769df1: Pull complete
1128949d0793: Pull complete
667692510b70: Pull complete
bed4ecf88e6a: Pull complete
8a8c75f3996a: Pull complete
8c90ed29fb66: Pull complete
984b0e9d1433: Pull complete
d930e1ce5d4a: Pull complete
Digest: sha256:f0db6711abee8d406121c9e057bc0f7605336e8148006164fea2c43809fe7977
Status: Downloaded newer image for python:3.7-buster
 ---> 023b89039ba4
Step 2/5 : RUN pip install flask
 ---> Running in c1ce514c5329
Collecting flask
  Downloading https://files.pythonhosted.org/packages/9b/93/628509b8d5dc749656a9641f4caf13540e2cdec85276964ff8f43bbb1d3b/Flask-1.1.1-py2.py3-none-any.whl (94kB)
Collecting click>=5.1
  Downloading https://files.pythonhosted.org/packages/fa/37/45185cb5abbc30d7257104c434fe0b07e5a195a6847506c074527aa599ec/Click-7.0-py2.py3-none-any.whl (81kB)
Collecting itsdangerous>=0.24
  Downloading https://files.pythonhosted.org/packages/76/ae/44b03b253d6fade317f32c24d100b3b35c2239807046a4c953c7b89fa49e/itsdangerous-1.1.0-py2.py3-none-any.whl
Collecting Jinja2>=2.10.1
  Downloading https://files.pythonhosted.org/packages/65/e0/eb35e762802015cab1ccee04e8a277b03f1d8e53da3ec3106882ec42558b/Jinja2-2.10.3-py2.py3-none-any.whl (125kB)
Collecting Werkzeug>=0.15
  Downloading https://files.pythonhosted.org/packages/ce/42/3aeda98f96e85fd26180534d36570e4d18108d62ae36f87694b476b83d6f/Werkzeug-0.16.0-py2.py3-none-any.whl (327kB)
Collecting MarkupSafe>=0.23
  Downloading https://files.pythonhosted.org/packages/98/7b/ff284bd8c80654e471b769062a9b43cc5d03e7a615048d96f4619df8d420/MarkupSafe-1.1.1-cp37-cp37m-manylinux1_x86_64.whl
Installing collected packages: click, itsdangerous, MarkupSafe, Jinja2, Werkzeug, flask
Successfully installed Jinja2-2.10.3 MarkupSafe-1.1.1 Werkzeug-0.16.0 click-7.0 flask-1.1.1 itsdangerous-1.1.0
Removing intermediate container c1ce514c5329
 ---> f9000efabe48
Step 3/5 : EXPOSE 5000
 ---> Running in d29192c9cdd4
Removing intermediate container d29192c9cdd4
 ---> 1bc39c9a4d7d
Step 4/5 : COPY hello.py /hello.py
 ---> 12e89f668a64
Step 5/5 : CMD python /hello.py
 ---> Running in cb60497f2d75
Removing intermediate container cb60497f2d75
 ---> 56916b568bd7
Successfully built 56916b568bd7
Successfully tagged labo5:latest
```

8. Roulez l'image!

```
$  docker run labo5
 * Serving Flask app "hello" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

9. Par contre, nous devons préciser le port à transférer pour pouvoir se connecter au conteneur de l'extérieur avec l'option `-p`. L'option prend deux ports, un port
pour la machine hôte, et le port du conteneur (grâce à `EXPOSE 5000`).

```
$ docker run -p8080:5000 labo5
 * Serving Flask app "hello" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

L'application Flask est maintenant accessible à partir de [http://localhost:8080/](http://localhost:8080/)!

10. Vous pouvez arrêter le conteneur avec `docker stop`

```
$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
8cf5e35b7550        labo5               "/bin/sh -c 'python …"   42 seconds ago      Up 41 seconds       0.0.0.0:8080->5000/tcp   great_ramanujan
$ docker stop 8cf5e35b7550
```
