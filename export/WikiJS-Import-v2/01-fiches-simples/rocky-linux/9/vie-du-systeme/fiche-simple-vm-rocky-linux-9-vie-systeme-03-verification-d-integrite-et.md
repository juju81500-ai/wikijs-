---
title: "Fiche Simple - VM Rocky Linux 9 Vie Systeme 03 Verification D Integrite Et"
description: "Prouver que l'ISO n'est ni corrompue ni modifiée."
published: true
date: 2026-10-29T20:22:10Z
tags: ["rocky9", "vie-du-systeme", "cycle-de-vie", "etape-03"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Rocky_Linux_9_Vie_Systeme_03_Verification_D_Integrite_Et

- **Environnement** : VM Rocky Linux 9 (serveur)
- **OS / Version** : Rocky Linux 9; étape 03 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `rocky9`, `vie-du-systeme`, `cycle-de-vie`, `etape-03`

---

## Problème précis à résoudre

Prouver que l'ISO n'est ni corrompue ni modifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Calculer et comparer l'empreinte SHA-256 :
   ```bash
   sha256sum -c CHECKSUM --ignore-missing
   ```
   👉 Explication : doit afficher `Rocky-9-latest-x86_64-minimal.iso: OK`.

2. Importer la clé publique de publication Rocky :
   ```bash
   curl -LO https://download.rockylinux.org/pub/rocky/RPM-GPG-KEY-Rocky-9
   gpg --import RPM-GPG-KEY-Rocky-9
   gpg --fingerprint | grep -i -A1 rocky
   ```
   👉 Explication : charge la clé; comparer l'empreinte avec celle publiée sur le site officiel.

3. Vérifier la signature du fichier CHECKSUM :
   ```bash
   gpg --verify CHECKSUM.sig CHECKSUM
   ```
   👉 Explication : `Good signature` prouve l'authenticité de la liste d'empreintes (si le fichier `CHECKSUM.sig` est fourni pour la version).

## 2. Production — Contrôles

Conserver la preuve de vérification avec l'image archivée.

## 3. Production — Sécurité

Une empreinte qui ne correspond pas impose de supprimer l'ISO et de la retélécharger.

## Validation et retour arrière

- **Validation** : `OK` pour le SHA-256 et `Good signature` pour GPG.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/sommaire-vie-du-systeme-rocky-linux-9)
- [Documentation officielle](https://docs.rockylinux.org/)