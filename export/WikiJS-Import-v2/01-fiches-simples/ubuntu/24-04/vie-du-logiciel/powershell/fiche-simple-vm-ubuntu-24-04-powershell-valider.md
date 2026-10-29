---
title: "Fiche Simple - VM Ubuntu 24.04 PowerShell Valider"
description: "Recette de PowerShell 7 : installation, profil, modules, remoting."
published: true
date: 2026-10-29T20:59:00Z
tags: ["ubuntu2404", "powershell", "pwsh", "scripting"]
editor: markdown
dateCreated: 2026-10-29T20:59:00Z
dateModified: 2026-10-29T20:59:00Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_PowerShell_Valider

- **Environnement** : VM Ubuntu 24.04 LTS de laboratoire, accès sudo, dépôt Microsoft officiel
- **OS / Version** : Ubuntu 24.04 LTS
- **Catégorie** : shell / scripting
- **Tags** : `ubuntu2404`, `powershell`, `pwsh`, `scripting`

---

## Problème précis à résoudre

Recette de PowerShell 7 : installation, profil, modules, remoting.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la version et l'édition :
   ```bash
   pwsh -NoLogo -NoProfile -Command '$PSVersionTable | Select-Object PSVersion,PSEdition,OS,Platform'
   ```
   👉 Explication : attendu : édition `Core`, plateforme `Unix`.

2. Contrôler l'origine du paquet :
   ```bash
   apt-cache policy powershell
   ```
   👉 Explication : l'origine doit être Microsoft.

3. Contrôler le chargement du profil et d'un module :
   ```bash
   pwsh -NoLogo -Command 'Get-Module -ListAvailable | Select-Object -First 5 Name,Version'
   ```
   👉 Explication : aucune erreur au démarrage.

4. Tester le remoting SSH depuis un client (HOTE et UTILISATEUR à remplacer) :
   ```powershell
   Invoke-Command -HostName HOTE -UserName UTILISATEUR -ScriptBlock { hostname }
   ```
   👉 Explication : retourne le nom de la machine distante si le sous-système est correct.

## 2. Production — Contrôles

Consigner le résultat de la recette dans le dossier d'exploitation. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Ne pas laisser de transcripts de test contenant des données sensibles.

## Validation et retour arrière

- **Validation** : toutes les commandes répondent sans erreur.
- **Retour arrière** : reprendre la fiche concernée par l'échec (Installer ou Remoting_SSH).

## Si le problème n'est pas résolu

- [Microsoft Learn — installer PowerShell sur Linux](https://learn.microsoft.com/powershell/scripting/install/installing-powershell-on-linux)
- [Microsoft Learn — remoting PowerShell via SSH](https://learn.microsoft.com/powershell/scripting/security/remoting/ssh-remoting-in-powershell)
- [Fiche connexe — Prerequis Limites](/01-fiches-simples/ubuntu/24-04/vie-du-logiciel/powershell/fiche-simple-vm-ubuntu-24-04-powershell-prerequis-limites)