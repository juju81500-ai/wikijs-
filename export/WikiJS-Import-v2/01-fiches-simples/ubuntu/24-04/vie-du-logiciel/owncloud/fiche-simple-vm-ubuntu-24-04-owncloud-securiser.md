---
title: "Fiche Simple - VM Ubuntu 24.04 ownCloud Securiser"
description: "Restreindre accès oCIS au reverse proxy HTTPS."
published: true
date: 2026-10-29T21:07:31Z
tags: ["owncloud", "serveur", "vie-du-logiciel", "securiser"]
editor: markdown
dateCreated: 2026-10-29T21:07:31Z
dateModified: 2026-10-29T21:07:31Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_ownCloud_Securiser

- **Environnement** : VM Ubuntu Server 24.04; ownCloud Infinite Scale (oCIS), binaire officiel
- **OS / Version** : Ubuntu Server 24.04
- **Catégorie** : Vie du logiciel / ownCloud — Sécuriser
- **Tags** : `owncloud`, `serveur`, `vie-du-logiciel`, `securiser`

---

## Problème précis à résoudre

Restreindre accès oCIS au reverse proxy HTTPS.

## 1. Hors-Production (Lab / Test / POC)

1. Sécuriser :
   ```bash
   sudo ss -lntp | grep -E ":(443|9200)\b" || true
sudo ufw allow from ADMIN_CIDR to any port 22 proto tcp
sudo ufw allow 443/tcp
sudo ufw status verbose
   ```
   👉 Explication : `ADMIN_CIDR` est un placeholder. Ouvrir HTTPS uniquement; 9200 reste au proxy local.


## 2. Production — Contrôles

Configurer certificat TLS valide et contrôler qu’aucune règle n’expose le backend.

## 3. Production — Sécurité

Protéger certificats/environnement, limiter sources et garder SELinux/pare-feu actifs.

## Validation et retour arrière

- **Validation** : HTTPS valide et 9200 non accessible depuis réseaux non autorisés.
- **Retour arrière** : Rétablir les règles précédentes sans couper l’administration.

## Si le problème n'est pas résolu

- [Prérequis et limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-prerequis-limites)
- [Installer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-installer)
- [Configurer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-configurer)
- [Valider (recette)](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-valider)
- [Sauvegarder / restaurer](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/owncloud/fiche-simple-vm-ubuntu-24-04-owncloud-mise-a-jour-retour-arriere)
- [Documentation officielle](https://owncloud.dev/ocis/deployment/systemd/)