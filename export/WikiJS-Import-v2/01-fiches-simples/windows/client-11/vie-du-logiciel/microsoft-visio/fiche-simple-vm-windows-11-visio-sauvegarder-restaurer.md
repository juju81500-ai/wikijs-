---
title: "Fiche Simple - VM Windows 11 Visio Sauvegarder Restaurer"
description: "Sauvegarder et restaurer les fichiers Visio et les personnalisations."
published: true
date: 2026-10-29T20:57:15Z
tags: ["visio", "windows11", "microsoft-365", "sauvegarde"]
editor: markdown
dateCreated: 2026-10-29T20:57:15Z
dateModified: 2026-10-29T20:57:15Z
---

# Fiche_Simple_-_VM_Windows_11_Visio_Sauvegarder_Restaurer

- **Environnement** : Poste Windows 11 x64 d'un utilisateur ou administrateur (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; version Visio à vérifier auprès de l'éditeur
- **Catégorie** : outil de diagrammes / poste de travail
- **Tags** : `visio`, `windows11`, `microsoft-365`, `sauvegarde`

---

## Problème précis à résoudre

Sauvegarder et restaurer les fichiers Visio et les personnalisations.

## 1. Hors-Production (Lab / Test / POC)

1. Identifier les fichiers à protéger : fichiers .vsdx, formes personnelles (Mes formes) et modèles.
   👉 Explication : ces éléments ne sont pas inclus dans l'application.

2. Copier vers une sauvegarde :
```powershell
robocopy "$env:USERPROFILE\Documents\Mes formes" CHEMIN_SAUVEGARDE\MesFormes /MIR /R:2 /W:5
```
   👉 Explication : CHEMIN_SAUVEGARDE est à remplacer ; /MIR supprime en destination ce qui n'existe plus en source : vérifier avant usage.

3. Activer l'historique des versions sur le site SharePoint/OneDrive : GUI **Bibliothèque > Paramètres > Paramètres de la bibliothèque > Paramètres de contrôle de version**.
   👉 Explication : permet de restaurer une version antérieure d'un diagramme.

4. Restaurer : inverser la copie vers un dossier de test puis ouvrir un fichier restauré.
   👉 Explication : une sauvegarde n'est valable que si elle est testée.

## 2. Production — Contrôles

- Sauvegarde quotidienne planifiée.
- Copie hors site.

## 3. Production — Sécurité

- Chiffrer la sauvegarde.
- Droits limités aux propriétaires.

## Validation et retour arrière

- **Validation** : Fichier restauré ouvert correctement.
- **Retour arrière** : Rétablir l'ancienne version depuis l'historique ou la sauvegarde.

## Si le problème n'est pas résolu

- [Microsoft — Office Deployment Tool](https://learn.microsoft.com/fr-fr/deployoffice/overview-office-deployment-tool)
- [Microsoft — Visio, plans et tarifs](https://www.microsoft.com/fr-fr/microsoft-365/visio/compare-visio-options)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-microsoft-visio)
- [Alternative draw.io : fiche d'entrée](/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-draw-io-desktop)
- [Alternative draw.io : installation (Debian 13)](/01-fiches-simples/debian/13/vie-du-logiciel/draw-io/fiche-simple-vm-debian-13-draw-io-installer)