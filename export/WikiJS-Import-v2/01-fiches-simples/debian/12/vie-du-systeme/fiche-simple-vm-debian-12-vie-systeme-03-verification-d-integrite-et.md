---
title: "Fiche Simple - VM Debian 12 Vie Systeme 03 Verification D Integrite Et"
description: "S'assurer que l'ISO n'est ni corrompue ni modifiée."
published: true
date: 2026-10-29T20:22:10Z
tags: ["debian12", "vie-du-systeme", "cycle-de-vie", "etape-03"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Debian_12_Vie_Systeme_03_Verification_D_Integrite_Et

- **Environnement** : VM Debian 12 « bookworm » (serveur)
- **OS / Version** : Debian 12; étape 03 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `debian12`, `vie-du-systeme`, `cycle-de-vie`, `etape-03`

---

## Problème précis à résoudre

S'assurer que l'ISO n'est ni corrompue ni modifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la somme de contrôle :
   ```bash
   cd ~/iso
   sha256sum -c SHA256SUMS --ignore-missing
   ```
   👉 Explication : doit afficher `OK` pour l'ISO téléchargée.

2. Vérifier la signature de la somme (clé Debian à contrôler par son empreinte officielle) :
   ```bash
   sudo apt install gnupg
   gpg --verify SHA256SUMS.sign SHA256SUMS
   ```
   👉 Explication : confirme que `SHA256SUMS` est signé par Debian; une signature de clé inconnue doit être comparée à l'empreinte publiée sur debian.org.

## 2. Production — Contrôles

Consigner la date, l'empreinte de clé et le résultat dans le dossier.

## 3. Production — Sécurité

Si la vérification échoue, supprimer l'image et la retélécharger.

## Validation et retour arrière

- **Validation** : `OK` pour `sha256sum` et `Good signature` pour `gpg`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Debian 12](/01-fiches-simples/debian/12/vie-du-systeme/sommaire-vie-du-systeme-debian-12)
- [Documentation officielle](https://www.debian.org/doc/)