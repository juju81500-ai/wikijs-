# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_02_Recuperation_De_L_Image

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 02 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Obtenir l'image officielle de Windows Server 2022.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'ISO d'évaluation ou l'ISO sous contrat depuis le **Centre d'évaluation Microsoft** (https://www.microsoft.com/fr-fr/evalcenter/) ou le **Centre d'administration Microsoft 365 / Volume Licensing Service Center** selon le contrat :
   ```powershell
   New-Item -ItemType Directory -Path C:\ISO -Force
   # Après téléchargement par le navigateur, vérifier la présence du fichier :
   Get-ChildItem C:\ISO\*.iso | Select-Object Name, @{n='Taille_Go';e={[math]::Round($_.Length/1GB,2)}}
   ```
   👉 Explication : crée le dossier d'accueil et confirme que l'image est présente avec une taille cohérente.

2. Ranger l'image dans la bibliothèque de l'hyperviseur (Hyper-V : **Gestionnaire Hyper-V > Paramètres de la VM > Contrôleur SCSI/IDE > Lecteur de DVD > Fichier image** ; Proxmox : **Datacenter > Stockage > ISO Images > Upload**).
   👉 Explication : l'image devient sélectionnable à la création de la VM.

## 2. Production — Contrôles

Utiliser uniquement les sources officielles ou la bibliothèque interne approuvée; l'édition d'évaluation est limitée dans le temps.

## 3. Production — Sécurité

Ne jamais utiliser une image tierce, « pré-activée » ou non vérifiée.

## Validation et retour arrière

- **Validation** : Fichier `.iso` présent, taille cohérente et édition conforme à la licence achetée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2022](/01-fiches-simples/windows/server-2022/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2022)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)