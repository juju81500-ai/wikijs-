---
title: "Fiche Simple - Debian 13 Nakivo Transporter Valider Mettre A Jour"
description: "Contrôler que le Transporter fonctionne correctement et appliquer ses mises à jour en suivant la documentation NAKIVO actuelle."
published: true
date: 2026-10-29T21:07:50Z
tags: ["debian-13", "nakivo", "transporter", "valider-mettre-a-jour"]
editor: markdown
dateCreated: 2026-10-29T21:07:50Z
dateModified: 2026-10-29T21:07:50Z
---

# Fiche_Simple_-_Debian_13_Nakivo_Transporter_Valider_Mettre_A_Jour

- **Environnement** : Debian 13 x64; NAKIVO Backup & Replication Transporter
- **OS / Version** : Debian 13 64-bit — explicitement listé dans les exigences de déploiement NAKIVO; valider le build produit
- **Catégorie** : sauvegarde / maintenance
- **Tags** : `debian-13`, `nakivo`, `transporter`, `valider-mettre-a-jour`

---

## Problème précis à résoudre

Contrôler que le Transporter fonctionne correctement et appliquer ses mises à jour en suivant la documentation NAKIVO actuelle.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l’état du nœud depuis la console NAKIVO et examiner les journaux si le statut n’est pas sain.
   👉 Explication : la console confirme l’état utile au Director; le nom local du service peut varier selon le build.

2. Exécuter un job pilote, puis restaurer un objet ou une machine de test dans une destination isolée.
   👉 Explication : le succès de sauvegarde seul ne prouve pas que le parcours de restauration est opérationnel.

3. Avant mise à jour, relever le build actuel, confirmer la compatibilité dans les notes de version et vérifier une sauvegarde/rétention valide.
   👉 Explication : les notes de version déterminent le chemin et l’ordre de mise à jour.

4. Appliquer la mise à jour du Transporter par une méthode explicitement décrite par NAKIVO pour la version déployée; ne pas lancer de commande générique sans vérifier ses options.
   👉 Explication : le mode d’update dépend du build et du type d’installation.

## 2. Production — Contrôles

Prévoir une fenêtre de changement, une sauvegarde de configuration, des règles réseau restreintes et un test de restauration avant l’usage en production.

## 3. Production — Sécurité

- Garder le système et le Transporter dans le périmètre de mises à jour approuvé.
- Ne pas exposer SSH ou l’interface NAKIVO sur Internet sans architecture de sécurité explicitement approuvée.
- Ne jamais copier de secrets ou de clés privées dans les fiches ou journaux partagés.

## Validation et retour arrière

- **Validation** : Debian 13 x64 est confirmé dans la matrice de déploiement NAKIVO; le nœud est sain, les jobs pilotes et une restauration de test réussissent.
- **Retour arrière** : suivre uniquement la procédure de désinstallation ou de retour arrière indiquée par NAKIVO pour le build; préserver les dépôts et données de sauvegarde.

## Si le problème n’est pas résolu

- [NAKIVO — Deployment Requirements](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/System-Requirements/Deployment-Requirements.htm)
- [NAKIVO — Installation on Linux](https://helpcenter.nakivo.com/User-Guide/Content/Deployment/Installing-NAKIVO-Backup-and-Replication/Installing-on-Linux/Installing-on-Linux.htm)
- [Fiche d’entrée NAKIVO / Altaro](/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro)