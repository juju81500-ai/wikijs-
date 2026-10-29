---
title: "Fiche Simple - VM Debian 13 Systeme Joindre AD Sssd"
description: "Joindre une machine Debian 13 à un domaine Active Directory avec realmd et sssd, afin que les comptes du domaine puissent se connecter localement et en SSH, sans créer manuellement chaque utilisateur."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[debian13]", "[debian]", "[active-directory]", "[realmd]", "[sssd]", "[kerberos]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Debian_13_Systeme_Joindre_AD_Sssd

- **Environnement** : VM ou serveur Debian 13 membre d'un domaine Active Directory existant
- **OS / Version** : Debian 13 (Trixie) - Famille Debian
- **Catégorie** : Système & Services / Annuaire et authentification
- **Tags** : `[debian13]`, `[debian]`, `[active-directory]`, `[realmd]`, `[sssd]`, `[kerberos]`

## 🎯 Problème précis à résoudre
Joindre une machine Debian 13 à un domaine Active Directory avec `realmd` et `sssd`, afin que les comptes du domaine puissent se connecter localement et en SSH, sans créer manuellement chaque utilisateur.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer les paquets de jonction et de résolution des comptes :
   ```bash
   sudo apt-get update
   sudo apt-get install -y realmd sssd sssd-tools adcli samba-common-bin krb5-user libpam-sss libnss-sss packagekit
   ```
   👉 Explication : `realmd` découvre et joint le domaine, `sssd` fournit l'authentification et la résolution des comptes, `adcli` et `samba-common-bin` effectuent la jonction, `krb5-user` gère Kerberos. Pendant l'installation de `krb5-user`, saisir le domaine en majuscules (par exemple `EXEMPLE.LOCAL`) comme royaume Kerberos.

2. Vérifier que le domaine est découvert et que la résolution DNS fonctionne :
   ```bash
   sudo realm discover <domaine_ad>
   getent hosts <controleur_domaine>
   ```
   👉 Explication : `realm discover` interroge les enregistrements DNS SRV du domaine. Sans résolution DNS vers le contrôleur de domaine, la jonction échoue ; le serveur DNS du client doit être le contrôleur AD.

3. Joindre le domaine avec un compte autorisé à ajouter des machines :
   ```bash
   sudo realm join -U <admin_ad> <domaine_ad>
   realm list
   ```
   👉 Explication : Crée le compte machine dans l'annuaire et génère `/etc/sssd/sssd.conf`. `realm list` doit afficher `configured: kerberos-member` et le domaine joint.

---

## ⚡ 2. Production — Façon Simplifiée
1. Vérifier l'heure et la résolution DNS avant la jonction ; Kerberos refuse un décalage supérieur à 5 minutes :
   ```bash
   timedatectl show -p NTPSynchronized --value
   host -t SRV _ldap._tcp.<domaine_ad>
   ```
   👉 Explication : `NTPSynchronized` doit valoir `yes` (voir la fiche Chrony de Debian 13). Le SRV `_ldap._tcp` doit pointer vers les contrôleurs de domaine.

2. Après la jonction de l'étape 3 de la section 1 (ou sur un serveur déjà joint), adapter le format des identifiants dans `sssd.conf` :
   ```bash
   sudo sed -i 's/use_fully_qualified_names = True/use_fully_qualified_names = False/' /etc/sssd/sssd.conf
   sudo sed -i 's|^fallback_homedir.*|fallback_homedir = /home/%u|' /etc/sssd/sssd.conf
   sudo systemctl restart sssd
   ```
   👉 Explication : Sans `use_fully_qualified_names = False`, les connexions doivent utiliser `utilisateur@domaine`. Le répertoire personnel reste `/home/<utilisateur>` pour les comptes du domaine.

3. Activer la création automatique du répertoire personnel à la première connexion, puis vérifier la résolution d'un compte du domaine :
   ```bash
   sudo pam-auth-update --enable mkhomedir
   id <utilisateur_ad>
   ```
   👉 Explication : `pam-auth-update` est l'outil Debian qui active les modules PAM. `id` doit afficher les groupes du domaine, ce qui prouve que `sssd` répond.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Restreindre les connexions aux groupes autorisés, au lieu d'ouvrir l'accès à tout le domaine :
   ```bash
   sudo realm permit -g <groupe_admins_serveur>@<domaine_ad>
   sudo realm deny --all
   ```
   👉 Explication : `realm deny --all` ferme l'accès à tous les comptes du domaine ; `realm permit -g` n'ouvre que le groupe désigné. Tester la connexion d'un compte hors groupe, qui doit être refusé.

2. Limiter les droits d'administration à un groupe du domaine, dans un fichier sudoers dédié :
   ```bash
   sudo visudo -f /etc/sudoers.d/tssr-ad-admins
   ```
   Contenu attendu : `%<groupe_admins_serveur>@<domaine_ad> ALL=(ALL:ALL) ALL` ; ajuster les droits à la politique du service.
   👉 Explication : `visudo` valide la syntaxe avant l'enregistrement. Ne jamais donner de droits root sans restriction à un groupe large.

3. Contrôler l'état de la jonction et les erreurs sssd après chaque changement de contrôleur de domaine :
   ```bash
   realm list
   sudo journalctl -u sssd --since today --no-pager | tail -n 30
   ```
   👉 Explication : Permet de repérer une perte de contact avec le contrôleur ou un ticket Kerberos invalide avant qu'un utilisateur ne soit bloqué.