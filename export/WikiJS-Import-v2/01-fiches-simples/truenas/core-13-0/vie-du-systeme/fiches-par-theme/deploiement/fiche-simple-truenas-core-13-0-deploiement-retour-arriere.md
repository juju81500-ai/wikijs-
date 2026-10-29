---
title: "Fiche Simple - TrueNAS CORE 13.0 Deploiement Retour Arriere"
description: "Savoir revenir à un état précédent."
published: true
date: 2026-10-29T20:22:42Z
tags: ["truenas-core", "truenas", "freebsd", "zfs", "smb", "nas"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Fiche_Simple_-_TrueNAS_CORE_13.0_Deploiement_Retour_Arriere.md

- **Environnement** : Appliance TrueNAS CORE (FreeBSD) en VM de laboratoire ou NAS existant
- **OS / Version** : TrueNAS CORE, branche 13.0 (build exact à relever sur l'ISO)
- **Catégorie** : stockage NAS / reprise
- **Tags** : `truenas-core`, `truenas`, `freebsd`, `zfs`, `smb`, `nas`

---

## Problème précis à résoudre

Savoir revenir à un état précédent.

## 1. Hors-Production (Lab / Test / POC)

1. Avant toute mise à jour : exporter la configuration (**System > General > Save Config**) et prendre un snapshot de la VM (laboratoire).
   👉 Explication : point de retour avant changement.

2. Pour revenir à une configuration : **System > General > Upload Config**.
   👉 Explication : recharge le fichier `.db` exporté.

3. **Reset Config** : à utiliser seulement après export de la configuration.
   👉 Explication : remet l'appareil aux paramètres d'usine et force un nouveau mot de passe.

4. Une migration vers SCALE n'est pas décrite ici : suivre la documentation officielle et valider d'abord en laboratoire.
   👉 Explication : évite une migration non testée.

## 2. Production — Contrôles

Si un pool est détruit ou des disques effacés, seule une sauvegarde externe permet la reprise.

## 3. Production — Sécurité

- Fichier de configuration protégé comme un secret.

## Validation et retour arrière

- **Validation** : La configuration exportée est rechargeable en laboratoire.
- **Retour arrière** : Upload Config ou retour au snapshot de VM.

## Si le problème n'est pas résolu

- [TrueNAS — documentation CORE 13.0](https://www.truenas.com/docs/core/13.0/)
- [TrueNAS — Software Status](https://www.truenas.com/docs/softwarestatus/)
- [Guide complet — 7. Retour arrière](/02-fiches-completes/truenas/core-13-0/installation-deploiement/89-deploiement-truenas-core-13-0#7-retour-arriere)