---
title: "Fiche Simple - VM Debian 13 Centreon Installer Central"
description: "Installer Centreon Central 26.10 avec le script officiel, TLS activé."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "centreon", "supervision", "tls", "unattended"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_Centreon_Installer_Central.md

- **Environnement** : VM Debian 13 dédiée, serveur Centreon Central avec MariaDB locale
- **OS / Version** : Debian 13 Trixie; Centreon 26.10
- **Catégorie** : supervision / installation
- **Tags** : `debian13`, `centreon`, `supervision`, `tls`, `unattended`

---

## Problème précis à résoudre

Installer Centreon Central 26.10 avec le script officiel, TLS activé.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier avant de lancer : sauvegarde de la VM faite, DNS et certificat validés.
   👉 Explication : l'installation configure paquets, MariaDB et services; elle est difficile à annuler.

2. Exécuter :
   ```bash
   sudo bash /root/centreon-install/unattended.sh install -t central -v 26.10 --tls enabled
   ```
   👉 Explication : lance l'installation du Central en version 26.10 avec TLS activé.

3. Noter où l'outil affiche les identifiants générés, les copier dans un coffre puis supprimer le fichier temporaire.
   👉 Explication : ces secrets ne doivent figurer ni dans un ticket ni dans la documentation.

4. Ne pas utiliser l'option `-s` lors de la première installation.
   👉 Explication : l'automatisation complète n'est pas validée à ce stade.

## 2. Production — Contrôles

Suivre le journal d'installation et contrôler les étapes finales; l'assistant Web et les rôles d'accès ne sont pas terminés automatiquement.

## 3. Production — Sécurité

- Protéger les identifiants générés dans un coffre.
- Ne pas désactiver durablement le pare-feu.
- Ne pas publier le Central hors réseau de gestion.

## Validation et retour arrière

- **Validation** : l'installation se termine sans erreur et les services sont installés.
- **Retour arrière** : restaurer la sauvegarde de la VM prise avant l'installation.

## Si le problème n'est pas résolu

- [Centreon — installation unattended](https://docs.centreon.com/docs/installation/installation-of-a-central-server/unattended-install-central/)
- [Centreon — installation par paquets](https://docs.centreon.com/docs/installation/installation-of-a-central-server/using-packages/)
- [Guide complet Déployer Centreon 26.10 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/48-deploiement-centreon-26-10-debian-13#3-installer-le-central-avec-tls)