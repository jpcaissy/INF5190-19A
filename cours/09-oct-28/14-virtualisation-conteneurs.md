% INF5190 - Virtualisation et conteneurs
% Jean-Philippe Caissy
% 30 octobre 2019

---
header-includes:
 - \usepackage{fvextra}
 - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
---

#

Il y a eu des changements à l'horaire du plan de cours depuis le début de la session.

* La première partie du cours était consacré à la conception d'applications Web :
    * HTTP
    * Fonctionnement d'une application Web
    * Sécurité d'applications Web
    * Modèle MVC
    * REST
    * Formats de sérialisation

* La deuxième moitié de la session se penche sur la gestion et la maintenance d'une application Web :
    * Virtualisation et conteneurs
    * Déploiements
    * Microservices
    * Résilience et performance d'applications Web
    * Maintenance

# Virtualisation

* Virtualisation : création et utilisation d'un environnement virtuel, incluant les périphériques matériels (CPU,
carte de son, etc), les engins de stockage (disque dur) et ressources réseaux (carte réseaux).

* Concepts : hôte (*host*) et invité (*guest*)
* Un environnement virtuel est isolé de l'hôte et chacun des invités sont isolés d'eux-mêmes.

# Virtualisation

![Schéma de virtualisation](./img/virtualisation.pdf){height=60%}

Source : [John Aplessed [Public domain]](https://commons.wikimedia.org/w/index.php?title=File:Hardware%5fVirtualization%5f%28copy%29.svg&oldid=256242957)

# Virtualisation

![2 hôtes Linux sous VirtualBox](./img/virtualbox-hosts.pdf)

# Virtualisation

![Matériel simulés configurable dans VirtualBox](./img/virtualbox.pdf)

# Virtualisation
## Avantages

* Environnement reproductible
* Sécurité par la séparation et l'isolation des systèmes
* Meilleur contrôle des coûts
* Mise à l'échelle (_scaling_) plus facile et rapide
* Plus grande flexbilité (IP dynamique, migration, etc)

# Virtualisation
## Désavantages

* En raison de la simulation des environnements, demande plus de ressources
* Ressources physiques (RAM, disque dur, réseau) partagées, donc plus difficile à gérer
* Redondance entre chaque invité (N systèmes d'exploitation complet)

# Virtualisation
## Exemples de scénarios

* Rouler une application qui n'est pas supporté par l'OS de l'hôte
* Tester et évaluer d'autres OS
* Virtualisation de serveurs : plusieurs serveurs virtuels roulent sur le même matériel physique
* Dupliquer des environnements
* Protéger des environnements

# Virtualisation
## Types de virtualisation

### Virtualisation complète

L'invité n'est aucunement conscient qu'il roule sur un environnement virtuel. Aucune modification à l'hôte n'est
nécessaire. Le matériel physique est complètement simulé par l'hôte et le système invité croit faire des appels
directement sur le matériel physique.

Ex : VirtualBox


### Paravirtualisation

Le système invité qui est virtualisé est au courant qu'il roule dans un environnement virtuel et utilise des
pilotes (*drivers*) spécifiques au lieu d'accéder au matériel physique (disque, RAM, etc).

Ex : Xen

# Virtualisation
## Application Web

On peut utiliser une application Web pour virtualiser et isoler les composantes :

* Application Web
* Serveur HTTP
* Base de donnée
* etc

# Virtualisation
## Application Web

![Virtualisation d'une application Web](./img/virtualisation-app-web.pdf)

# Conteneurs

![Conteneurs](./img/conteneurs.pdf)

# Conteneurs

* Paravirtualisation : le matériel n'est pas virtualisé
* Le conteneur partage le système d'exploitation hôte
    * Puisque le OS hôte est partagé : souvent plus léger (RAM, espace disque)
* Mêmes avantages que la virtualisation complète :
    * Isolation, environnement reproductible, etc

# Conteneurs
## Différence entre virtualisation complète

* Virtualisation : rouler des applications qui nécessitent toutes les ressources et fonctionnalités d'un système
d'exploitation
* Conteneurs : maximiser les ressources disponible d'un système d'exploitation en roulant le plus d'applications possible

| Virtualisation | Conteneurs |
|-----------------------------------|------------------------------------------------|
| Lourd | Léger |
| Perte de performance | Performance native |
| OS complet simulé | Partage de l'OS de l'hôte |
| Périphériques virtualisés | OS virtualisé
| Démarrage dans les minutes | Démarrage dans les millisecondes |
| Allocation complète de la RAM | Allocation dynamique de la RAM |
| Isolation complète | Isolation au niveau de l'OS |

# Conteneurs
## Types

* **Linux Containers (LXC)** : Système qui permet de virtualiser le noyau de Linux pour permettre de rouler
simultanément plusieurs systèmes Linux isolés sous un même hôte.

* **Docker** : Initialement une solution pour faire rouler une seule application avec LXC pour le rendre plus portable
et flexible. Maintenant c'est une solution complète de gestion de conteneurs.

# Conteneurs
## Docker

![Logo de Docker](./img/docker-logo.pdf){width=30%}

* Open source
* Support natif pour Linux et Windows (beta pour Mac)
* Norme de facto pour les applications Web

# Conteneurs
## Docker
### Concepts

* Logiciel (daemon)
    * Installé sur l'hôte
    * Gestionnaire des conteneurs
    * Roule en arrière plan
    * ```bash
$ docker -v
Docker version 19.03.4, build 9013bf583
```

# Conteneurs
## Docker
### Concepts

* Image
    * Application/binaire unique
    * Statique, tous changements à l'image durant l'exécution sont perdu
* Conteneur
    * **Instance** d'une image
* Registre
    * Répertoire d'images
    * Publique ou privé
    * Exemple : Docker Hub
