# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Stockage_Fstab_Options

- **Environnement** : VM Ubuntu Server
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat)
- **Catégorie** : Stockage / Montages et options de sécurité
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[fstab]`, `[mount]`, `[tmpfs]`, `[nodev]`, `[nosuid]`, `[noexec]`

## 🎯 Problème précis à résoudre
Vérifier les montages déclarés dans `/etc/fstab` sur Ubuntu Server 24.04 LTS, ajouter les options `nodev`, `nosuid` et `noexec` sur `/tmp`, `/var/tmp` et `/dev/shm`, puis valider le fichier avant tout redémarrage.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Lister les montages actifs et leurs options :
   ```bash
   findmnt
   findmnt --verify
   ```
   👉 *Explication : `findmnt --verify` contrôle la syntaxe de `/etc/fstab` et signale les points de montage absents ou les options inconnues.*
2. Sauvegarder le fichier et relever les identifiants des partitions :
   ```bash
   sudo cp -a /etc/fstab /etc/fstab.bak
   sudo blkid
   ```
   👉 *Explication : Référencer les disques par UUID évite un décalage de nom (`/dev/sdb`) après ajout d'un disque.*

## ⚡ 2. Production — Façon Simplifiée
1. Ouvrir `/etc/fstab` et ajouter les lignes suivantes pour les montages temporaires :
   ```bash
   sudo nano /etc/fstab
   ```
   ```text
   tmpfs /tmp     tmpfs defaults,nodev,nosuid,noexec,size=1G,mode=1777 0 0
   tmpfs /dev/shm tmpfs defaults,nodev,nosuid,noexec                  0 0
   ```
   👉 *Explication : `nodev` interdit les périphériques spéciaux, `nosuid` ignore le bit SUID, `noexec` interdit l'exécution de binaires depuis ces montages. Ne pas appliquer `noexec` sur un répertoire où un installeur doit exécuter des scripts.*
2. Recharger systemd, valider et appliquer les montages :
   ```bash
   sudo systemctl daemon-reload
   sudo findmnt --verify
   sudo mount -a
   findmnt -o TARGET,FSTYPE,OPTIONS /tmp /dev/shm
   ```
   👉 *Explication : `mount -a` monte tout ce qui est déclaré ; la vérification finale doit afficher `nodev,nosuid,noexec`.*

## 🔒 3. Production — Façon Sécurisée
1. Ajouter les mêmes options à `/var/tmp` lorsqu'il est un montage séparé, puis contrôler le résultat :
   ```bash
   findmnt -o TARGET,OPTIONS /var/tmp
   ```
   👉 *Explication : Sous Ubuntu 24.04, `/var/tmp` est souvent sur le système racine ; une option ne s'applique qu'à un montage distinct.*
2. Tester qu'un binaire ne peut pas s'exécuter depuis `/tmp` :
   ```bash
   printf '#!/bin/sh\necho ok\n' | sudo tee /tmp/test-noexec.sh >/dev/null
   sudo chmod +x /tmp/test-noexec.sh
   /tmp/test-noexec.sh
   sudo rm -f /tmp/test-noexec.sh
   ```
   👉 *Explication : La commande doit échouer avec `Permission denied` ; le script de test est supprimé immédiatement.*

## ✅ Validation et retour arrière
- Après validation, faire un test de redémarrage en fenêtre de maintenance ; vérifier ensuite `findmnt --verify` sans erreur.
- En cas d'échec de montage, restaurer le fichier depuis la console avec `sudo cp -a /etc/fstab.bak /etc/fstab`, puis `sudo systemctl daemon-reload` et `sudo mount -a`.
