---
title: "Fiche Simple - VM Ubuntu 24.04 Systeme Joindre AD Sssd"
description: "Joindre un serveur Ubuntu Server 24.04 LTS à un domaine Active Directory avec realmd et sssd, autoriser des groupes AD précis à se connecter et contrôler la résolution des comptes du domaine."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[ubuntu24.04]", "[ubuntu]", "[active-directory]", "[realmd]", "[sssd]", "[kerberos]", "[pam]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Ubuntu_24.04_Systeme_Joindre_AD_Sssd

- **Environnement** : VM Ubuntu Server joint à un domaine Active Directory
- **OS / Version** : Ubuntu Server 24.04 LTS (Noble Numbat) - realmd 0.17.x et SSSD 2.9.x (versions des dépôts Noble)
- **Catégorie** : Système / Annuaire et authentification centralisée
- **Tags** : `[ubuntu24.04]`, `[ubuntu]`, `[active-directory]`, `[realmd]`, `[sssd]`, `[kerberos]`, `[pam]`

## 🎯 Problème précis à résoudre
Joindre un serveur Ubuntu Server 24.04 LTS à un domaine Active Directory avec `realmd` et `sssd`, autoriser des groupes AD précis à se connecter et contrôler la résolution des comptes du domaine.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérifier la résolution DNS du domaine, qui doit pointer vers un contrôleur de domaine :
   ```bash
   resolvectl status | grep -i 'DNS Servers'
   host -t SRV _ldap._tcp.<domaine>
   ```
   👉 *Explication : Une jonction AD échoue presque toujours par un DNS incorrect ; l'enregistrement SRV `_ldap._tcp` doit répondre.*
2. Installer les composants et découvrir le domaine :
   ```bash
   sudo apt update
   sudo apt install -y realmd sssd sssd-tools adcli libnss-sss libpam-sss
   sudo realm discover <domaine>
   ```
   👉 *Explication : `realm discover` interroge le DNS et les contrôleurs de domaine ; il doit afficher le type `active-directory` et les logiciels pris en charge.*

## ⚡ 2. Production — Façon Simplifiée
1. Joindre le domaine avec un compte autorisé à créer des objets ordinateur :
   ```bash
   sudo realm join --user=<compte_admin_ad> <domaine>
   ```
   👉 *Explication : La commande demande le mot de passe du compte et crée l'objet ordinateur dans l'Active Directory.*
2. Autoriser uniquement un groupe AD à se connecter, puis activer la création du répertoire personnel :
   ```bash
   sudo realm permit -g '<groupe_ad>@<domaine>'
   sudo pam-auth-update --enable mkhomedir
   realm list
   ```
   👉 *Explication : `realm permit` restreint les ouvertures de session ; `mkhomedir` crée le répertoire personnel à la première connexion. Par défaut, `realm join` autorise tous les comptes du domaine.*

## 🔒 3. Production — Façon Sécurisée
1. Désactiver les noms complets (`utilisateur@domaine`) et limiter les répertoires personnels :
   ```bash
   sudo sed -i 's/^use_fully_qualified_names = True/use_fully_qualified_names = False/' /etc/sssd/sssd.conf
   sudo sed -i 's/^fallback_homedir = .*/fallback_homedir = \/home\/%u/' /etc/sssd/sssd.conf
   sudo systemctl restart sssd
   ```
   👉 *Explication : Simplifie les noms de connexion et garde des répertoires personnels prévisibles. Vérifier le fichier `/etc/sssd/sssd.conf` après modification.*
2. Accorder les droits sudo à un groupe AD via un fichier dédié, validé par `visudo` :
   ```bash
   sudo install -o root -g root -m 0440 /dev/null /etc/sudoers.d/ad-admins
   sudo tee /etc/sudoers.d/ad-admins >/dev/null <<'EOF'
   %<groupe_admins_ad> ALL=(ALL:ALL) ALL
   EOF
   sudo visudo -cf /etc/sudoers.d/ad-admins
   ```
   👉 *Explication : Un fichier sudoers mal formé peut bloquer l'accès administrateur ; `visudo -cf` doit répondre `parsed OK`. Le groupe doit être écrit sans espace inutile.*

## ✅ Validation et retour arrière
- Depuis un autre poste, ouvrir une session SSH avec `<utilisateur>@<domaine>` et vérifier `id` ; le groupe AD autorisé doit apparaître.
- Vérifier la jonction avec `sudo realm list` et les journaux avec `sudo journalctl -u sssd --since today --no-pager`.
- Retour arrière : `sudo realm leave <domaine>` (avec `--user=<compte_admin_ad>` si demandé), puis `sudo apt purge -y realmd sssd sssd-tools`.