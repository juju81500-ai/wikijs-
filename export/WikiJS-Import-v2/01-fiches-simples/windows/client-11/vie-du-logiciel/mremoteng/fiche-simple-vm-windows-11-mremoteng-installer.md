---
title: "Fiche Simple - VM Windows 11 mRemoteNG Installer"
description: "Installer mRemoteNG sur Windows 11."
published: true
date: 2026-10-29T20:39:58Z
tags: ["mremoteng", "windows11", "installation", "winget"]
editor: markdown
dateCreated: 2026-10-29T20:39:58Z
dateModified: 2026-10-29T20:39:58Z
---

# Fiche_Simple_-_VM_Windows_11_mRemoteNG_Installer

- **Environnement** : Poste Windows 11 x64 d'administration (VM de test puis poste pilote)
- **OS / Version** : Windows 11 x64; mRemoteNG VERSION_MREMOTENG (à remplacer)
- **Catégorie** : gestionnaire de connexions distantes
- **Tags** : `mremoteng`, `windows11`, `installation`, `winget`

---

## Problème précis à résoudre

Installer mRemoteNG sur Windows 11.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger le MSI/installateur de VERSION_MREMOTENG (à remplacer) depuis la page Releases GitHub.
   👉 Explication : source officielle.

2. GUI : exécuter l'installateur, suivre l'assistant, choisir le dossier d'installation.
   👉 Explication : installation de référence.

3. Dans PowerShell, chercher le nom exact : `winget search "mRemoteNG" --source winget`. Relever l'ID exact affiché (colonne Id) et le noter comme ID_PAQUET_VERIFIE (à remplacer ; ne jamais le deviner). Puis, ID vérifié seulement : `winget install --id ID_PAQUET_VERIFIE --exact --source winget`.
   👉 Explication : l'ID du paquet doit venir du catalogue réel de la machine ; il n'a pas pu être vérifié lors de la rédaction de cette fiche.

4. Option : version portable dans `C:\Outils\mRemoteNG\` (à remplacer).
   👉 Explication : utile pour test sans droits administrateur.

5. Lancer mRemoteNG puis **Help > About mRemoteNG**.
   👉 Explication : affiche la version installée.

## 2. Production — Contrôles

Installer d'abord sur le poste pilote et consigner version et hash.

## 3. Production — Sécurité

- `Get-FileHash .\FICHIER_INSTALLATEUR -Algorithm SHA256` puis comparer avec la valeur publiée si disponible (FICHIER_INSTALLATEUR à remplacer).
- `Get-AuthenticodeSignature` sur l'exécutable.

## Validation et retour arrière

- **Validation** : L'application démarre et la version affichée correspond.
- **Retour arrière** : **Paramètres > Applications** > désinstaller, ou `winget uninstall --id ID_PAQUET_VERIFIE`.

## Si le problème n'est pas résolu

- Tous les éléments en MAJUSCULES sont des placeholders **à remplacer** ; ne jamais saisir de vrais secrets dans une fiche ou un ticket.
- [mRemoteNG — documentation officielle](https://mremoteng.readthedocs.io/en/latest/)
- [mRemoteNG — dépôt et releases](https://github.com/mRemoteNG/mRemoteNG/releases)
- [mRemoteNG — site officiel](https://mremoteng.org/)