---
title: "Fiche Simple - VM Debian 13 Vie Systeme 35 Controle D Acces Obligatoire"
description: "Confiner les services."
published: true
date: 2026-10-29T20:22:10Z
tags: ["debian13", "vie-du-systeme", "cycle-de-vie", "etape-35"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Debian_13_Vie_Systeme_35_Controle_D_Acces_Obligatoire

- **Environnement** : VM Debian 13 « trixie » (serveur)
- **OS / Version** : Debian 13; étape 35 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian13`, `vie-du-systeme`, `cycle-de-vie`, `etape-35`

---

## Problème précis à résoudre

Confiner les services.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler et installer les profils :
   ```bash
   sudo apt install apparmor apparmor-utils apparmor-profiles
   sudo aa-status
   ```
   👉 Explication : liste les profils chargés et en mode `enforce`.

2. Passer un profil en application (remplacer le chemin) :
   ```bash
   sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx
   ```
   👉 Explication : force le blocage; utiliser `aa-complain` pour apprendre.

## 2. Production — Contrôles

Passer en `complain` pour tester avant `enforce`.

## 3. Production — Sécurité

Lire `journalctl -k | grep apparmor` pour les refus.

## Validation et retour arrière

- **Validation** : `aa-status` montre les profils en `enforce`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 13](/01-fiches-simples/debian/13/vie-du-systeme/sommaire-vie-du-systeme-debian-13)
- [Documentation officielle](https://www.debian.org/doc/)