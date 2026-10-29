---
title: "Fiche Simple - VM Debian 13 PuTTY Configurer"
description: "Générer une clé SSH et se connecter avec plink, pscp ou psftp."
published: true
date: 2026-10-29T21:24:09Z
tags: ["putty", "putty-tools", "plink", "puttygen", "ssh", "configuration", "cle-ssh"]
editor: markdown
dateCreated: 2026-10-29T21:24:09Z
dateModified: 2026-10-29T21:24:09Z
---

# Fiche_Simple_-_VM_Debian_13_PuTTY_Configurer

- **Environnement** : VM Debian 13 (Trixie), poste d'administration en ligne de commande
- **OS / Version** : Debian 13 (Trixie) — paquet putty-tools
- **Catégorie** : outils d'administration / SSH
- **Tags** : `putty`, `putty-tools`, `plink`, `puttygen`, `ssh`, `configuration`, `cle-ssh`

---

## Problème précis à résoudre

Générer une clé SSH et se connecter avec `plink`, `pscp` ou `psftp`.

## 1. Hors-Production (Lab / Test / POC)

1. Générer une clé Ed25519 protégée par une phrase de passe saisie à l'invite :
   ```bash
   puttygen -t ed25519 -o ~/.ssh/CLE_A_REMPLACER.ppk
   ```
   👉 Explication : `CLE_A_REMPLACER` est un nom à remplacer ; la phrase de passe se saisit en interactif (ne pas l'écrire en clair).
2. Exporter la clé publique à placer dans `authorized_keys` du serveur :
   ```bash
   puttygen -L ~/.ssh/CLE_A_REMPLACER.ppk
   ```
   👉 Explication : `-L` affiche la clé publique au format OpenSSH.
3. Se connecter et exécuter une commande :
   ```bash
   plink -i ~/.ssh/CLE_A_REMPLACER.ppk UTILISATEUR@SERVEUR_SSH uptime
   ```
   👉 Explication : `UTILISATEUR` et `SERVEUR_SSH` sont à remplacer.
4. Copier un fichier :
   ```bash
   pscp -i ~/.ssh/CLE_A_REMPLACER.ppk FICHIER_LOCAL UTILISATEUR@SERVEUR_SSH:/chemin/
   ```
   👉 Explication : `pscp` utilise SSH ; `psftp` offre un mode interactif.

## 2. Production — Contrôles

- Vérifier l'empreinte de clé d'hôte lors de la première connexion.

## 3. Production — Sécurité

- Fichier de clé en droits `600` : `chmod 600 ~/.ssh/CLE_A_REMPLACER.ppk`.

## Validation et retour arrière

- **Validation** : la commande distante s'exécute. **Retour arrière** : supprimer la clé publique du serveur et le fichier `.ppk`.

## Si le problème n'est pas résolu

- [Fiche d'entrée PuTTY](/01-fiches-simples/logiciels/11-scripting-developpement-et-administration/fiche-logiciel-putty)
- [Debian — paquet putty-tools](https://packages.debian.org/trixie/putty-tools)
- [Documentation officielle PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html)