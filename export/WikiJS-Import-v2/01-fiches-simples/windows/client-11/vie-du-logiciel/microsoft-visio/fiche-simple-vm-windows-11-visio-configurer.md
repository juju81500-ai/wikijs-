---
title: "Fiche Simple - VM Windows 11 Visio Configurer"
description: "Configurer licence, modèles et options de Visio."
published: true
date: 2026-10-29T20:57:15Z
tags: ["visio", "windows11", "microsoft-365", "configuration"]
editor: markdown
dateCreated: 2026-10-29T20:57:15Z
dateModified: 2026-10-29T20:57:15Z
---

# Fiche_Simple_-_VM_Windows_11_Visio_Configurer

- **Environnement** : Poste Windows 11 x64 d'un utilisateur ou administrateur (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; version Visio à vérifier auprès de l'éditeur
- **Catégorie** : outil de diagrammes / poste de travail
- **Tags** : `visio`, `windows11`, `microsoft-365`, `configuration`

---

## Problème précis à résoudre

Configurer licence, modèles et options de Visio.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir Visio puis **Fichier > Compte** et se connecter avec UTILISATEUR (licence Plan 2).
   👉 Explication : l'activation se fait par le compte ; plus de clé.

2. Vérifier l'état de licence. PowerShell (perpétuel uniquement) :
```powershell
cd 'C:\Program Files\Microsoft Office\Office16'
cscript ospp.vbs /dstatus
```
   👉 Explication : non applicable aux abonnements ; indique l'état d'activation en volume.

3. Définir les emplacements de modèles et de formes : GUI **Fichier > Options > Avancé > Chemins d'accès aux fichiers**, vers PARTAGE_MODELES (à remplacer).
   👉 Explication : centralise les stencils d'équipe.

4. Configurer l'enregistrement : GUI **Fichier > Options > Enregistrer** : format .vsdx, enregistrement automatique actif.
   👉 Explication : limite la perte de données.

## 2. Production — Contrôles

- Documenter les options retenues.
- Déployer via GPO ou Intune si possible.

## 3. Production — Sécurité

- Interdire les macros non signées : GUI **Options > Centre de gestion de la confidentialité**.

## Validation et retour arrière

- **Validation** : Compte connecté, modèles accessibles.
- **Retour arrière** : Réinitialiser les options ou déconnecter le compte via **Fichier > Compte**.

## Si le problème n'est pas résolu

- [Microsoft — Office Deployment Tool](https://learn.microsoft.com/fr-fr/deployoffice/overview-office-deployment-tool)
- [Microsoft — Visio, plans et tarifs](https://www.microsoft.com/fr-fr/microsoft-365/visio/compare-visio-options)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-microsoft-visio)
- [Alternative draw.io : fiche d'entrée](/01-fiches-simples/logiciels/15-topologie-ipam-et-outils-metiers/fiche-logiciel-draw-io-desktop)
- [Alternative draw.io : installation (Debian 13)](/01-fiches-simples/debian/13/vie-du-logiciel/draw-io/fiche-simple-vm-debian-13-draw-io-installer)