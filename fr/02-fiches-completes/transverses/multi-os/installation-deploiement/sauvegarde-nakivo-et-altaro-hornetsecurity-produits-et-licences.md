---
title: "Sauvegarde Nakivo et Altaro / Hornetsecurity : produits et licences"
description: "Deux éditeurs, deux produits : ne pas mélanger."
published: true
date: 2026-11-03T09:36:14Z
tags: ["nakivo", "altaro", "hornetsecurity", "sauvegarde", "vmware", "hyperv"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Sauvegarde Nakivo et Altaro / Hornetsecurity : produits et licences

- **Environnement** : Sauvegarde de machines virtuelles et de charges de travail ; produits distincts de deux éditeurs
- **Tags** : `nakivo`, `altaro`, `hornetsecurity`, `sauvegarde`, `vmware`, `hyperv`
- **Statut de validation** : **Verdict : Non testé sur plateforme cible.** Les procédures ci-dessous sont issues de la méthode documentaire et doivent être rejouées en laboratoire avant toute production.

## 1. Périmètre et prérequis

Deux éditeurs, deux produits : ne pas mélanger.
- **Nakivo Backup & Replication** : sauvegarde/réplication de [[Glossary:VM]] (VMware vSphere, Hyper-V, Nutanix [[Glossary:AHV]], etc.), machines physiques, cloud ; déploiement sur Windows, Linux, appliance ou [[Glossary:NAS]] ; transporteurs, dépôts.
- **Altaro VM Backup**, aujourd'hui commercialisé sous l'éditeur Hornetsecurity (gamme « VM Backup » ; Altaro est l'ancien nom) : sauvegarde Hyper-V et VMware. Gamme complémentaire « 365 Total Backup » pour Microsoft 365 : produit différent, licence par utilisateur.
Prérequis : dépôt de sauvegarde sur stockage distinct de la production, règle 3-2-1, compte de service à droits minimaux, connectivité hyperviseur, synchronisation horaire, politique de rétention, chiffrement des sauvegardes avec séquestre de clé.

## 2. Exigences de version et licence

- **Version à figer avant déploiement** et à valider contre la compatibilité hyperviseur dans la documentation de l'éditeur.
- Nakivo : licences par socket/CPU, par charge de travail ou par édition ; vérifier les conditions (éditions, essai, fonctions).
- Hornetsecurity VM Backup : édition (Standard/Unlimited Plus selon offre actuelle), licence par hôte ; ne pas confondre avec 365 Total Backup (par utilisateur). Les offres évoluent : confirmer avec l'éditeur.

## 3. Procédure – Nakivo

1. Télécharger l'installateur depuis le site officiel, vérifier l'empreinte si fournie.
2. Installer le Director et le Transporter selon la plateforme choisie, ouvrir uniquement les ports documentés.
3. Ajouter l'inventaire (vCenter/hôte Hyper-V), créer un dépôt de sauvegarde.
4. Créer une tâche de sauvegarde d'une VM de test : planification, rétention, chiffrement, vérification de la sauvegarde.
5. Exécuter la tâche et restaurer vers un nouvel emplacement.

## 4. Procédure – Altaro / Hornetsecurity VM Backup

1. Installer la console et le service sur un hôte Windows prévu, depuis le site officiel.
2. Ajouter l'hôte Hyper-V ou VMware (compte dédié), choisir un emplacement de sauvegarde.
3. Créer un plan de sauvegarde et un planning ; activer la déduplication/compression selon l'édition.
4. Lancer la sauvegarde d'une VM de test et exécuter un test de restauration (restauration complète et fichier).
5. Pour Microsoft 365, utiliser la procédure du produit 365 Total Backup séparément.

## 5. Vérifications

- Tâche terminée sans avertissement ; sauvegarde cohérente applicativement ([[Glossary:VSS]] pour Windows).
- Restauration vers un site de test réussie et vérifiée.
- Alertes email/supervision actives.

## 6. Rollback et risques

- Désinstallation du produit : conserver les sauvegardes et clés de chiffrement avant tout retrait.
- Perte de clé de chiffrement = sauvegardes inutilisables.
- Dépôt sur le même stockage que la production : pas de protection en cas de sinistre.
- Les restaurations sur le même emplacement peuvent écraser la VM : utiliser un autre nom/réseau isolé en test.

## 7. Documentation officielle

- <https://helpcenter.nakivo.com/>
- <https://www.hornetsecurity.com/>
- <https://docs.hornetsecurity.com/>