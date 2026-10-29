---
title: "Déployer Proxmox Backup Server 3.x"
description: "Fiche simple : [préparer l'infrastructure PBS](../../../../01-Fiches-Simples/Proxmox/Toutes-versions/Vie-du-logiciel/Proxmox-Backup-Server/FicheSimple-HoteProxmoxBackupServerPreparerInfrastructure.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["proxmox-backup-server", "pbs3", "proxmox", "sauvegarde", "restauration"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Déployer Proxmox Backup Server 3.x

- **Environnement** : Serveur de sauvegarde dédié, séparé du cluster protégé
- **Tags** : `proxmox-backup-server`, `pbs3`, `proxmox`, `sauvegarde`, `restauration`

## 1. Préparer l'infrastructure

Fiche simple : [préparer l'infrastructure PBS](/01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-preparer-infrastructure).

Dimensionner le stockage à partir des données, de la rétention, du taux de changement et de la fenêtre de sauvegarde. Séparer datastore et système si possible, protéger le serveur et le réseau d'administration, et prévoir une copie hors site ou hors ligne. La déduplication n'est ni une réplication ni une sauvegarde indépendante.

Vérifier compatibilité des versions PVE/PBS, DNS, NTP, certificats et accès. Les références `3.x` sont historiques : appliquer une version encore supportée et les notes de mise à jour actuelles.

## 2. Installer et créer le datastore

Fiche simple : [installer PBS et créer le datastore](/01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-installer-datastore).

Installer PBS depuis le média ou le dépôt officiel, puis configurer le stockage dans l'interface d'administration. Créer un datastore sur un système de fichiers pris en charge, avec capacité, alertes et politique de nettoyage vérifiées. Ne pas modifier le stockage actif avec des commandes génériques de formatage ou de montage.

Créer des utilisateurs et API tokens dédiés avec les permissions minimales sur les namespaces/datastores requis. Protéger les secrets et les clés de chiffrement des sauvegardes côté client.

## 3. Relier Proxmox VE à PBS

Fiche simple : [relier Proxmox VE à PBS](/01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-relier-pve-pbs).

Dans PVE, ajouter PBS via le stockage de sauvegarde, vérifier le certificat/empreinte depuis un canal fiable, sélectionner le datastore et utiliser un compte ou token dédié. Choisir chiffrement côté client lorsque la stratégie de confidentialité l'exige et sauvegarder séparément la clé de déchiffrement.

Configurer une tâche sur un petit groupe de VM/CT et vérifier le résultat, la rétention, la vérification d'intégrité et les alertes avant généralisation.

## 4. Tester la restauration

Fiche simple : [tester la restauration](/01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-tester-restauration).

Restaurer régulièrement une VM/CT vers un réseau isolé, vérifier le démarrage, l'application, les permissions et la cohérence métier. Une tâche verte n'est pas une preuve de restaurabilité.

```text
Test d'acceptation : sélectionner un point de sauvegarde, restaurer vers un identifiant temporaire et un réseau isolé, démarrer et documenter le résultat.
```

## 5. Exploitation et incident

Fiche simple : [exploitation et incident](/01-fiches-simples/proxmox/toutes-versions/vie-du-logiciel/proxmox-backup-server/fiche-simple-hote-proxmox-backup-server-exploitation-incident).

Surveiller l'espace, la durée, l'échec des jobs et la vérification des chunks. Mettre à jour PVE et PBS selon la matrice officielle. Protéger l'accès administratif avec MFA, réseau dédié et audit. En perte de PBS, préserver les disques et les clés ; ne pas réinitialiser ou recréer un datastore avant analyse.