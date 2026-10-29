---
title: "Fiche Simple - VM Rocky 9 FreeIPA Sauvegarder"
description: "Réaliser une sauvegarde ipa-backup complète et la mettre hors de l'hôte."
published: true
date: 2026-10-29T20:14:10Z
tags: ["rocky9", "freeipa", "idm", "kerberos"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Rocky_9_FreeIPA_Sauvegarder.md

- **Environnement** : VM Rocky Linux 9 dédiée au premier serveur FreeIPA/IdM
- **OS / Version** : Rocky Linux 9 x86_64; paquets `ipa-server` des dépôts de la distribution
- **Catégorie** : annuaire / sauvegarde
- **Tags** : `rocky9`, `freeipa`, `idm`, `kerberos`

---

## Problème précis à résoudre

Réaliser une sauvegarde `ipa-backup` complète et la mettre hors de l'hôte.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer la sauvegarde :
   ```bash
   sudo ipa-backup
   ```
   👉 Explication : Sauvegarde hors ligne : les services IdM sont arrêtés pendant l'opération, donc prévoir une fenêtre de maintenance.

2. Vérifier le résultat :
   ```bash
   sudo ls -l /var/lib/ipa/backup/
   ```
   👉 Explication : Confirme la présence du répertoire de sauvegarde créé.

3. Copier le répertoire de sauvegarde, chiffré, hors de l'hôte avec l'outil de sauvegarde approuvé.
   👉 Explication : la sauvegarde contient clés et condensats : la protéger comme un secret.

## 2. Production — Contrôles

Planifier la fenêtre de maintenance; la sauvegarde d'un serveur doit contenir tous les rôles (CA, DNS, KRA).

## 3. Production — Sécurité

- Ne pas utiliser `--disable-role-check` : la sauvegarde serait insuffisante pour le PRA.
- Chiffrer et restreindre l'accès aux copies.

## Validation et retour arrière

- **Validation** : une sauvegarde datée existe sous `/var/lib/ipa/backup/` et une copie chiffrée est hors hôte.
- **Retour arrière** : supprimer une sauvegarde invalide après avoir conservé la précédente; redémarrer les services avec `sudo ipactl start` si besoin.

## Si le problème n'est pas résolu

- [FreeIPA — Quick Start Guide](https://www.freeipa.org/page/Quick_Start_Guide)
- [Red Hat — RHEL 9, Installing Identity Management](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/installing_identity_management/index)
- [Guide complet — étape 5](/02-fiches-completes/rocky-linux/9/installation-deploiement/88-deploiement-freeipa-rocky-linux-9#5-sauvegarder)