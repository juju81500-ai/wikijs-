---
title: "VM_Debian_13_Stockage_Configuration-NFS-Server-v4"
description: "Installer et configurer un serveur de fichiers NFSv4 exclusif sur Debian 13 (Trixie), exporter un répertoire de données partagé, désactiver le protocole obsolète et vulnérable NFSv3, et sécuriser le filtrage des clients."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[debian13]", "[nfs]", "[nfsv4]", "[storage]", "[partage-fichiers]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 VM_Debian_13_Stockage_Configuration-NFS-Server-v4.md

- **Environnement** : VM (Debian 13 Trixie / Proxmox Storage)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Stockage / Partage de fichiers NFSv4
- **Tags** : `[debian13]`, `[nfs]`, `[nfsv4]`, `[storage]`, `[partage-fichiers]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer et configurer un serveur de fichiers NFSv4 exclusif sur Debian 13 (Trixie), exporter un répertoire de données partagé, désactiver le protocole obsolète et vulnérable NFSv3, et sécuriser le filtrage des clients.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du serveur NFS :
   `apt-get update && apt-get install -y nfs-kernel-server`
   👉 Explication : Télécharge et installe les modules noyau et les démons du serveur NFS.

2. Création d'un répertoire de test avec droits restreints :
   `groupadd --system nfs_lab && install -d -o root -g nfs_lab -m 2770 /mnt/lab_nfs`
   👉 Explication : Réserve l'accès aux membres du groupe ; ne pas utiliser `chmod 777` pour corriger les permissions.

3. Exportation de test limitée à un réseau de laboratoire dans `/etc/exports` :
   `/mnt/lab_nfs 192.0.2.0/24(rw,sync,root_squash,no_subtree_check)`
   Puis valider et afficher les exports avec `exportfs -rav && exportfs -v`.
   👉 Explication : Remplacer le réseau documentaire par le sous-réseau réel ; ne jamais exporter en écriture à `*`.

---

## ⚡ 2. Production — Façon Simplifiée
1. Structure d'exportation NFSv4 avec racine virtuelle dédiée (`/export`) :
   `mkdir -p /export/partage_tssr /srv/donnees && mount --bind /srv/donnees /export/partage_tssr`
   👉 Explication : Monte le dossier de stockage réel `/srv/donnees` dans la racine virtuelle NFSv4 `/export`.

2. Ajout du point de montage persistant dans `/etc/fstab` :
   `echo "/srv/donnees /export/partage_tssr none bind 0 0" >> /etc/fstab`
   👉 Explication : S'assure de la persistance de la liaison bind au redémarrage du système.

3. Configuration restrictive de l'exportation NFSv4 dans `/etc/exports` :
   /export                  192.0.2.0/24(ro,fsid=0,root_squash,no_subtree_check)
   /export/partage_tssr     192.0.2.0/24(rw,sync,root_squash,no_subtree_check)
   👉 Explication : Restreint l'accès aux seules machines du sous-réseau `192.168.1.0/24` sous le protocole NFSv4.

4. Application des règles d'exportation :
   `exportfs -r`
   👉 Explication : Force le rechargement de la table des répertoires partagés par le noyau.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Désactivation stricte de NFSv2, NFSv3 et de rpcbind dans `/etc/nfs.conf` :
   [nfsd]
   vers2=no
   vers3=no
   vers4=yes
   vers4.2=yes
   👉 Explication : Force l'utilisation exclusive de NFSv4.2 et supprime le service de mappage de ports vulnérable `rpcbind`.

2. Arrêt et désactivation du service rpcbind inutile en NFSv4 pur :
   `systemctl disable --now rpcbind.service rpcbind.socket`
   👉 Explication : Réduit la surface d'attaque en fermant le port 111 (RPC Portmapper).

3. Garder `root_squash` sur les exports et vérifier qu'aucune règle plus permissive ne le remplace :
   `sudo exportfs -v`
   👉 Explication : `root_squash` empêche le root distant de conserver ses privilèges. Ne pas utiliser `no_root_squash` sur un partage accessible par le réseau.

4. Autoriser TCP/2049 aux seuls clients NFS dans le pare-feu persistant géré par le serveur ; valider et appliquer la règle via ce gestionnaire. Ne pas utiliser une règle nftables ajoutée en mémoire comme configuration de production.