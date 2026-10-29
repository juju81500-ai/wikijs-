---
title: "TrueNAS Core"
description: "Mettre en service un NAS TrueNAS CORE, créer un pool ZFS et un jeu de données partagé, vérifier l'état du pool et les instantanés, puis durcir l'accès d'administration. Les tests ne se font que sur votre propre appliance. Les commandes s'exécutent dans le shell de l'interface (System > Shell), en ro"
published: true
date: 2026-10-29T12:24:36Z
tags: ["[truenas-core]", "[freebsd]", "[zfs]", "[nas]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T12:24:36Z
dateModified: 2026-10-29T12:24:36Z
---

# 📄 TrueNAS Core

- **Environnement** : Appliance dédiée (matériel ou VM réservée au NAS)
- **OS / Version** : TrueNAS CORE 13.0 (appliance basée sur FreeBSD 13, hors Debian 12 et Rocky Linux 9 par nature)
- **Version** : TrueNAS CORE 13.0-U6 ou supérieure, à vérifier dans `System > Update`
- **Catégorie** : Stockage et SAN / NAS
- **Tags** : `[truenas-core]`, `[freebsd]`, `[zfs]`, `[nas]`, `[hardening]`

## 🎯 Problème précis à résoudre
Mettre en service un NAS TrueNAS CORE, créer un pool ZFS et un jeu de données partagé, vérifier l'état du pool et les instantanés, puis durcir l'accès d'administration. Les tests ne se font que sur votre propre appliance. Les commandes s'exécutent dans le shell de l'interface (`System > Shell`), en root.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérification de la version du système :
```bash
uname -a
midclt call system.version
```
👉 Explication : `uname -a` affiche le noyau FreeBSD. `midclt call system.version` affiche la version TrueNAS. Point à vérifier : la commande `midclt` est disponible sur CORE 13.0, mais sa sortie varie selon la version.

2. Création du pool de test dans l'interface :
```bash
zpool status -v
zfs list -o name,used,avail,mountpoint
```
👉 Explication : Le pool est créé dans `Storage > Create Pool` avec le nom `tank` (disques de lab). `zpool status` doit afficher l'état `ONLINE` pour chaque disque. `zfs list` indique le point de montage, normalement `/mnt/tank`.

3. Création d'un jeu de données et du partage :
```bash
zfs create tank/partage-test
zfs list -o name,mountpoint -r tank
ls -ld /mnt/tank/partage-test
```
👉 Explication : Crée le jeu de données `partage-test`. Le partage SMB se configure ensuite dans `Sharing > Windows Shares (SMB)` en pointant sur `/mnt/tank/partage-test`.

4. Instantané de test et accès à sa copie :
```bash
zfs snapshot tank/partage-test@test-1
zfs list -t snapshot -r tank/partage-test
ls /mnt/tank/partage-test/.zfs/snapshot/
```
👉 Explication : Crée un instantané, copie figée et en lecture seule du jeu de données. Le dossier caché `.zfs/snapshot/` permet de retrouver les fichiers de l'instantané sans restauration complète.

5. Vérification d'intégrité par scrub :
```bash
zpool scrub tank
zpool status tank
```
👉 Explication : Lance une lecture complète du pool qui vérifie les sommes de contrôle ZFS. `zpool status` affiche l'avancement (`scrub in progress`) puis le résultat, sans erreur attendue.

---

## ⚡ 2. Production — Façon Simplifiée
1. Contrôle de santé du pool :
```bash
zpool status -x
zpool list tank
```
👉 Explication : `zpool status -x` affiche `all pools are healthy` si aucun problème n'est détecté. `zpool list` indique la capacité et la fragmentation.

2. Tâches planifiées dans l'interface :
```bash
zfs list -t snapshot -o name,creation -r tank/partage-test | tail -n 5
```
👉 Explication : Les instantanés périodiques, les scrubs et la réplication se configurent dans `Data Protection`. La commande vérifie que les derniers instantanés planifiés ont bien été créés.

3. Surveillance SMART des disques :
```bash
camcontrol devlist
smartctl -H /dev/ada0
```
👉 Explication : `camcontrol devlist` liste les disques détectés et leur nom (`ada0`, `da0`...). `smartctl -H` donne l'état de santé du disque indiqué. Répéter pour chaque disque. Point à vérifier : les seuils d'alerte sont à régler dans `System > Alert Settings`.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Contrôle des services exposés :
```bash
sockstat -4 -l
service sshd status
```
👉 Explication : `sockstat -4 -l` liste les ports IPv4 en écoute. Seuls l'interface web (80 et 443), SSH (22), SMB (445) et NFS (2049) selon les services activés doivent apparaître. Point à vérifier : ne pas modifier `/etc/ssh/sshd_config` à la main, TrueNAS l'écrase ; passer par `System > Services`.

2. Propriétés ZFS du jeu de données :
```bash
zfs get -r compression,atime,readonly,sync tank/partage-test
```
👉 Explication : Affiche les propriétés utiles à la sécurité et à l'intégrité : `readonly` doit être à `off` pour un partage en écriture, `sync` à `standard` pour garantir l'écriture sur disque.

3. Droits d'accès au partage :
```bash
ls -ld /mnt/tank/partage-test
getfacl /mnt/tank/partage-test
```
👉 Explication : Vérifie le propriétaire et les ACL NFSv4 du dossier. Les droits se modifient dans `Storage > Dataset > Edit Permissions` plutôt qu'en ligne de commande.

4. Sauvegarde de la configuration :
```bash
ls -l /data/freenas-v1.db
```
👉 Explication : Contrôle la présence de la base de configuration. Point à vérifier : l'export se fait dans `System > General Settings > Save Config`. Le fichier exporté contient les mots de passe et clés : le stocker hors du NAS, dans un coffre-fort (voir la fiche Passbolt ou Vaultwarden du pack).

5. Contrôle du journal système :
```bash
tail -n 50 /var/log/messages
```
👉 Explication : Affiche les 50 dernières lignes du journal. Les erreurs disque, les échecs de scrub et les connexions SSH refusées sont à remonter au responsable sécurité.

---