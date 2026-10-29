---
title: "Fiche Simple - VM Windows Server 2022 Systeme Sysprep Modele"
description: "Préparer une VM Windows Server 2022 propre, puis la généraliser avec Sysprep pour en faire un modèle de référence réutilisable : chaque copie reçoit alors un SID, un nom et une configuration de premier démarrage distincts."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[windows-server-2022]", "[sysprep]", "[template]", "[dism]", "[hyper-v]", "[powershell]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Systeme_Sysprep_Modele

- **Environnement** : VM (Windows Server 2022, serveur modèle destiné au clonage)
- **OS / Version** : Windows Server 2022 - Famille Windows Server
- **Catégorie** : Système & Services / Images et modèles
- **Tags** : `[windows-server-2022]`, `[sysprep]`, `[template]`, `[dism]`, `[hyper-v]`, `[powershell]`

## 🎯 Problème précis à résoudre
Préparer une VM Windows Server 2022 propre, puis la généraliser avec Sysprep pour en faire un modèle de référence réutilisable : chaque copie reçoit alors un SID, un nom et une configuration de premier démarrage distincts.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Nettoyer les composants et fichiers temporaires avant la capture :
   ```powershell
   Dism.exe /Online /Cleanup-Image /StartComponentCleanup
   Remove-Item -Path "$env:TEMP\*" -Recurse -Force -ErrorAction SilentlyContinue
   ```
   👉 Explication : Réduit la taille du modèle en supprimant les anciennes versions de composants et les fichiers temporaires de la session.
2. Vider les journaux Application et System pour repartir d'un état propre :
   ```powershell
   wevtutil cl Application
   wevtutil cl System
   ```
   👉 Explication : Évite de copier l'historique du modèle dans chaque clone. Ne pas vider le journal Sécurité avant une conservation légale.
3. Lancer Sysprep en mode généralisation avec arrêt de la machine :
   ```powershell
   Start-Process -FilePath "C:\Windows\System32\Sysprep\sysprep.exe" -ArgumentList "/generalize /oobe /shutdown" -Wait
   ```
   👉 Explication : Supprime le SID et les paramètres propres au poste, relance l'expérience de premier démarrage (OOBE), puis éteint la VM. Ne pas redémarrer la VM après cette étape.

**Équivalent interface graphique :**

- **Win + R** > `C:\Windows\System32\Sysprep\sysprep.exe`, cocher **Generalize**, **Enter System Out-of-Box Experience (OOBE)**, **Shutdown**, **OK**.
  👉 Explication : équivalent de la commande Sysprep; snapshot de la VM avant.
- **Observateur d'événements** (`eventvwr.msc`) > clic droit sur **Application** / **System** > **Effacer le journal**.
  👉 Explication : équivalent de `wevtutil cl`.

## ⚡ 2. Production — Façon Simplifiée
1. Sysprep avec fichier de réponses (unattend) pour automatiser le premier démarrage :
   ```powershell
   Start-Process -FilePath "C:\Windows\System32\Sysprep\sysprep.exe" -ArgumentList "/generalize /oobe /shutdown /unattend:C:\Windows\Panther\unattend.xml" -Wait
   ```
   👉 Explication : Le fichier `unattend.xml` doit exister à l'emplacement indiqué, sinon Sysprep échoue. Il définit la langue, le fuseau et le compte administrateur du premier démarrage.
2. Capturer la VM modèle dans l'hyperviseur (exécuter sur l'hôte Hyper-V) :
   ```powershell
   Checkpoint-VM -Name "<nom_vm_modele>" -SnapshotName "01-CLEAN-INSTALL"
   ```
   👉 Explication : Conserve un point de restauration nommé selon la convention du cycle de vie, à utiliser avant toute nouvelle généralisation.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Vérifier l'empreinte du disque modèle avant diffusion :
   ```powershell
   Get-FileHash -Algorithm SHA256 -Path "<chemin_disque_modele>"
   ```
   👉 Explication : Permet de contrôler l'intégrité du modèle avant de le copier vers d'autres hyperviseurs, et de comparer deux versions.
2. Après un échec de Sysprep sur une VM de test, lire le journal de Sysprep :
   ```powershell
   Get-Content -Path "C:\Windows\System32\Sysprep\Panther\setupact.log" -Tail 30
   ```
   👉 Explication : Le fichier `setupact.log` indique la cause de l'échec (application non conforme, fichier de réponses invalide, etc.). Corriger la cause sur une copie du modèle, jamais sur le modèle de référence.
3. Consigner la version du modèle et son état après généralisation :
   ```powershell
   Get-ComputerInfo -Property WindowsProductName, WindowsVersion, OsBuildNumber
   ```
   👉 Explication : Note la version de Windows et le build dans la documentation de la version du modèle. Cette information est nécessaire pour les mises à jour et les audits.