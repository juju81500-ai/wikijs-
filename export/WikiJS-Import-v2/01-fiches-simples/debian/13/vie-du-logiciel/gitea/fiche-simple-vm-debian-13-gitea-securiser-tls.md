---
title: "Fiche Simple - VM Debian 13 Gitea Securiser TLS"
description: "Mettre le reverse proxy sous HTTPS et limiter les flux entrants."
published: true
date: 2026-10-29T20:47:59Z
tags: ["debian13", "gitea", "forge-git", "tls", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T20:47:59Z
dateModified: 2026-10-29T20:47:59Z
---

# Fiche_Simple_-_VM_Debian_13_Gitea_Securiser_TLS

- **Environnement** : VM Debian 13 isolée; domaine et stockage définis
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : forge Git / administration
- **Tags** : `debian13`, `gitea`, `forge-git`, `tls`, `sauvegarde`
---

## Problème précis à résoudre

Mettre le reverse proxy sous HTTPS et limiter les flux entrants.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les ports écoutés
   ```bash
   sudo ss -lntp
   sudo systemctl --no-pager status gitea
   ```
   👉 Explication : le port 3000 reste interne; n’exposer que les ports approuvés.

2. Configurer proxy et certificat TLS
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitea.com/installation/install-from-binary
   ```
   👉 Explication : remplacer le nom par le FQDN à remplacer; suivre le guide du proxy retenu. Détail à confirmer dans la documentation officielle avant application : Configurer le proxy approuvé pour le FQDN, certificat valide et transmission du schéma HTTPS. Conserver ROOT_URL = https://FQDN/ (FQDN à remplacer).

3. Vérifier certificat et accès HTTPS
   ```bash
   openssl s_client -connect forge.example.com:443 -servername forge.example.com </dev/null
   curl -I https://forge.example.com/
   ```
   👉 Explication : remplacer le FQDN; contrôler chaîne, nom d’hôte, expiration et redirection.

4. Limiter ports au pare-feu de l’organisation
   ```text
   Navigateur > ouvrir la documentation officielle : https://docs.gitea.com/installation/install-from-binary
   ```
   👉 Explication : faire appliquer les ACL par l’équipe réseau et préserver l’accès d’administration. Détail à confirmer dans la documentation officielle avant application : Autoriser 443/TCP depuis les réseaux clients approuvés. Autoriser le SSH Git seulement si retenu et depuis les réseaux prévus. Refuser l’accès direct au port 3000.

## 2. Production — Contrôles

Tester depuis les zones autorisées et refusées; faire valider TLS, renouvellement, MFA, pare-feu et accès SSH.

## 3. Production — Sécurité

- Forcer HTTPS et activer MFA selon la politique.
- Ne pas exposer le port backend ou l’assistant d’installation.
- Révoquer immédiatement les accès d’un compte ou d’une clé compromis.

## Validation et retour arrière

- **Validation** : HTTPS est valide et le backend est inaccessible directement aux clients.
- **Retour arrière** : Rétablir l’ancienne configuration proxy/certificat; ne pas désactiver TLS pour contourner l’incident.

## Si le problème n'est pas résolu

- [Gitea — installation depuis un binaire](https://docs.gitea.com/installation/install-from-binary)
- [Gitea — configuration](https://docs.gitea.com/administration/config-cheat-sheet)
- [Gitea — sauvegarde/restauration](https://docs.gitea.com/administration/backup-and-restore)
- [Fiche connexe](</01-fiches-simples/debian/13/vie-du-logiciel/gitea/fiche-simple-vm-debian-13-gitea-prerequis-limites>)