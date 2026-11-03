---
title: "StarWind Virtual SAN : stockage répliqué sur deux nœuds"
description: "- Périmètre : stockage haute disponibilité à deux nœuds (réplication synchrone) pour hyperviseurs. Ne couvre pas la plateforme complète HCI propriétaire ni les appliances livrées clé en main."
published: true
date: 2026-11-03T09:36:14Z
tags: ["starwind", "vsan", "stockage", "ha", "iscsi", "hyperv"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# StarWind Virtual SAN : stockage répliqué sur deux nœuds

- **Environnement** : Windows Server ou Linux, selon variante StarWind VSAN, hôtes d'hyperviseur
- **Tags** : `starwind`, `vsan`, `stockage`, `ha`, `iscsi`, `hyperv`
- **Statut de validation** : **Verdict : Non testé sur plateforme cible.** Les procédures ci-dessous sont issues de la méthode documentaire et doivent être rejouées en laboratoire avant toute production.

## 1. Périmètre et prérequis

- Périmètre : stockage haute disponibilité à deux nœuds (réplication synchrone) pour hyperviseurs. Ne couvre pas la plateforme complète HCI propriétaire ni les appliances livrées clé en main.
- Matériel : deux serveurs équivalents, disques ou RAID dédiés, réseau de synchronisation dédié et réseau iSCSI séparé du réseau de gestion ; liaisons redondantes.
- Quorum : avec deux nœuds, prévoir un témoin (heartbeat via le réseau de gestion ou nœud témoin) pour éviter le split-brain, selon les recommandations de la documentation éditeur.
- Sauvegarde : sauvegarde externe complète avant mise en production ; la réplication ne remplace pas la sauvegarde.
- Fenêtre : l'initialisation de la synchro complète peut saturer le réseau et dégrader les performances.

## 2. Exigences de version et licence

- **Version à figer avant déploiement** (build de l'agent, version hyperviseur et OS hôte) d'après la matrice de compatibilité éditeur.
- La licence (gratuite limitée, commerciale ou appliance) dépend de l'édition, du nombre de nœuds et de la capacité ; vérifier les conditions et restrictions d'usage sur le site de l'éditeur. Conserver la preuve de licence.

## 3. Procédure

1. Valider la compatibilité OS/hyperviseur et la configuration réseau (MTU identique, pas de NAT, ports iSCSI ouverts seulement entre nœuds et hôtes).
2. Installer le logiciel sur les deux nœuds depuis le programme téléchargé via le compte éditeur ; vérifier hash/signature si fournis.
3. Créer les volumes de stockage locaux, les cibles et les périphériques répliqués selon l'assistant de la console de gestion.
4. Configurer les chemins de synchronisation et de heartbeat ; lancer la synchronisation initiale.
5. Côté hyperviseur (ex. initiateur iSCSI) : connecter les deux cibles avec multipath (MPIO) ; ne pas monter le même volume sur plusieurs hôtes sans système de fichiers cluster (CSV, VMFS, etc.).
6. Provoquer, en laboratoire seulement, la panne d'un nœud et contrôler la continuité d'accès, puis la resynchronisation.

## 4. Vérifications

- État « Synchronized » sur tous les périphériques ; latence de synchro stable.
- Chemins MPIO actifs sur les deux nœuds.
- Alertes de la console traitées ; test de restauration d'une VM depuis sauvegarde.

## 5. Rollback et risques

- Split-brain : si les deux nœuds acceptent des écritures isolées, la reprise peut entraîner une perte de données ; suivre uniquement la procédure éditeur et choisir le nœud de référence après analyse.
- Ne jamais arrêter/redémarrer les deux nœuds en même temps ; patcher un nœud à la fois en attendant la resynchro complète.
- Retour arrière : migrer les VM vers un autre stockage avant de supprimer les périphériques ; conserver la sauvegarde externe.

## 6. Documentation officielle

- <https://www.starwindsoftware.com/>
- <https://www.starwindsoftware.com/resource-library>