---
title: "VM_Debian_12_Systeme_Joindre-AD-Sssd"
description: "Joindre un serveur Debian 12 à un domaine Active Directory avec realmd et sssd, authentifier les comptes du domaine et restreindre l'ouverture de session aux seuls groupes autorisés."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian12]", "[debian-family]", "[realmd]", "[sssd]", "[active-directory]", "[kerberos]", "[adcli]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 VM_Debian_12_Systeme_Joindre-AD-Sssd.md

- **Environnement** : VM (Proxmox VE / KVM)
- **OS / Version** : Debian 12 (Bookworm) - Famille Debian
- **Catégorie** : Système & Identité / Jonction Active Directory
- **Tags** : `[debian12]`, `[debian-family]`, `[realmd]`, `[sssd]`, `[active-directory]`, `[kerberos]`, `[adcli]`

## 🎯 Problème précis à résoudre
Joindre un serveur Debian 12 à un domaine Active Directory avec `realmd` et `sssd`, authentifier les comptes du domaine et restreindre l'ouverture de session aux seuls groupes autorisés.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation des paquets de jonction :
   `sudo apt-get update && sudo apt-get install -y realmd sssd sssd-tools adcli krb5-user samba-common-bin packagekit`
   👉 Explication : Installe `realmd` (découverte et jonction), `sssd` (authentification), `adcli` (compte machine) et Kerberos. Pour `krb5-user`, saisir le royaume en MAJUSCULES (ex. `<DOMAINE.LOCAL>`).
2. Découverte du domaine :
   `sudo realm discover <domaine.local>`
   👉 Explication : Interroge le DNS et les contrôleurs de domaine pour valider que le domaine est joignable et connu.
3. Résolution du contrôleur de domaine :
   `getent hosts <domaine.local>`
   👉 Explication : Vérifie que le nom de domaine se résout ; un échec signifie que le DNS du serveur ne pointe pas vers les DC.

---

## ⚡ 2. Production — Façon Simplifiée
1. Jonction au domaine avec un compte délégué :
   `sudo realm join -U <admin_ad> <domaine.local>`
   👉 Explication : Crée le compte machine dans l'OU par défaut, configure `sssd` et Kerberos. Le mot de passe est demandé en interactif.
2. Contrôle de la jonction :
   `realm list`
   👉 Explication : Affiche le domaine joint, les formats de connexion et les services configurés.

---

## 🔒 3. Production — Façon Sécurisée (Restriction par groupe & Home)
1. Restriction des connexions à un groupe AD :
   `sudo realm permit -g "<groupe_ad_autorise>"`
   👉 Explication : Par défaut, `realm join` autorise tout le domaine ; cette commande limite l'accès au groupe désigné. Retirer l'autorisation globale si nécessaire avec `sudo realm deny --all`.
2. Création automatique du répertoire personnel :
   `sudo pam-auth-update --enable mkhomedir`
   👉 Explication : Active le module PAM qui crée le `/home` des utilisateurs AD à la première connexion.
3. Vérification d'identité côté système :
   `id <utilisateur>@<domaine.local>`
   👉 Explication : Confirme que le compte AD est résolu avec ses UID, GID et groupes ; sinon vérifier `sudo systemctl status sssd`.