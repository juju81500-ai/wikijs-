---
title: "Fiche Simple - VM Windows 11 Visio Valider"
description: "Recetter Visio : démarrage, licence, création et enregistrement d'un diagramme."
published: true
date: 2026-10-29T20:57:15Z
tags: ["visio", "windows11", "microsoft-365", "validation"]
editor: markdown
dateCreated: 2026-10-29T20:57:15Z
dateModified: 2026-10-29T20:57:15Z
---

# Fiche_Simple_-_VM_Windows_11_Visio_Valider

- **Environnement** : Poste Windows 11 x64 d'un utilisateur ou administrateur (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; version Visio à vérifier auprès de l'éditeur
- **Catégorie** : outil de diagrammes / poste de travail
- **Tags** : `visio`, `windows11`, `microsoft-365`, `validation`

---

## Problème précis à résoudre

Recetter Visio : démarrage, licence, création et enregistrement d'un diagramme.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la version installée. PowerShell :
```powershell
(Get-Item 'C:\Program Files\Microsoft Office\root\Office16\VISIO.EXE').VersionInfo.ProductVersion
```
   👉 Explication : retourne la version de Visio.

2. Ouvrir Visio, créer un diagramme réseau, l'enregistrer en .vsdx dans DOSSIER_TEST (à remplacer).
   👉 Explication : valide la licence et l'écriture.

3. Réouvrir le fichier et l'exporter en PDF : GUI **Fichier > Exporter > Créer un document PDF/XPS**.
   👉 Explication : valide la lecture et l'export.

4. Vérifier **Fichier > Compte** : produit activé.
   👉 Explication : confirme l'activation.

## 2. Production — Contrôles

- Consigner le résultat.
- Tester sur un second poste.

## 3. Production — Sécurité

- Supprimer les fichiers de test.

## Validation et retour arrière

- **Validation** : Création, enregistrement, ouverture et export OK.
- **Retour arrière** : Réparer Office via **Paramètres > Applications > Microsoft 365 > Modifier > Réparation en ligne**.

## Si le problème n'est pas résolu

- [Microsoft — Office Deployment Tool](https://learn.microsoft.com/fr-fr/deployoffice/overview-office-deployment-tool)
- [Microsoft — Visio, plans et tarifs](https://www.microsoft.com/fr-fr/microsoft-365/visio/compare-visio-options)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-microsoft-visio)
- [Alternative draw.io : fiche d'entrée](/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-draw-io-desktop)
- [Alternative draw.io : installation (Debian 13)](/01-fiches-simples/debian/13/vie-du-logiciel/draw-io/fiche-simple-vm-debian-13-draw-io-installer)