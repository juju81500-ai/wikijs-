---
title: "Scanner des vulnérabilités avec Nessus ou OpenVAS (périmètre autorisé et laboratoire)"
description: "Installer et utiliser un scanner uniquement sur des cibles dont vous avez l'autorisation écrite. Cette fiche couvre la préparation, la création d'une politique de scan non destructive, la lecture des résultats et la remédiation. Aucun exploit ni cible tierce."
published: true
date: 2026-11-03T09:36:14Z
tags: ["nessus", "tenable", "openvas", "greenbone", "gvm", "vulnerabilites", "audit"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Scanner des vulnérabilités avec Nessus ou OpenVAS (périmètre autorisé et laboratoire)

- **OS / Version** : Linux (Nessus sous Linux/Windows/macOS; OpenVAS/Greenbone sous Linux)
- **Type de fiche** : Installation/Déploiement
- **Environnement** : Laboratoire isolé ou périmètre signé
- **Machine ciblée** : Scanner de vulnérabilités
- **Catégorie** : Audit / gestion des vulnérabilités
- **Tags** : `nessus`, `tenable`, `openvas`, `greenbone`, `gvm`, `vulnerabilites`, `audit`

## 1. Périmètre

Installer et utiliser un scanner uniquement sur des cibles dont vous avez l'autorisation écrite. Cette fiche couvre la préparation, la création d'une politique de scan non destructive, la lecture des résultats et la remédiation. Aucun exploit ni cible tierce.

## 2. Prérequis

- Autorisation écrite précisant cibles, plages IP, dates, horaires et contact d'urgence.
- Segment ou VM d'administration isolé pour le scanner.
- Licence Nessus (Essentials, Professional ou Expert selon besoin) obtenue sur le site éditeur, ou installation de Greenbone Community Edition.
- Comptes de scan authentifié à moindre privilège (lecture), stockés dans un coffre.
- Sauvegardes et fenêtre de maintenance pour les systèmes fragiles (équipements industriels, imprimantes, appliances).
- Nessus est commercial : la console, les droits d'accès au portail éditeur et la licence sont des prérequis. Aucune commande générique n'est donnée quand elle dépend de la console ou de la version; suivre la documentation de la version exacte.

## 3. Variantes éditeur à distinguer

| Produit | Édition | Installation | Gestion |
|---|---|---|---|
| Tenable Nessus | Commerciale (version gratuite limitée) | Paquet depuis le portail Tenable | Interface web sur le port 8834 par défaut |
| OpenVAS / Greenbone | Greenbone Community Edition (libre) et offres commerciales | Conteneurs ou paquets selon la documentation Greenbone, évolutifs entre versions | Greenbone Security Assistant (web) |

Les deux outils diffèrent par la gestion des flux de signatures, la licence et l'interface.

## 4. Étapes vérifiables

### 4.1 Préparer l'hôte

Installer sur un hôte durci et à jour, avec NTP et espace disque suffisant, sans l'exposer à Internet. Limiter l'accès à l'interface web à un réseau d'administration.

### 4.2 Installer

Nessus : télécharger le paquet adapté à l'OS depuis le site Tenable, vérifier l'empreinte publiée, installer, activer le service puis finaliser l'assistant web avec le code d'activation. Greenbone : suivre le guide officiel de la Community Edition de la version choisie et patienter jusqu'à la synchronisation initiale des flux.

### 4.3 Créer la politique

Choisir un modèle de découverte ou d'évaluation de vulnérabilités, désactiver les contrôles dangereux ou de déni de service, régler la concurrence pour ne pas saturer les cibles.

### 4.4 Déclarer les cibles et identifiants

Saisir uniquement les plages autorisées. Utiliser un compte de scan authentifié dédié lorsque possible, car il réduit les faux positifs.

### 4.5 Lancer d'abord sur un échantillon

Exécuter un scan sur un petit groupe de machines de test, vérifier l'impact, puis étendre dans la fenêtre convenue.

### 4.6 Exploiter

Trier par risque réel (exposition, criticité du bien), créer des tickets de remédiation, rescanner pour confirmer et archiver le rapport de façon protégée.

## 5. Validation

- Le scanner est à jour (plugins/flux) et accessible uniquement depuis l'administration.
- Le scan d'échantillon se termine sans incident sur les cibles.
- Le rapport ne contient que des hôtes du périmètre autorisé.
- Un rescan confirme la fermeture d'une vulnérabilité corrigée.

## 6. Retour arrière

- Arrêter le scan en cours depuis l'interface.
- Désactiver le compte de scan et révoquer ses accès.
- Supprimer ou chiffrer les rapports si la mission est terminée ; désinstaller ou restaurer l'instantané de la VM du scanner.

## 7. Limites de version et de licence

- Les modèles, ports et noms de services varient selon version; consulter la documentation exacte.
- Les limites de licence (nombre d'IP, fonctions) dépendent de l'édition Nessus.
- Un scan peut perturber des systèmes fragiles : toujours prévoir un plan de contact.
- Ne jamais scanner des systèmes tiers ou Internet sans autorisation.

## 8. Verdict historique

**Non testé sur plateforme cible.** Cette fiche est une synthèse documentaire des sources officielles; aucune exécution n'a été réalisée sur les produits, versions ou licences visés. Valider en laboratoire isolé avant production.

## Sources

- [Tenable — documentation Nessus](https://docs.tenable.com/nessus/Content/GettingStarted.htm)
- [Greenbone — documentation](https://greenbone.github.io/docs/latest/)
- [ANSSI — recommandations de sécurité](https://cyber.gouv.fr/)