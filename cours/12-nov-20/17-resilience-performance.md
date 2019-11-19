% INF5190 - Résilience et performance
% Jean-Philippe Caissy
% 20 novembre 2019

---
header-includes:
 - \usepackage{fvextra}
 - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
---

# Résilience

Définition : capacité d'un système à récupérer d'une défaillance et rester opérationnel

* Une défaillance dans un système (application Web) va se produire éventuellement
* Plus un système est complexe, plus les risques de défaillances sont élevées
    * Une application avec 3-4 systèmes peut facilement être disponible 100% du temps
        vs. une application avec des centaines de composantes 
* Un système est résilient s'il reste fonctionnel malgré une défaillance

# Résilience

Lors d'une défaillance, un système devrait être en mesure d'opérer en mode *défaillance partiel*.

Exemples :

* Amazon : la recherche ne fonctionne plus
* Netflix : les vidéos HD ne chargent plus
* Google : impossible de se connecter

# Résilience

La résilience d'une application Web se fait sur 4 niveaux différents :

* L'application elle-même
* Les données
* Le réseau
* Les gens et la culture organisationnelle

# Résilience
## Patrons

Il existe plusieurs patrons à utiliser pour rendre une application résiliente.

## Redondance

* Architecturer une application pour pouvoir rouler de manière redondante (plus d'une instance)
* La redondance s'applique à tous les niveaux :
    * Application Web
    * Base de donnée
    * Réseau
    * Employés
* La redondance permet d'éliminer les défaillances causés par un point de défaillance unique (*SPOF, ou single point of failure*) 

# Résilience
## Redondance

![Composantes en série](./img/composantes-series.pdf){width=50%}

La disponibilité d'un système en série est mesuré par la sommes de la disponibilité des deux systèmes.

| Composante    | Disponibilité   | Temps indisponible                |
|---------------|-----------------|-----------------------------------|
| A             | 99%             | 3 jours, 15 heures                |
| B             | 99.99%          | 52 minutes                        |
| A et B        | 98.99%          | 3 jours, 16 heures et 33 minutes  |

# Résilience
## Redondance

![Composantes en parallèles](./img/composantes-par.pdf){width=40%}

$$ D = 1 - (1 - Ax)^n $$

| Composante    | Disponibilité   | Temps indisponible                |
|---------------|-----------------|-----------------------------------|
| Un seul A     | 99%             | 3 jours, 15 heures                |
| Deux A en parallèle | 99.99%          | 52 minutes                        |
| Trois A en parallèle | 99.9999%          | 31 secondes |

# Résilience
## Mise à l'échelle automatique (*auto-scaling*)

* Automatiquement augmenter, puis diminuer les capacités d'un système
    * Mot clé : automatique, et non pas manuellement

Exemple : Diminuer le nombre de serveur applicatifs la nuit lorsque le trafique est très bas
