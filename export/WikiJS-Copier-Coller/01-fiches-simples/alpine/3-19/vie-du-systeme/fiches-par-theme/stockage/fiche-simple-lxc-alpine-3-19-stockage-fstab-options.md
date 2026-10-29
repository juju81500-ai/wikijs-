# 📄 Fiche_Simple_-_LXC_Alpine_3.19_Stockage_Fstab_Options.md

- **Environnement** : LXC (Proxmox VE)
- **OS / Version** : Alpine Linux 3.19 - Famille Alpine (OpenRC, apk)
- **Catégorie** : Stockage & Systèmes de fichiers / Montages

## 🎯 Problème précis à résoudre
Vérifier et durcir les montages persistants d'un conteneur Alpine Linux (`/etc/fstab`) avec les options `nodev`, `nosuid` et `noexec`, tout en tenant compte de la gestion des disques par Proxmox pour un LXC.

> Alpine 3.19 est en fin de support : valider cette procédure sur une branche maintenue avant tout usage en production.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lister les montages actifs et les entrées persistantes :
   ```sh
   mount
   df -h
   cat /etc/fstab
   ```
   👉 Explication : `mount` affiche les montages effectifs, `df -h` l'espace utilisé, et `/etc/fstab` les montages rejoués au démarrage.

2. Ajouter un montage `tmpfs` durci pour `/tmp` :
   ```text
   tmpfs   /tmp   tmpfs   defaults,nodev,nosuid,noexec,size=512M   0 0
   ```
   👉 Explication : `noexec` interdit l'exécution directe de binaires depuis `/tmp`, `nosuid` ignore le bit SUID et `nodev` ignore les fichiers périphériques. Sauvegarder `/etc/fstab` avant cette modification.

3. Appliquer les entrées sans redémarrer et contrôler le résultat :
   ```sh
   mount -a
   mount | grep ' /tmp '
   ```
   👉 Explication : `mount -a` monte toutes les entrées de `/etc/fstab` qui ne le sont pas encore. Dans un LXC non privilégié, le montage `tmpfs` peut être refusé : lire le message d'erreur, puis retirer la ligne.

---

## ⚡ 2. Production — Façon Simplifiée
1. Déclarer un disque de données depuis l'hôte Proxmox, et non dans le `fstab` du conteneur :
   ```sh
   pct set <vmid> -mp0 /srv/<nom_du_volume>,mp=/srv/<nom_du_volume>
   pct reboot <vmid>
   ```
   👉 Explication : Pour un LXC, le point de montage est géré par Proxmox dans `/etc/pve/lxc/<vmid>.conf`. Le conteneur n'a pas à gérer le périphérique bloc lui-même.

2. Vérifier le point de montage dans le conteneur :
   ```sh
   mount | grep ' /srv/<nom_du_volume> '
   df -h /srv/<nom_du_volume>
   ```
   👉 Explication : Le montage doit apparaître avec la taille attendue. Sinon, contrôler la configuration `mp0` sur l'hôte.

---

## 🔒 3. Production — Façon Sécurisée
1. Sauvegarder l'état du `fstab`, puis vérifier les options appliquées aux répertoires temporaires :
   ```sh
   cp -a /etc/fstab /root/fstab.avant-durcissement.bak
   mount | grep -E ' /tmp | /var/tmp | /dev/shm '
   ```
   👉 Explication : Les options `nodev,nosuid,noexec` doivent figurer sur `/tmp`, `/var/tmp` et `/dev/shm`. N'appliquer `noexec` qu'à un répertoire qui ne doit jamais exécuter de logiciel.

2. Ne pas monter de disque avec des options `exec` ou `suid` sur un répertoire de dépôt de fichiers accessible par des comptes de service, et retenir que les options de montage de l'hôte priment sur celles du conteneur.