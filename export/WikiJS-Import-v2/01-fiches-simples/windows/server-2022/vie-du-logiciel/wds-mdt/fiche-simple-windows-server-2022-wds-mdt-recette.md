---
title: "Fiche Simple - Windows Server 2022 WDS MDT Recette"
description: "Recetter le service de déploiement après installation, changement ou restauration. L'installation est décrite dans la [procédure historique WDS + MDT](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/FicheSimple-WDS-MDT.md)."
published: true
date: 2026-10-29T20:39:58Z
tags: ["windows-server-2022", "wds", "mdt", "recette", "validation"]
editor: markdown
dateCreated: 2026-10-29T20:39:58Z
dateModified: 2026-10-29T20:39:58Z
---

# Fiche_Simple_-_Windows_Server_2022_WDS_MDT_Recette

- **Environnement** : Windows Server 2022, WDS + MDT installés et configurés selon la procédure historique; poste ou VM de test
- **OS / Version** : Windows Server 2022; WDS, MDT : vérifier la version publiée
- **Catégorie** : Automatisation, déploiement et IaC
- **Tags** : `windows-server-2022`, `wds`, `mdt`, `recette`, `validation`

---

## Problème précis à résoudre

Recetter le service de déploiement après installation, changement ou restauration. L'installation est décrite dans la [procédure historique WDS + MDT](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-simple-wds-mdt).

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les services. GUI : `services.msc`.
   ```powershell
   Get-Service WDSServer, LanmanServer | Select-Object Name, Status
   ```
   👉 Explication : les deux services doivent être `Running`.

2. Contrôler les images publiées :
   ```powershell
   wdsutil /Get-AllImages /Show:Boot
   Get-ChildItem "D:\DeploymentShare$\Boot"
   ```
   👉 Explication : `D:\DeploymentShare$` à remplacer. L'image de démarrage MDT doit figurer dans WDS et dans le dossier `Boot`. La syntaxe de `wdsutil` est à vérifier avec `wdsutil /?`.

3. Contrôler le partage :
   ```powershell
   Get-SmbShare -Name "DeploymentShare$"
   Test-Path "\\SERVEUR-DEPLOIEMENT\DeploymentShare$\Control\Bootstrap.ini"
   ```
   👉 Explication : remplacer `SERVEUR-DEPLOIEMENT`; doit renvoyer `True` depuis un poste autorisé.

4. Démarrer une VM de test en PXE (touche F12 ou ordre de boot réseau), lancer la séquence de tâches de test.
   👉 Explication : la VM doit obtenir une adresse, charger WinPE, se connecter au partage, installer et rejoindre le domaine si prévu.

5. Consulter les journaux côté serveur :
   ```powershell
   Get-WinEvent -LogName "Microsoft-Windows-Deployment-Services-Diagnostics/Admin" -MaxEvents 20 -ErrorAction SilentlyContinue
   ```
   👉 Explication : le nom exact du journal est à vérifier sur la version déployée. Les journaux MDT d'un poste sont dans `C:\MININT\SMSOSD\OSDLOGS` (à vérifier).

## 2. Production — Contrôles

Rejouer le test sur un poste pilote réel; consigner image, séquence et résultat; conserver la VM de test.

## 3. Production — Sécurité

- Recette sur un VLAN de test ou un poste non sensible; aucun secret dans les captures ou journaux joints.

## Validation et retour arrière

- **Validation** : services actifs, image de démarrage publiée, partage accessible, installation complète sur la VM de test.
- **Retour arrière** : supprimer la VM de test et son enregistrement dans WDS/AD; aucune modification serveur n'est requise.

## Si le problème n'est pas résolu

- [Procédure historique WDS + MDT](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-simple-wds-mdt)
- [Fiche d'entrée WDS/MDT](/01-fiches-simples/logiciels/09-automatisation-deploiement-et-iac/fiche-logiciel-wds-mdt)
- [Microsoft Learn — wdsutil](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/wdsutil)
- [Microsoft Learn — Démarrer avec MDT](https://learn.microsoft.com/en-us/windows/deployment/deploy-windows-mdt/get-started-with-the-microsoft-deployment-toolkit)