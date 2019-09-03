---
wip: true
sigle: INF5190
title: Programmation Web avancée
session: Automne 2019
resp:
  nom: Beaudry
  prenom:  Éric
  local: PK-4635
  tel: poste 4005
  email: beaudry.eric@uqam.ca
  web: http://ericbeaudry.ca/
ens:
  nom: Caissy
  prenom: Jean-Philippe
  email: caissy.jean-philippe@uqam.ca
  web: https://caissy.dev/inf5190
---

# Description du cours

## Objectifs

Ce cours introduit aux méthodes avancées et aux bonnes pratiques de conception et de développement d'applications Web modernes.

## Sommaire du contenu

Infrastructure et cadre de développement Web ; intégration d'une base de données ; authentification ; conception de services web ; formats de sérialisation ; gestion d'erreurs ; interopérabilité ; déploiement de services ; tests de charge ; sécurité et patrons d'attaques spécifiques aux applications web.

## Modalité d'enseignement

Ce cours comporte une séance obligatoire de laboratoire (2 heures par semaine).

## Préalables académiques

* INF3080 - Bases de données
* INF3190 - Introduction à la programmation Web

# Contenu du cours

* Rappel et historique du développement web : évolution des protocoles (Gopher, HTTP, HTTP2), sites statiques, langages de script côtés client et côtés serveur, plugins de navigateurs (Flash, Java applets, Silverlight), Ajax, HTML5;
* Fonctionnement d'une application Web : requêtes HTTP, ressources, balanceurs de charge, Cookie/Local storages, stratégies d'optimisations (caches locales, caches de protocole HTTP, caches applicatives);
* Architecture d'une application web : MVC, middlewares, différents types de tests (unitaires, fonctionnels et d’intégrations, de navigateurs, bout en bout), websockets;
    * *Model* : Intégration d'une base de données : différents types de bases de données (NoSQL, relationnel, distribué, key-value store), ORM, modélisation du modèle, migrations;
    * *View* : Engins de templating HTML, formats de sérialisation (JSON, XML, Protocol Buffers), localisation (l10n) et internationalisation (i18n);
    * *Controller*: Gestion de contrôle : authentification (API, JWT, HTTP, authentification basée sur des certificats), validation de l'entrée et gestion d'erreurs;
* Maintenance d'une application web : gestion des logs d'erreurs, observabilité, métriques opérationnelles, métriques d’acceptabilité (SLA, SLO), modèle SRE (Site Reliability Engineer);
* Interopérabilité d'une application web et micro services : RPC (gRPC, HTTP), REST, découvertes de services;
* Résilience et performances d'une application web : tests de charge, requêtes n+1, pagination, disjoncteurs et contrôles de flux, tâches en arrière plan et récurrentes, réseau de diffusion de contenu (Content Delivery Network);
* Virtualisation et conteneurs : virtualisation et émulation de systèmes d'exploitations, isolation, quotas de ressources, conteneurs, orchestration (Kubernetes)
* Déploiement d'une application web : Platform as a Service (PaaS: Heroku, Google AppEngine), Infrastructure as a Service (IaaS: AWS, GCP), déploiement continu, déploiements progressifs et de canaries;

## Horaire

L'horaire présenté est à titre indicatif et peut changer tout au long de la session.

  | Semaine |  Date du cours | Cours                                                                      | Laboratoire                                                                                       |
  |---------|----------------|----------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
  | 1       | 4 septembre    | Présentation du cours, rappel au dévelopement web, introduction à Python | Introduction à Python, création d'une application web simple                                      |
  | 2       | 11 septembre   | (Suite) Introduction à Python, fonctionnement d'une application web          | Introduction au cadriciel de développement web Flask                                              |
  | 3       | 18 septembre   | Architecture d'une application web                                         | Création d'une application web avec Flask et intégration de tests                                 |
  | 4       | 25 septembre   | Modèle MVC : Controller                                                    | Système de templating, Sérialisation JSON                                                         |
  | 5       | 2 octobre      | (suite) Modèle MVC : Model                                                 | Intégration d'une base de données à une application Flask, systèmes de migration de base de données |
  | 6       | 9 octobre      | (suite) Modèle MVC : View                                                  | Formulaires, validation et gestion d'erreurs, localisation (i10n) et internationalisation (i18n) |
  | 7       | 16 octobre     | Révision                                                                   | Aide pour le projet de session                                                                    |
  | 8       | 23 octobre     | Examen intra                                                               |                                                                                                   |
  | 9       | 30 octobre     | Maintenance d'une application web, interopérabilité d'une application web    | Intégration de métriques d'observabilité, création d'une API REST                                |
  | 10      | 6 novembre     | (suite) Micro services, résilience d'une application web                     | Création et utilisation d'un service externe, pagination de l'API REST                            |
  | 11      | 13 novembre    | Performance d'une application web                                          | Systèmes de caching, intégration de tâches en arrière plan (background jobs)                      |
  | 12      | 20 novembre    | Virtualisation et conteneurs                                               | Création d'une image docker de l'application web                                                  |
  | 13      | 27 novembre    | Déploiement d'une application web                                          | Déploiement de l'application web sur Google Cloud Platform                                        |
  | 14      | 4 décembre     | Révision                                                                   | Aide pour le projet de session                                                                    |
  | 15      | 11 décembre    | Examen final                                                               |                                                                                                   |

## Projet de session

Le projet de session consiste à développer et déployer une application web complète. Cette application sera développée avec le langage de programmation Python et le cadriciel de développement Flask.

# Modalités d'évaluation

  Description sommaire  |Date      |Pondération
  ----------------------|----------|----------:
  Examen intra          | 23 octobre 2019 |35%
  Examen final          |11 décembre 2019 |35%
  Projet de session     |13 décembre 21h |30%

Un projet de session remis en retard reçoit la note zéro à moins d'avoir fait l'objet d'une entente préalable avec le professeur.

Le détail des conditions de réalisation du travail de session est précisé avec la description de celui-ci.

La qualité du français fait partie intégrante des critères d'évaluation des travaux et des examens jusqu'à un maximum de 25%.

La note de passage du cours est de 60% pour l'ensemble de l'évaluation et de 50% pour les deux examens combinés.

Le projet projet de session peut se faire individuellement ou en équipe de deux.

# Médiagrahie

* Matt Makai. Full Stack Python Supporter's Edition. [Disponible gratuitement](https://www.fullstackpython.com/table-of-contents.html)
* Betsy Beyer, Chris Jones, Jennifer Petoff et Niall Richard Murphy. Site Reliability Engineering: How Google Runs Production Systems. O'Reilly Media (2016). [Disponible gratuitement](https://landing.google.com/sre/books/)
* Michael T. Nygard. Release It!: Design and Deploy Production-Ready Software. Pragmatic Bookshelf (2007)
