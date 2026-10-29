---
title: "Fiche Simple - VM OPNsense Vie Systeme 03 Verification D Integrite Et"
description: "Prouver que l'image n'est ni corrompue ni modifiée."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-03"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_03_Verification_D_Integrite_Et

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 03 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-03`

---

## Problème précis à résoudre

Prouver que l'image n'est ni corrompue ni modifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Comparer l'empreinte SHA-256 de l'archive téléchargée :
   ```sh
   sha256sum OPNsense-VERSION-dvd-amd64.iso.bz2
   grep dvd-amd64.iso.bz2 OPNsense-VERSION-checksums-amd64.sha256
   ```
   👉 Explication : les deux valeurs hexadécimales doivent être identiques (sous FreeBSD : `sha256`).

2. Télécharger la signature et la clé publique de la version, puis vérifier la signature :
   ```sh
   curl -fLO https://MIROIR/releases/VERSION/OPNsense-VERSION-dvd-amd64.iso.bz2.sig
   curl -fLO https://MIROIR/releases/VERSION/OPNsense-VERSION.pub
   openssl base64 -d -in OPNsense-VERSION-dvd-amd64.iso.bz2.sig -out sig.bin
   openssl dgst -sha256 -verify OPNsense-VERSION.pub -signature sig.bin OPNsense-VERSION-dvd-amd64.iso.bz2
   ```
   👉 Explication : `Verified OK` prouve que l'archive a été signée par le projet; obtenir la clé publique par un canal distinct si possible.

## 2. Production — Contrôles

Conserver la preuve de vérification (sortie des commandes) avec l'image archivée.

## 3. Production — Sécurité

Une empreinte ou une signature invalide impose de supprimer le fichier et de le retélécharger depuis un autre miroir.

## Validation et retour arrière

- **Validation** : SHA-256 identique et `Verified OK` pour la signature.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)