---
title: "Fiche Simple - VM Debian 13 GitLab CE Sauvegarder Restaurer"
description: "Sauvegarder les données GitLab et séparément configuration/secrets puis valider restauration isolée."
published: true
date: 2026-10-29T20:47:59Z
tags: ["debian13", "gitlab-ce", "forge-git", "tls", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T20:47:59Z
dateModified: 2026-10-29T20:47:59Z
---

# Fiche_Simple_-_VM_Debian_13_GitLab_CE_Sauvegarder_Restaurer

- **Environnement** : VM Debian 13 de préproduction; FQDN et ressources confirmés
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : forge Git / administration
- **Tags** : `debian13`, `gitlab-ce`, `forge-git`, `tls`, `sauvegarde`
---

## Problème précis à résoudre

Sauvegarder les données GitLab et séparément configuration/secrets puis valider restauration isolée.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l’espace avant backup
   ```bash
   sudo df -h /var/opt/gitlab /var/log/gitlab
   sudo gitlab-ctl status
   ```
   👉 Explication : anticiper la taille du backup.

2. Créer un backup Omnibus
   ```bash
   sudo gitlab-backup create
   ```
   👉 Explication : vérifier le résultat et l’emplacement; ce backup ne contient pas automatiquement tous les fichiers système.

3. Sauvegarder config et secrets séparément
   ```bash
   sudo install -d -m 0700 /root/gitlab-config-backup
   sudo cp -a /etc/gitlab/gitlab.rb /etc/gitlab/gitlab-secrets.json /root/gitlab-config-backup/
   ```
   👉 Explication : fichiers sensibles à chiffrer et transférer vers une cible restreinte.

4. Répéter restauration sur même version en environnement isolé
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitlab.com/install/package/
   ```
   👉 Explication : restaurer configuration, secrets et données de façon cohérente. Détail à confirmer dans la documentation officielle avant application : Restaurer selon le guide GitLab pour une version correspondante. Vérifier dépôt témoin et accès sans connexion à la production.

## 2. Production — Contrôles

Définir RPO/RTO, rétention, chiffrement et restauration périodique indépendante du serveur source.

## 3. Production — Sécurité

- Protéger secrets et sauvegardes au même niveau que la production.
- Ne pas considérer un job vert sans restauration testée comme PRA validé.
- Ne pas restaurer une version d’état sur une instance active non compatible.

## Validation et retour arrière

- **Validation** : Instance isolée démarre et un projet/dépôt témoin est accessible.
- **Retour arrière** : Restaurer l’ensemble cohérent d’une date vérifiée et garder la cible isolée si l’essai échoue.

## Si le problème n'est pas résolu

- [GitLab — installation paquet](https://docs.gitlab.com/install/package/)
- [GitLab — configuration Omnibus](https://docs.gitlab.com/omnibus/settings/)
- [GitLab — backup/restore](https://docs.gitlab.com/omnibus/backup-restore/)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/gitlab/fiche-simple-vm-debian-13-gitlab-ce-prerequis-limites>)