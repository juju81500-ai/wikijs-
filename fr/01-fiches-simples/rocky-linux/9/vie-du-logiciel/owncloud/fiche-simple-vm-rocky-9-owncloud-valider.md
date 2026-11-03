---
title: "Fiche Simple - VM Rocky 9 ownCloud Valider"
description: "Vérifier service, logs et URL TLS."
published: true
date: 2026-11-03T09:36:13Z
tags: ["owncloud", "serveur", "vie-du-logiciel", "valider"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_VM_Rocky_9_ownCloud_Valider

- **Environnement** : VM Rocky Linux 9; ownCloud Infinite Scale (oCIS), binaire officiel
- **OS / Version** : Rocky Linux 9
- **Catégorie** : Vie du logiciel / ownCloud — Valider (recette)
- **Tags** : `owncloud`, `serveur`, `vie-du-logiciel`, `valider`

---

## Problème précis à résoudre

Vérifier service, logs et URL TLS.

## 1. Hors-Production (Lab / Test / POC)

1. Valider (recette) :
   ```bash
   /usr/local/bin/ocis version
systemctl is-active ocis
sudo journalctl -u ocis -n 80 --no-pager
curl -fsSI https://CLOUD.EXAMPLE.NET/
   ```
   👉 Explication : Remplacer le FQDN; tester connexion puis un fichier non sensible depuis un client autorisé.


## 2. Production — Contrôles

Valider authentification, stockage et cycle de fichier depuis poste approuvé.

## 3. Production — Sécurité

Ne pas utiliser données sensibles ou comptes démo.

## Validation et retour arrière

- **Validation** : Service actif, TLS valide, scénario utilisateur réussi.
- **Retour arrière** : Fermer l’accès proxy et restaurer configuration validée.

## Si le problème n'est pas résolu

- [Prérequis et limites](/fr/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-prerequis-limites)
- [Installer](/fr/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-installer)
- [Configurer](/fr/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-configurer)
- [Sécuriser](/fr/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-securiser)
- [Sauvegarder / restaurer](/fr/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-sauvegarder-restaurer)
- [Mise à jour et retour arrière](/fr/01-fiches-simples/rocky-linux/9/vie-du-logiciel/owncloud/fiche-simple-vm-rocky-9-owncloud-mise-a-jour-retour-arriere)
- [Documentation officielle](https://owncloud.dev/ocis/deployment/systemd/)