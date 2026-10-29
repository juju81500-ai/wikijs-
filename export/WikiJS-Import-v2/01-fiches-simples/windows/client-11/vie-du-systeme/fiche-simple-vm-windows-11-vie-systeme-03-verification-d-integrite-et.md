---
title: "Fiche Simple - VM Windows 11 Vie Systeme 03 Verification D Integrite Et"
description: "S'assurer que l'ISO n'est ni corrompue ni modifiée."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windows11", "vie-du-systeme", "cycle-de-vie", "etape-03"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_03_Verification_D_Integrite_Et

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 03 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windows11`, `vie-du-systeme`, `cycle-de-vie`, `etape-03`

---

## Problème précis à résoudre

S'assurer que l'ISO n'est ni corrompue ni modifiée.

## 1. Hors-Production (Lab / Test / POC)

1. Calculer l'empreinte SHA-256 du fichier (pas d'équivalent graphique natif : utiliser PowerShell ou `certutil -hashfile FICHIER SHA256`).
   ```powershell
   Get-FileHash 'C:\ISO\Win11_FR.iso' -Algorithm SHA256 | Format-List
   ```
   👉 Explication : affiche le hachage SHA-256 de l'ISO téléchargée.

2. Comparer à l'empreinte publiée par Microsoft ou par le portail de licences (page de téléchargement ou fichier de somme fourni).
   ```powershell
   $Attendu = 'EMPREINTE_SHA256_PUBLIEE'
   (Get-FileHash 'C:\ISO\Win11_FR.iso' -Algorithm SHA256).Hash -eq $Attendu
   ```
   👉 Explication : renvoie `True` uniquement si l'empreinte est identique; remplacer `EMPREINTE_SHA256_PUBLIEE` par la valeur officielle.

3. Monter l'ISO pour contrôler son contenu : **Explorateur de fichiers > clic droit sur l'ISO > Monter**.
   ```powershell
   Mount-DiskImage -ImagePath 'C:\ISO\Win11_FR.iso'
   $L = (Get-DiskImage 'C:\ISO\Win11_FR.iso' | Get-Volume).DriveLetter
   Get-ChildItem "${L}:\sources\install.*"
   Dismount-DiskImage -ImagePath 'C:\ISO\Win11_FR.iso'
   ```
   👉 Explication : vérifie la présence de `install.wim` ou `install.esd` puis démonte l'image.

4. Consigner l'empreinte contrôlée dans le dossier du projet.
   👉 Explication : preuve de traçabilité de l'image utilisée.

## 2. Production — Contrôles

Refuser toute image dont l'empreinte diffère; retélécharger depuis la source officielle.

## 3. Production — Sécurité

Conserver l'empreinte hors du dossier de l'image (registre de déploiement) pour détecter une altération ultérieure.

## Validation et retour arrière

- **Validation** : `Get-FileHash` identique à l'empreinte officielle.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Fiche détaillée : VM Windows 11 Sysinternals Telecharger Verifier](</01-fiches-simples/windows/client-11/vie-du-logiciel/sysinternals/fiche-simple-vm-windows-11-sysinternals-telecharger-verifier>)
- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/sommaire-vie-du-systeme-windows-11)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)