---
title: "VM_Debian_12_Stockage_Configuration-Partage-Samba"
description: "Installer le service Samba sur Debian 12, créer un partage réseau compatible Windows/Linux, gérer les utilisateurs Samba et restreindre l'accès par sous-réseau et chiffrement du protocole."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian12]", "[samba]", "[smb]", "[cifs]", "[partage-fichiers]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Debian_12_Stockage_Configuration-Partage-Samba.md

- **Environnement** : VM (Debian 12 Bookworm)
- **OS / Version** : Debian 12 - Famille Debian
- **Catégorie** : Stockage / Partage de fichiers (Samba / SMB)
- **Tags** : `[debian12]`, `[samba]`, `[smb]`, `[cifs]`, `[partage-fichiers]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer le service Samba sur Debian 12, créer un partage réseau compatible Windows/Linux, gérer les utilisateurs Samba et restreindre l'accès par sous-réseau et chiffrement du protocole.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du paquet Samba :
   `apt-get update && apt-get install -y samba`
   👉 Explication : Télécharge et installe le démon Samba (smbd/nmbd).

2. Créer un dossier de test lisible, sans écriture anonyme :
   `install -d -o root -g root -m 0755 /srv/samba/public`
   👉 Explication : Le partage de test reste en lecture seule ; ne jamais utiliser `chmod 777` pour résoudre un problème de droits.

3. Ajouter un bloc de partage de test en lecture seule dans `/etc/samba/smb.conf`, puis valider avant rechargement :
   ```ini
   [Public-Test]
   path = /srv/samba/public
   browseable = yes
   read only = yes
   guest ok = yes
   ```
   `testparm -s && systemctl reload smbd`
   👉 Explication : Rend un contenu de test lisible sans autoriser l'écriture anonyme.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création du dossier de stockage et du groupe dédié :
   `groupadd --system smbgroup && install -d -o root -g smbgroup -m 2770 /srv/samba/partage_tssr`
   👉 Explication : Restreint l'accès système uniquement aux membres du groupe smbgroup.

2. Ajout d'un utilisateur système au sous-système Samba :
   `useradd -M -s /sbin/nologin user_tssr && usermod -aG smbgroup user_tssr && smbpasswd -a user_tssr`
   👉 Explication : Crée un compte restreint sans accès shell local et l'enregistre dans la base d'authentification Samba (passdb).

3. Configuration du partage authentifié dans `/etc/samba/smb.conf` (appliquer les droits de dossiers et fichiers séparément ; ne pas rendre tous les fichiers exécutables) :
   `[Partage_TSSR]\npath = /srv/samba/partage_tssr\nvalid users = @smbgroup\nguest ok = no\nwritable = yes\nbrowseable = yes`
   👉 Explication : Exige une authentification valide et réserve l'accès aux utilisateurs du groupe smbgroup.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Forcer le chiffrement SMB et limiter les clients dans la section `[global]` après sauvegarde du fichier :
   ```ini
   server min protocol = SMB3_02
   server smb encrypt = required
   hosts allow = 192.0.2.0/24 127.0.0.1
   hosts deny = 0.0.0.0/0
   ```
   Remplacer le réseau d'exemple par le réseau client réel, puis exécuter `testparm -s` avant `systemctl reload smbd`.
   👉 Explication : Bloque les anciennes versions vulnérables du protocole SMB (SMB1/SMB2) et force le chiffrement AES du trafic réseau.

2. Masquage des fichiers non autorisés et blocage des fichiers exécutables (.exe, .bat, .sh) :
   `sed -i '/\[Partage_TSSR\]/a \   veto files = /*.exe/*.bat/*.vbs/*.sh/\n   hide unreadable = yes' /etc/samba/smb.conf`
   👉 Explication : Empêche le dépôt de fichiers exécutables potentiellement malveillants et masque les fichiers illisibles pour l'utilisateur.

3. Autoriser TCP/445 uniquement aux clients prévus dans le pare-feu persistant déjà géré par le serveur. N'ajouter les règles SMB dans la configuration propriétaire, les valider, puis appliquer pendant une fenêtre ; ne pas utiliser une règle `nft add rule` en mémoire comme configuration finale.