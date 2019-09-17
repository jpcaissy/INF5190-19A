% INF5190 - Tests d'applications Web
% Jean-Philippe Caissy
% 18 septembre 2019

# Tests d'applications Web

*Un code non testé est fondamentalement brisé*

Les tests d'applications Web assurent une assurance qualité de l'application testé.

Il existe trois niveaux de tests :

* Tests unitaires
* Tests fonctionnelles
* Tests d'intégrations

# Suite de tests

Le différents tests d'une application sont regroupés en une suite de tests.

Ils sont regroupés dans les trois niveaux (unitaire, fonctionnelles et intégration).

Une suite de test efficace possède les 4 caractéristiques suivantes :

1. Rapide
2. Complet
3. Fiable
4. Hermétique

# Suite de tests
## 1. Rapide

* Plus un test est rapide, plus souvent il est exécuté lors du développement
* Les tests devraient être à chaque changement au code
* Une boucle de rétroaction rapide (_feedback loop_) aide au développement
* Si un test devient trop lent, il pourrait être ignoré

# Suite de tests
## 2. Complet

* La suite de test devrait couvrir tout le code de l'application
* Supprimer du code de l'application doit faire échouer les tests
* Si la couverture n'est pas complète, il est difficile d'avoir confiance aux changements

# Suite de tests
## 3. Fiable

* Les tests ne devraient pas aléatoirement échoués
* Des faux positifs minent a confiance à la suite de tests
* Les erreurs intermittents sont difficile à diagnostiquer


# Suite de tests
## 4. Hérmétique

* Les tests roulent indépendant d'eux autres.
* Chacune des suites de test est responsable pour s'initialiser et libérer les ressources à la fin
* Les tests ne sont pas dépendant d'un ordre d'exécution

# Types de tests
## Tests unitaires

* Tests de premier niveau
* Sert à tester des unités spécifique de l'application web
* Ne doit tester et affirmer **qu'une seule** partie spécifique de l'application
* Ne nécessite pas l'instanciation complète de l'application Web
* L'interaction entre d'autres composantes est souvent remplacés par des _mocks_
* Les tests de modèle sont en grande partie des tests unitaires

# Types de tests
## Tests unitaires

Un test unitaire sert à tester : 

* La fonctionnalité et la non-fonctionnalité d'une méthode
* La gestion des erreurs et des exceptions
* Les cas limites

# Types de tests
## Tests unitaires

Un test unitaire devrait être rapide, complet, fiable et hermétique :

* Pas de manipulation de fichiers ou de base de donnée
* Pas de communication réseau
* Pas d'effets de bords

# Types de tests
## Tests fonctionnels

* Tests de 2e niveau
* Niveau d'abstraction supérieur aux tests unitaires
* Vérifie une fonctionnalité du système
* Nécessite l'instanciation de l'application Web, car peut interagir avec plusieurs composantes
* Il s'agit souvent d'une seule requête à un contrôleur
* Les tests de contrôleurs et vues sont des tests fonctionnels

# Types de tests
## Tests fonctionnels

Un test fonctionnel sert à tester :

* La fonctionnalité d'une composante du système
* Un test fonctionnel va souvent couvrir l'équivalent de plusieurs tests unitaires

# Types de tests
## Tests fonctionnels

Un test fonctionnel peut :

* Manipuler des fichiers ou une base de donnée
* Faire des communications réseaux
* Avoir des effets de bords

**Mais** :

* Les effets de bords doivent être testés
* Le test fonctionnel doit nettoyer après celui-ci :
    * Toutes opérations de manipulation de fichiers doit être défaites
    * La base de donnée doit être remise dans l'état initiale

# Types de tests
## Tests d'intégrations

* Tests de 3e nievau
* Niveau d'abstraction similaire à une requête Web
* Vérifie que chacune des composantes s'intègre au système complet
* Un test d'intégration représente une ou plusieurs requêtes Web à l'application
* Exemple : Enregistrer un nouvel utilisateur sur l'application Web, et vérifier que celui-ci peut se connecter

# Types de tests
## Tests d'intégrations

Un test d'intégration va tester :

* L'envoie d'une requête HTTP à l'application Web
* Va couvrir du code touché par plusieurs composantes (modèle, vue et contrôleur)
* Peut faire plusieurs requêtes web dans un seul test

# Types de tests
## Flask

Flask (et Python!) possèdent des outils de tests très puissants.

Flask expose un client Web afin de simuler les requêtes Web à l'application et ainsi les tester.

# Liens utiles

* [Testing Rails](https://books.thoughtbot.com/assets/testing-rails.pdf)
