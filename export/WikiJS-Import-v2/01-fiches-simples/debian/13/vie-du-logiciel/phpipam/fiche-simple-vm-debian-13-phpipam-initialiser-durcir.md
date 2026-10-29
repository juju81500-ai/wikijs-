---
title: "Fiche Simple - VM Debian 13 phpIPAM Initialiser Durcir"
description: "Initialiser le schéma puis désactiver l'installateur et durcir la console."
published: true
date: 2026-10-29T20:14:10Z
tags: ["debian13", "phpipam", "ipam", "nginx", "mariadb", "installateur", "durcissement"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Debian_13_phpIPAM_Initialiser_Durcir.md

- **Environnement** : VM Debian 13, phpIPAM avec MariaDB locale, PHP-FPM et Nginx
- **OS / Version** : Debian 13 Trixie x86-64; phpIPAM 1.8.3; PHP 8.4
- **Catégorie** : IPAM / sécurité
- **Tags** : `debian13`, `phpipam`, `ipam`, `nginx`, `mariadb`, `installateur`, `durcissement`

---

## Problème précis à résoudre

Initialiser le schéma puis désactiver l'installateur et durcir la console.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir `https://ipam.example.net/` (nom d'exemple) et lancer l'assistant d'installation avec le compte SQL applicatif `phpipam`.
   👉 Explication : initialise le schéma; ne jamais fournir le compte root.

2. Changer immédiatement le mot de passe administrateur initial.
   👉 Explication : les identifiants par défaut sont publiés dans le README officiel.

3. Exécuter :
   ```bash
   sudoedit /var/www/phpipam/config.php
   ```
   👉 Explication : passer `$disable_installer = true` et vérifier `$debugging = false`.

4. Créer des comptes nominatifs et groupes limités aux sections nécessaires; créer un token API minimal seulement si l'API est utilisée.
   👉 Explication : réduit les droits de chaque acteur.

5. Saisir quelques préfixes et adresses fictifs du lab et vérifier sous-réseaux, VLAN et sections.
   👉 Explication : valide le modèle sans scan ni suppression automatique.

## 2. Production — Contrôles

Ne pas activer scan, ping, discovery ni suppression des adresses inactives dans cette procédure.

## 3. Production — Sécurité

- Mot de passe admin changé immédiatement.
- Installateur désactivé.
- API sans HTTP non sécurisé.
- Compte administrateur réservé aux changements d'administration.

## Validation et retour arrière

- **Validation** : connexion nominative possible, installateur désactivé, données de test correctes.
- **Retour arrière** : restaurer la base et `config.php` sauvegardés; en lab, recréer la base.

## Si le problème n'est pas résolu

- [phpIPAM — mise à niveau et restauration](https://phpipam.net/documents/upgrade/)
- [phpIPAM — configuration de référence 1.8.3](https://github.com/phpipam/phpipam/blob/v1.8.3/config.dist.php)
- [Guide complet Déployer phpIPAM 1.8.3 sur Debian 13](/02-fiches-completes/debian/13/installation-deploiement/74-deploiement-phpipam-1-8-3-debian-13#6-initialiser-et-durcir-phpipam)