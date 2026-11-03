---
title: "EVE-NG : éditions Community, Freemium et Pro, licences et statut"
description: "- Périmètre : plateforme de laboratoire réseau multi-éditeurs, installation en VM, accès web, import d'images et premier laboratoire. Usage : formation et validation ; ne pas l'utiliser comme environnement de production."
published: true
date: 2026-11-03T09:36:14Z
tags: ["eve-ng", "laboratoire", "reseau", "emulation", "licence"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# EVE-NG : éditions Community, Freemium et Pro, licences et statut

- **Environnement** : VM ou serveur d'émulation réseau de laboratoire (hors production)
- **Tags** : `eve-ng`, `laboratoire`, `reseau`, `emulation`, `licence`
- **Statut de validation** : **Verdict : Non testé sur plateforme cible.** Les procédures ci-dessous sont issues de la méthode documentaire et doivent être rejouées en laboratoire avant toute production.

## 1. Périmètre et prérequis

- Périmètre : plateforme de laboratoire réseau multi-éditeurs, installation en VM, accès web, import d'images et premier laboratoire. Usage : formation et validation ; ne pas l'utiliser comme environnement de production.
- Matériel : virtualisation imbriquée activée sur l'hôte, CPU avec extensions de virtualisation, RAM et disque adaptés au nombre de nœuds, réseau d'accès.
- Images éditeur (routeurs, pare-feu) : le droit de les utiliser dépend des licences des éditeurs ; l'outil ne fournit pas ces images.

## 2. Exigences de version et licence – restrictions et statut

| Édition | Points à vérifier |
|---|---|
| Community | Gratuite ; fonctions limitées. **Statut/EOL : à vérifier prudemment.** La matrice du dépôt signale une version Community marquée en fin de vie (juin 2026) ; ne pas déployer de nouvelle installation Community sans confirmer le statut sur le site officiel. |
| Freemium | Édition actuelle gratuite avec limites (par exemple nombre de nœuds, fonctions) ; vérifier les limites en vigueur. |
| Pro | Licence payante, abonnement, fonctions avancées (multi-utilisateurs, nombre de nœuds supérieur, Docker, etc.) ; vérifier le périmètre exact avant achat. |

- **Version à figer avant déploiement** après lecture de la page de téléchargement officielle et des notes de version ; consigner la date de vérification du statut/EOL.
- Respecter les conditions de licence : une licence Pro est nominative ; ne pas la partager ni contourner les limites.

## 3. Procédure

1. Télécharger l'OVA/ISO depuis le site officiel uniquement ; vérifier la somme de contrôle si publiée.
2. Importer dans l'hyperviseur de laboratoire, activer la virtualisation imbriquée sur la VM, configurer CPU/RAM/disque et un réseau accessible.
3. Démarrer, suivre l'assistant de première configuration (mot de passe root, nom d'hôte, DNS, NTP, mode IP).
4. Accéder à l'interface web par HTTPS (restreindre l'accès au poste d'administration) et changer les mots de passe par défaut.
5. Vérifier le prérequis de virtualisation :
```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
```
6. Importer uniquement des images dont la licence est acquise, dans l'arborescence documentée, puis corriger les permissions avec l'outil de l'éditeur.
7. Créer un laboratoire minimal (deux nœuds liés) et tester la connectivité.
8. Pour Pro : appliquer la licence selon la documentation et contrôler le périmètre affiché.

## 4. Vérifications

- Interface web accessible ; version affichée conforme à la version figée.
- Nœuds démarrent et communiquent ; consommation CPU/RAM maîtrisée.
- Aucun accès exposé sur Internet.

## 5. Rollback et risques

- Faire un instantané de la VM avant toute mise à jour ; les mises à jour majeures peuvent casser des laboratoires : exporter les labs avant.
- Version Community en fin de vie : plus de correctifs de sécurité ; isoler du réseau de production.
- Risque de non-conformité de licence avec les images éditeur ou l'édition Pro partagée.
- Restauration : retour à l'instantané et réimport des labs exportés.

## 6. Documentation officielle

- <https://www.eve-ng.net/>
- <https://www.eve-ng.net/index.php/documentation/>