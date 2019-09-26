# Laboratoire 3

**Le laboratoire aura lieu dans le local PK-S1575**

## Projet de session

Assurez-vous de rejoindre le projet de session sur Github Classroom.

1. Créer un compte [Github](https://github.com) si ce n'est déjà pas le cas.
2. Rendez-vous sur la page du projet de session :
    [**https://classroom.github.com/g/oH9-4nj2**](https://classroom.github.com/g/oH9-4nj2)
3. Acceptez le travail, et identifier vous dans la liste en choisissant votre code permanent
    **Assurez-vous de ne pas prendre le code de quelqu'un d'autre!**
4. Créer une équipe individuelle, ou rejoignez l'équipe de votre collègue si vous faites la remise à 2.
5. Votre dépôt Github privé sera créé, vous pouvez commencer à l'utiliser.

## REST

Modéliser les routes, méthodes HTTP et un exemple de données JSON d'une API REST qui représente
l'emprunt de livres à un bibliothèque.

Les ressources sont :

* Un livre
* Un membre de la bibliothèque
* Les emprunts

Voici les routes à définir, avec deux exemples.

1. Créer un nouveau livre

    `POST https://api.example.com/bibliotheque/livre/`

    ```json
    {
        "livre": {
            "titre": "Release It!",
            "auteur": [
                "Michael T. Nygard"
            ],
            "edition": 2018,
            "copies": 3
        }
    }
    ```

2. Récupérer les emprunts d'un livre

    `GET https://api.example.com/bibliotheque/livre/10/emprunts`

    ```json
    {
        "emprunt": {
            "id": 42,
            "livre_id": 10,
            "membre_id": 25,
            "date_emprunt": "2019-09-25",
            "date_retour_prevu": "2019-10-02",
            "date_retour": null,
        }
    }
    ```

3. Créer un nouveau membre de la bibliothèque (avec nom, prénom, courriel)

    `POST https://api.example.com/bibliotheque/membre`

    ```json
    {
        "membre": {
            "prenom": "Jean-Philippe Caissy",
            "nom": "Caissy",
            "courriel": "caissy.jean-philippe@uqam.ca"
        }
    }
    ```

4. Récupérer la liste des emprunts d'un livre

    `GET https://api.example.com/bibliotheque/livre/<livre_id>/emprunts`

5. Récupérer la liste des livres actuellement empruntés par un membre

    `GET https://api.example.com/bibliotheque/membre/<membre_id>/emprunts`

6. Étendre la date de retour prévu d'un livre emprunté par un membre

    `PATCH https://api.example.com/bibliotheque/membre/<membre_id>/emprunts/<emprunt_id>`

    ```json
    {
        "emprunt": {
            "date_retour_prevu": "2019-10-05"
        }
    }
    ```

7. Marquer un livre comme retourné (ne pas supprimer l'emprunt)

    `PATCH https://api.example.com/bibliotheque/membre/<membre_id>/emprunts/<emprunt_id>`

    ```json
    {
        "emprunt": {
            "date_retour": "2019-09-28"
        }
    }
    ```

8. Supprimer un livre

    `DELETE https://api.example.com/bibliotheque/livre/<livre_id>`
