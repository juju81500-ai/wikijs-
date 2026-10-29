---
title: "Fiche Simple - VM Rocky 9 Securite SSH Cle Sshd"
description: "Déployer une clé cryptographique ed25519 pour l'administrateur, puis durcir sshd (pas de mot de passe, pas de connexion root) sans perdre l'accès au serveur."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[rocky9]", "[rhel9]", "[ssh]", "[sshd]", "[cles]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Rocky_9_Securite_SSH_Cle_Sshd.md

- **Environnement** : VM ou serveur Rocky Linux
- **OS / Version** : Rocky Linux 9 / RHEL 9 (OpenSSH 8.7 et supérieur)
- **Catégorie** : Sécurité / Accès distant SSH
- **Tags** : `[rocky9]`, `[rhel9]`, `[ssh]`, `[sshd]`, `[cles]`, `[hardening]`

## 🎯 Problème précis à résoudre
Déployer une clé cryptographique ed25519 pour l'administrateur, puis durcir `sshd` (pas de mot de passe, pas de connexion root) sans perdre l'accès au serveur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Générer la paire de clés sur le poste client :
   ```bash
   ssh-keygen -t ed25519 -C "<utilisateur>@<poste>"
   ```
   👉 Explication : Crée `~/.ssh/id_ed25519` (privée) et `~/.ssh/id_ed25519.pub` (publique). Protéger la clé privée par une passphrase.

2. Copier la clé publique sur le serveur :
   ```bash
   ssh-copy-id -i ~/.ssh/id_ed25519.pub <utilisateur>@<nom_du_serveur>
   ```
   👉 Explication : Ajoute la clé publique dans `~/.ssh/authorized_keys` de l'utilisateur distant. Cette commande s'exécute sur le poste client.

3. Tester la connexion par clé :
   ```bash
   ssh -i ~/.ssh/id_ed25519 <utilisateur>@<nom_du_serveur>
   ```
   👉 Explication : La connexion doit aboutir sans demande de mot de passe (la passphrase de la clé peut être demandée).

---

## ⚡ 2. Production — Façon Simplifiée
1. Créer un fichier de durcissement dans le répertoire `sshd_config.d` (lu via la directive `Include` en tête de `/etc/ssh/sshd_config`) :
   ```bash
   sudo tee /etc/ssh/sshd_config.d/10-durcissement.conf >/dev/null <<'EOF'
   PermitRootLogin no
   PubkeyAuthentication yes
   PasswordAuthentication no
   KbdInteractiveAuthentication no
   MaxAuthTries 3
   EOF
   ```
   👉 Explication : Un drop-in évite de modifier le fichier principal. `sshd` retient la première valeur lue, et les drop-ins sont lus avant le reste du fichier.

2. Valider la syntaxe puis recharger le service :
   ```bash
   sudo sshd -t
   sudo systemctl reload sshd
   ```
   👉 Explication : `sshd -t` valide la configuration sans rien appliquer; en cas d'erreur, ne pas recharger. `reload` conserve les sessions déjà ouvertes.

3. Vérifier la configuration effective :
   ```bash
   sudo sshd -T | grep -Ei '^(permitrootlogin|passwordauthentication|pubkeyauthentication)'
   ```
   👉 Explication : `sshd -T` affiche la configuration réellement appliquée, après lecture des Include. Les valeurs attendues sont `no`, `no` et `yes`.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Limiter la connexion SSH à un groupe dédié. Créer le groupe et y ajouter l'administrateur **avant** de limiter la connexion :
   ```bash
   sudo groupadd ssh-admins
   sudo usermod -aG ssh-admins <utilisateur>
   ```
   👉 Explication : Sans ce groupe, l'utilisateur ne pourra plus se connecter après l'ajout de `AllowGroups` ci-dessous.

2. Ajouter la directive dans le drop-in existant, puis valider :
   ```bash
   echo "AllowGroups ssh-admins" | sudo tee -a /etc/ssh/sshd_config.d/10-durcissement.conf
   sudo sshd -t && sudo systemctl reload sshd
   ```
   👉 Explication : Seuls les membres du groupe `ssh-admins` peuvent ouvrir une session SSH. Garder une session active pendant le test.

3. Restreindre le port 22 au réseau d'administration avec firewalld :
   ```bash
   sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="<reseau_admin>/24" service name="ssh" accept'
   sudo firewall-cmd --permanent --remove-service=ssh
   sudo firewall-cmd --reload
   ```
   👉 Explication : Accepte SSH uniquement depuis `<reseau_admin>` et retire le service général. Tester depuis une seconde session avant de fermer la première.

---

## ✅ Contrôle
```bash
sudo sshd -T | grep -i '^allowgroups'
sudo firewall-cmd --list-rich-rules
```
👉 Explication : Confirme la liste blanche de groupe et la règle de pare-feu appliquée.