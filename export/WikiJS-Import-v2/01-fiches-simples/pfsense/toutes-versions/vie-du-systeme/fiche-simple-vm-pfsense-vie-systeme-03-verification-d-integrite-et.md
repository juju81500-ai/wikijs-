---
title: "Fiche Simple - VM pfSense Vie Systeme 03 Verification D Integrite Et"
description: "Prouver que l'image n'est ni corrompue ni modifiée."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-03"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_03_Verification_D_Integrite_Et

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 03 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-03`

---

## Problème précis à résoudre

Prouver que l'image n'est ni corrompue ni modifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Comparer l'empreinte SHA-256 de l'archive :
   ```sh
   sha256sum -c pfSense-CE-VERSION-RELEASE-amd64.iso.gz.sha256
   sha256sum pfSense-CE-VERSION-RELEASE-amd64.iso.gz
   ```
   👉 Explication : doit afficher `OK`; sous FreeBSD utiliser `sha256` et comparer à la valeur du fichier `.sha256`.

2. Comparer l'empreinte avec celle affichée sur la page officielle de téléchargement ou de la documentation Netgate, obtenue par un second canal.
   👉 Explication : pfSense CE ne fournit pas de signature GPG pour l'ISO : la somme de contrôle issue de deux canaux HTTPS distincts limite le risque.

## 2. Production — Contrôles

Conserver la preuve de vérification avec l'image archivée.

## 3. Production — Sécurité

Une empreinte différente impose de supprimer l'ISO et de la retélécharger depuis un autre miroir.

## Validation et retour arrière

- **Validation** : `OK` pour le SHA-256.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)