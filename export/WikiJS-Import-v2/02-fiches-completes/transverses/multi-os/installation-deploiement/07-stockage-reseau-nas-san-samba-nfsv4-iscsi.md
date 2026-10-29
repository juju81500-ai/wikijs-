---
title: "Services de stockage : Samba, NFSv4 et cible iSCSI"
description: "Fiche simple : [concevoir avant d'installer](../../../../01-Fiches-Simples/Transverses/Multi-OS/Stockage-Reseau/FicheSimple-HoteMultiOSStockageReseauConcevoir.md)."
published: true
date: 2026-10-29T19:41:12Z
tags: ["stockage", "samba", "nfs4", "iscsi", "debian", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T19:41:12Z
dateModified: 2026-10-29T19:41:12Z
---

# Services de stockage : Samba, NFSv4 et cible iSCSI

- **Environnement** : Serveur de stockage Linux dédié
- **Choix d'architecture** : Samba pour clients SMB, NFSv4 pour clients Unix, iSCSI pour présenter des blocs à un initiateur unique ou à un cluster conçu pour le multi-accès
- **Tags** : `stockage`, `samba`, `nfs4`, `iscsi`, `debian`, `sauvegarde`

## 1. Concevoir avant d'installer

Fiche simple : [concevoir avant d'installer](/01-fiches-simples/transverses/multi-os/stockage-reseau/fiche-simple-hote-multi-os-stockage-reseau-concevoir).

Définir les clients, les droits, le plan d'adressage, le protocole, la capacité, les snapshots, la sauvegarde et le scénario de restauration. Ne pas présenter simultanément un même système de fichiers en NFS/SMB et en LUN iSCSI sans conception explicite : un montage concurrent non compatible peut corrompre les données.

Créer des volumes et points de montage dédiés, avec supervision de l'espace et protection contre la saturation. Chiffrer les flux sur les réseaux non fiables.

## 2. Déployer Samba

Fiche simple : [déployer Samba](/01-fiches-simples/transverses/multi-os/stockage-reseau/fiche-simple-hote-multi-os-stockage-reseau-samba).

Installer `samba`, créer un groupe d'accès et un répertoire dont les permissions correspondent au modèle d'identité retenu. Configurer un partage nommé, limité aux groupes nécessaires, dans `/etc/samba/smb.conf`. Ne pas utiliser `guest ok = yes` sur un réseau de production.

```bash
sudo testparm -s
sudo systemctl enable --now smbd
sudo systemctl --no-pager status smbd
```

Ouvrir TCP/445 uniquement aux sous-réseaux clients prévus. Vérifier depuis un client avec un compte non administrateur.

## 3. Déployer NFSv4

Fiche simple : [déployer NFSv4](/01-fiches-simples/transverses/multi-os/stockage-reseau/fiche-simple-hote-multi-os-stockage-reseau-nfsv4).

Installer le serveur NFS, exporter un chemin dédié dans `/etc/exports` avec les clients ou réseaux explicitement autorisés et les options adaptées au modèle d'identité. Éviter `no_root_squash` sauf exigence documentée et contrôlée.

```bash
sudo exportfs -rav
sudo exportfs -v
sudo systemctl enable --now nfs-server
```

N'autoriser que les clients attendus et les flux nécessaires à la version NFS choisie. Valider le montage et les UID/GID depuis un client représentatif.

## 4. Présenter une cible iSCSI

Fiche simple : [présenter une cible iSCSI](/01-fiches-simples/transverses/multi-os/stockage-reseau/fiche-simple-hote-multi-os-stockage-reseau-iscsi).

Réserver une adresse sur un réseau de stockage isolé, configurer l'initiateur IQN autorisé, le LUN et les ACL de la cible. Utiliser l'outil maintenu par la distribution (par exemple `targetcli` avec LIO) et vérifier chaque identifiant avant d'exporter le volume.

Une LUN brute doit avoir un initiateur propriétaire clair. Pour le multi-accès, utiliser un système de fichiers en cluster et un mécanisme de réservation compatibles ; ne pas monter le même système de fichiers classique en écriture depuis plusieurs hôtes.

## 5. Vérifier et protéger

Fiche simple : [vérifier et protéger](/01-fiches-simples/transverses/multi-os/stockage-reseau/fiche-simple-hote-multi-os-stockage-reseau-verifier).

- Tester lecture/écriture et refus d'accès depuis un client non autorisé.
- Surveiller latence, erreurs disque, capacité, permissions et disponibilité.
- Sauvegarder les données indépendamment du serveur et tester la restauration.
- Toute modification d'export ou de LUN doit être planifiée : les clients peuvent perdre des écritures ou bloquer.