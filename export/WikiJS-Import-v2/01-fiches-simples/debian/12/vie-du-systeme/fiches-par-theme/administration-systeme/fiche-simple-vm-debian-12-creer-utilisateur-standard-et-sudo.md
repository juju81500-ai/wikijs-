---
title: "VM_Debian_12_Utilisateurs_Creer-Utilisateur-Standard-Et-Sudo"
description: "Créer un utilisateur système classique (sans privilèges particuliers) ainsi qu'un utilisateur administrateur disposant des droits d'élévation sudo sous Debian/Ubuntu, configurer les shells par défaut et sécuriser l'accès aux comptes."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian12]", "[ubuntu24.04]", "[utilisateurs]", "[sudo]", "[droits]", "[useradd]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Debian_12_Utilisateurs_Creer-Utilisateur-Standard-Et-Sudo.md

- **Environnement** : VM / LXC (Debian 12 / Ubuntu 24.04)
- **OS / Version** : Debian 12 (Bookworm) / Ubuntu 24.04 LTS - Famille Debian
- **Catégorie** : Utilisateurs & Droits / Gestion des Comptes
- **Tags** : `[debian12]`, `[ubuntu24.04]`, `[utilisateurs]`, `[sudo]`, `[droits]`, `[useradd]`, `[hardening]`

---

## 🎯 Problème précis à résoudre
Créer un utilisateur système classique (sans privilèges particuliers) ainsi qu'un utilisateur administrateur disposant des droits d'élévation sudo sous Debian/Ubuntu, configurer les shells par défaut et sécuriser l'accès aux comptes.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. **Création rapide d'un utilisateur classique sans mot de passe complexe** :
   `useradd -m -s /bin/bash user_std && echo "user_std:Pass123!" | chpasswd`
   👉 *Explication : Tu crées le compte utilisateur user_std avec son dossier personnel (/home/user_std), lui attribues le shell Bash et définis son mot de passe initial.*

2. **Création rapide d'un utilisateur administrateur avec privilèges Sudo** :
   `useradd -m -s /bin/bash user_admin && echo "user_admin:Admin123!" | chpasswd && usermod -aG sudo user_admin`
   👉 *Explication : Tu crées l'utilisateur user_admin et l'ajoutes immédiatement au groupe sudo pour lui accorder les droits d'administration de la machine.*

3. **Vérification rapide des privilèges et groupes** :
   `id user_admin`
   👉 *Explication : Tu contrôles les identifiants UID/GID et vérifies l'appartenance au groupe sudo.*

---

## ⚡ 2. Production — Façon Simplifiée
1. **Création interactive guidée d'un utilisateur standard avec la commande adduser** :
   `adduser jdupont`
   👉 *Explication : Tu réponds à l'assistant interactif qui crée le répertoire /home/jdupont, impose la saisie sécurisée du mot de passe et configure les informations de profil.*

2. **Création interactive d'un utilisateur administrateur d'exploitation TSSR** :
   `adduser adm-jdupont && usermod -aG sudo adm-jdupont`
   👉 *Explication : Tu crées le compte d'administration nommé distinct du compte standard et lui attribues l'élévation Sudo.*

3. **Test d'élévation de privilèges sous le compte admin** :
   `su - adm-jdupont -c "sudo whoami"`
   👉 *Explication : Tu bascules sous le compte administrateur et testes que la commande sudo renvoie bien "root".*

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. **Désactivation du compte root direct et obligation d'utiliser sudo avec MDP** :
   `passwd -l root`
   👉 *Explication : Tu verrouilles l'accès direct au compte superutilisateur root pour forcer la traçabilité nominative via sudo.*

2. **Inactivation des comptes inactifs et politique d'expiration de mot de passe** :
   `chage -M 90 -m 7 -W 14 jdupont`
   👉 *Explication : Tu forces le renouvellement du mot de passe tous les 90 jours avec un préavis de notification de 14 jours.*

3. **Verrouillage du umask par défaut à 027 (Permissions strictes 750 sur les dossiers personnels)** :
   `chmod 700 /home/jdupont && chmod 700 /home/adm-jdupont`
   👉 *Explication : Tu restreins la lecture et l'accès aux répertoires personnels uniquement aux propriétaires des comptes.*