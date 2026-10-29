---
title: "Fiche Simple - VM Rocky 9 Securite Hardening Comptes SSH"
description: "Passer à des comptes nominatifs et à une authentification SSH par clé."
published: true
date: 2026-10-29T20:22:42Z
tags: ["rocky9", "rhel9", "hardening", "ssh", "sudo", "wheel"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Fiche_Simple_-_VM_Rocky_9_Securite_Hardening_Comptes_SSH.md

- **Environnement** : VM ou serveur dédié Rocky Linux 9 avant ouverture en production
- **OS / Version** : Rocky Linux 9 / famille RHEL 9
- **Catégorie** : sécurité / SSH
- **Tags** : `rocky9`, `rhel9`, `hardening`, `ssh`, `sudo`, `wheel`

---

## Problème précis à résoudre

Passer à des comptes nominatifs et à une authentification SSH par clé.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler le compte administrateur (`admin1` est un nom d'exemple à remplacer) :
   ```bash
   id admin1
   sudo -l -U admin1
   ```
   👉 Explication : vérifie son identité et ses droits sudo.

2. Ajouter le compte à `wheel` selon la politique, puis installer sa clé publique approuvée et tester une seconde connexion :
   ```bash
   sudo usermod -aG wheel admin1
   ```
   👉 Explication : la seconde connexion prouve l'accès avant de réduire le mot de passe.

3. Valider la syntaxe SSH :
   ```bash
   sudo sshd -t
   ```
   👉 Explication : aucune erreur avant rechargement.

4. Lire les paramètres effectifs :
   ```bash
   sudo sshd -T | grep -E 'permitrootlogin|passwordauthentication|pubkeyauthentication'
   ```
   👉 Explication : vérifie root, mot de passe et clés.

5. Recharger `sshd` seulement après `sshd -t` réussi :
   ```bash
   sudo systemctl reload sshd
   ```
   👉 Explication : applique sans couper les sessions ouvertes.

## 2. Production — Contrôles

Gérer les réglages dans un fichier documenté, sans directive en double.

## 3. Production — Sécurité

- Ne pas exposer SSH à tout Internet.
- Garder une session ouverte pendant le test d'une nouvelle connexion.

## Validation et retour arrière

- **Validation** : connexion par clé réussie avec le compte nominatif.
- **Retour arrière** : restaurer `/etc/ssh` depuis la copie, `sudo sshd -t`, `sudo systemctl reload sshd`.

## Si le problème n'est pas résolu

- [Rocky Linux — documentation](https://docs.rockylinux.org/)
- [Red Hat — SELinux sur RHEL 9](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/using_selinux/)
- [Guide complet hardening Rocky Linux 9](/02-fiches-completes/rocky-linux/9/autres/24-hardening-production-rocky-linux-9#3-limiter-les-comptes-et-lacces-ssh)