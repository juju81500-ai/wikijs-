---
title: "VM_Debian_13_Securite_Hardening-SSH-ED25519"
description: "Durcir le service d'accès distant OpenSSH sur Debian 13 (Trixie), imposer la connexion par clé asymétrique moderne ED25519, désactiver l'authentification par mot de passe et masquer l'accès du compte root."
published: true
date: 2026-10-27T10:53:30Z
tags: ["[debian13]", "[ssh]", "[ed25519]", "[hardening]", "[security]", "[openssh]"]
editor: markdown
dateCreated: 2026-10-27T10:53:30Z
dateModified: 2026-10-27T10:53:30Z
---

# 📄 VM_Debian_13_Securite_Hardening-SSH-ED25519.md

- **Environnement** : VM (Debian 13 Trixie / OpenSSH 9.x)
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Sécurité / Accès Distant SSH
- **Tags** : `[debian13]`, `[ssh]`, `[ed25519]`, `[hardening]`, `[security]`, `[openssh]`

## 🎯 Problème précis à résoudre
Durcir le service d'accès distant OpenSSH sur Debian 13 (Trixie), imposer la connexion par clé asymétrique moderne ED25519, désactiver l'authentification par mot de passe et masquer l'accès du compte root.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Génération d'une paire de clés SSH ED25519 sur le poste d'administration :
   `ssh-keygen -t ed25519 -C "admin@lab.local" -f ~/.ssh/id_ed25519`
   👉 Explication : Crée une clé cryptographique haute sécurité basée sur la courbe elliptique Ed25519.

2. Copie temporaire de la clé publique sur le serveur cible :
   `ssh-copy-id -i ~/.ssh/id_ed25519.pub user_tssr@192.168.1.130`
   👉 Explication : Injecte la clé publique dans le fichier `~/.ssh/authorized_keys` du compte utilisateur distant.

3. Test de connexion sans mot de passe :
   `ssh -i ~/.ssh/id_ed25519 user_tssr@192.168.1.130`
   👉 Explication : Valide le bon fonctionnement de l'authentification par clé privée.

---

## ⚡ 2. Production — Façon Simplifiée
1. Garder la session actuelle et un accès console de secours ouverts. Copier la clé publique sur le serveur, puis confirmer une seconde connexion par clé avant de désactiver tout autre mode.

2. Sauvegarder la configuration et examiner les valeurs réellement appliquées :
   ```bash
   sudo cp -a /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
   sudo sshd -T | grep -E '^(port|permitrootlogin|passwordauthentication|pubkeyauthentication) '
   ```
   👉 Explication : OpenSSH peut prendre la première valeur rencontrée dans les fichiers inclus ; un fichier nommé `99-...` n'écrase pas nécessairement les valeurs précédentes.

3. Configurer un fichier géré dans `/etc/ssh/sshd_config.d/` avec des directives vérifiées :
   ```text
   PermitRootLogin no
   PubkeyAuthentication yes
   PasswordAuthentication no
   KbdInteractiveAuthentication no
   ```
   Ne pas changer le port dans cet exemple. Si un port différent est requis, coordonner d'abord les règles locales et amont, puis tester une nouvelle connexion avant de fermer la session de secours.

4. Tester la syntaxe et recharger :
   ```bash
   sudo sshd -t && sudo systemctl reload ssh
   sudo systemctl --no-pager status ssh
   ```
   👉 Explication : `sshd -t` valide la configuration avant application. Garder la console et l'ancienne session jusqu'à validation d'une nouvelle connexion.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. N'imposer une liste explicite de KEX, ciphers ou MAC que si une exigence l'impose et après vérification de la prise en charge par le client et le serveur (`man sshd_config`, `ssh -Q` et `sshd -T`). Ne pas copier la directive `s2v1-sha256@libssh.org`, qui est invalide.

2. Pour limiter les comptes, vérifier les membres avant de configurer `AllowGroups` :
   ```bash
   getent group ssh-users || sudo groupadd --system ssh-users
   sudo usermod -aG ssh-users user_tssr
   id user_tssr
   ```
   Ajouter `AllowGroups ssh-users` une seule fois après avoir inclus tous les comptes d'administration. Tester une nouvelle connexion avant de fermer la session de secours.

3. Vérifier les propriétaires et permissions du fichier de configuration et du compte concerné :
   ```bash
   sudo chown root:root /etc/ssh/sshd_config.d/99-hardening.conf
   sudo chmod 600 /etc/ssh/sshd_config.d/99-hardening.conf
   sudo chown -R user_tssr:user_tssr /home/user_tssr/.ssh
   sudo chmod 700 /home/user_tssr/.ssh
   sudo chmod 600 /home/user_tssr/.ssh/authorized_keys
   ```

4. Le pare-feu doit autoriser le port réellement configuré et être géré par son mécanisme persistant. Ne pas utiliser `nft add rule` sans vérifier la table/chaîne active et la persistance. Valider le filtrage depuis une console avant déconnexion.