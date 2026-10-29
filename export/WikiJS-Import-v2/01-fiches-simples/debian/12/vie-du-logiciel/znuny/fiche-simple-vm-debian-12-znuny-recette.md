---
title: "Fiche Simple - VM Debian 12 Znuny Recette"
description: "Valider le fonctionnement de Znuny et préparer l'exploitation (sauvegarde, mises à jour)."
published: true
date: 2026-10-29T19:55:10Z
tags: ["debian12", "znuny", "recette", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T19:55:10Z
dateModified: 2026-10-29T19:55:10Z
---

# Fiche_Simple_-_VM_Debian_12_Znuny_Recette.md

- **Environnement** : VM Debian 12 dédiée (Apache/mod_perl, MariaDB 10.11), Znuny 7.3.8
- **OS / Version** : Debian 12 Bookworm; Znuny 7.3.8
- **Catégorie** : ITSM / ticketing
- **Tags** : `debian12`, `znuny`, `recette`, `sauvegarde`

---

## Problème précis à résoudre

Valider le fonctionnement de Znuny et préparer l'exploitation (sauvegarde, mises à jour).

## 1. Hors-Production (Lab / Test / POC)

1. Créer un ticket de test, l'affecter, y répondre par courriel et vérifier l'accès selon les rôles.
   👉 Explication : on valide le cycle complet de traitement.

2. Contrôler les services après redémarrage de la VM :
   ```bash
   sudo reboot
   systemctl is-active apache2 mariadb
   ```
   👉 Explication : tous les services doivent revenir seuls. Lancer la deuxième commande après la reconnexion.

3. Sauvegarder la base (l'authentification passe par le socket local, sans mot de passe en argument) :
   ```bash
   sudo mariadb-dump --single-transaction znuny > znuny-AAAAMMJJ.sql
   ```
   👉 Explication : on obtient une copie logique de la base. Remplacer `AAAAMMJJ` par la date du jour.

4. Sauvegarder aussi les fichiers locaux :
   ```bash
   sudo tar -czf znuny-fichiers-AAAAMMJJ.tar.gz /opt/znuny/Kernel/Config.pm
   ```
   👉 Explication : `Config.pm` contient la configuration locale; ajouter les pièces jointes si elles sont stockées sur disque.

5. Restaurer dans un lab avant la production et planifier les mises à jour de sécurité.
   👉 Explication : une sauvegarde non testée n'est pas fiable.

## 2. Production — Contrôles

Configurer SMTP, annuaire et stockage des pièces jointes selon les politiques; planifier sauvegardes et mises à jour.

## 3. Production — Sécurité

- Chiffrer et stocker les sauvegardes hors hôte : elles contiennent des données de tickets et des secrets.
- Lire les notes de version avant toute mise à jour.

## Validation et retour arrière

- **Validation** : Ticket de test traité, services actifs après reboot, sauvegarde restaurée en lab.
- **Retour arrière** : Restaurer la base et `Config.pm` depuis la dernière sauvegarde; sur VM, revenir au snapshot.

## Si le problème n'est pas résolu

- [Znuny — Installation officielle](https://doc.znuny.org/znuny/installation/index.html)
- [Znuny — Release 7.3.8](https://doc.znuny.org/znuny/releases/7_3_8/index.html)
- [Znuny — Opérations et maintenance](https://doc.znuny.org/znuny/standardoperations/index.html)
- [Guide complet — recette et exploitation](/02-fiches-completes/debian/12/installation-deploiement/42-deploiement-znuny-7-3-8-debian-12#8-recette-et-exploitation)