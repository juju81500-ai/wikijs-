---
title: "Stockage NetApp ONTAP et Dell EMC : solutions et interfaces"
description: "Ce guide distingue des solutions de constructeurs différents ; ne pas appliquer les commandes de l'une à l'autre."
published: true
date: 2026-11-03T09:36:14Z
tags: ["netapp", "ontap", "dell-emc", "powerstore", "powerscale", "nas", "san"]
editor: markdown
dateCreated: 2026-11-03T09:36:14Z
dateModified: 2026-11-03T09:36:14Z
---

# Stockage NetApp ONTAP et Dell EMC : solutions et interfaces

- **Environnement** : Baies de stockage d'entreprise, accès [[Glossary:NAS]]/SAN depuis serveurs Linux/Windows/hyperviseurs
- **Tags** : `netapp`, `ontap`, `dell-emc`, `powerstore`, `powerscale`, `nas`, `san`
- **Statut de validation** : **Verdict : Non testé sur plateforme cible.** Les procédures ci-dessous sont issues de la méthode documentaire et doivent être rejouées en laboratoire avant toute production.

## 1. Périmètre et prérequis

Ce guide distingue des solutions de constructeurs différents ; ne pas appliquer les commandes de l'une à l'autre.

| Famille | Interfaces d'administration | Usage |
|---|---|---|
| NetApp ONTAP | [[Glossary:CLI]] ([[Glossary:SSH]]), System Manager (web), [[Glossary:API]] REST | NAS ([[Glossary:NFS]]/SMB) et [[Glossary:SAN]] (iSCSI/FC/NVMe) unifiés ; SVM, agrégats, volumes, LIF |
| NetApp ONTAP Select / Cloud | mêmes interfaces ONTAP | Variantes logicielles, licences distinctes |
| Dell EMC PowerStore | PowerStore Manager (web), CLI, REST | Baie bloc/fichier |
| Dell EMC PowerScale (Isilon) | OneFS : WebUI, CLI, REST | NAS scale-out |
| Dell EMC Unity / autres gammes | Unisphere, CLI | Selon cycle de vie du produit ; vérifier son statut |

Prérequis : accès administrateur délégué, réseau de gestion séparé, plan de capacité, [[Glossary:DNS]]/NTP, sauvegarde et réplication pensées, support constructeur actif. Pas d'opérations destructives (suppression de volume/agrégat, reformatage) sans validation écrite et snapshot/sauvegarde.

## 2. Exigences de version et licence

- **Version du système (ONTAP, OneFS, PowerStoreOS, etc.) à figer avant déploiement**, d'après la matrice d'interopérabilité du constructeur (par exemple l'outil de matrice d'interopérabilité NetApp, le support Dell).
- Licences par fonction (protocoles, SnapMirror, snapshots avancés, etc.) selon contrat ; vérifier ce qui est inclus.
- Vérifier les dates de fin de support matériel/logiciel avant achat ou migration.

## 3. Procédure – NetApp ONTAP (lecture et provisionnement type)

1. Se connecter en SSH à l'interface de gestion du cluster, vérifier l'état :
```
cluster show
storage failover show
system health status show
network interface show
```
2. Identifier la SVM cible et les agrégats avec capacité suffisante : `vserver show`, `storage aggregate show`.
3. Créer un volume de test avec politique de snapshots (valider d'abord la syntaxe via `volume create ?` / documentation version) :
```
volume create -vserver svm1 -volume vol_test -aggregate aggr1 -size 10GB -junction-path /vol_test
```
4. Exporter via NFS (export-policy restrictive par client) ou créer un partage [[Glossary:CIFS]] ; pour iSCSI créer [[Glossary:LUN]], igroup et mapping.
5. Monter depuis un client de test et écrire un fichier.

## 4. Procédure – Dell EMC (PowerStore / PowerScale)

1. PowerStore : connexion à PowerStore Manager, contrôler alertes et santé du cluster, créer volume/hôte/mapping ou partage selon le mode bloc/fichier.
2. PowerScale : connexion WebUI ou SSH, vérifier `isi status`, créer zone d'accès, export NFS ou partage SMB, quotas et SnapshotIQ (si licencié).
3. Vérifier chaque commande dans la documentation de la version ; les syntaxes CLI changent entre versions.
4. Tester l'accès client et la restauration depuis snapshot.

## 5. Vérifications

- Santé matérielle et failover OK avant et après la modification.
- Client monte le volume, droits corrects (export restrictif, pas d'accès « tous »).
- Snapshot créé et restauration d'un fichier testée.

## 6. Rollback et risques

- Le snapshot n'est pas une sauvegarde : prévoir réplication hors baie ou sauvegarde externe.
- Suppression de volume : conserver la période de rétention (corbeille ou file d'attente de récupération si disponible) ; ne pas la purger pendant la fenêtre.
- Mises à jour de firmware/système : déroulées par l'outil constructeur, sans interrompre le failover, après contrôles préalables ; prévoir retour arrière uniquement selon la procédure officielle.
- Risque de montage simultané de LUN par plusieurs hôtes sans cluster : corruption.

## 7. Documentation officielle

- <https://docs.netapp.com/>
- <https://www.dell.com/support/home/>