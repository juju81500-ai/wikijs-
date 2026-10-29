# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_02_Recuperation_De_L_Image

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 02 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Obtenir l'image officielle de Windows 11 depuis la source Microsoft ou le catalogue interne.

## 1. Hors-Production (Lab / Test / POC)

1. Télécharger l'outil de création de média (Media Creation Tool) depuis le site officiel Microsoft (page « Télécharger Windows 11 »), puis l'exécuter : **Créer un support d'installation > Fichier ISO**.
   ```powershell
   $Dossier = 'C:\ISO'
   New-Item -ItemType Directory -Path $Dossier -Force | Out-Null
   Start-Process -FilePath "$env:USERPROFILE\Downloads\MediaCreationTool.exe"
   ```
   👉 Explication : crée le dossier de stockage et lance l'outil; l'assistant propose ensuite d'enregistrer le fichier ISO (langue, édition et architecture à choisir).

2. Variante entreprise : récupérer l'ISO via le **Centre de gestion des licences en volume (VLSC)** ou le **Centre d'administration Microsoft 365**, selon le contrat.
   👉 Explication : ces sources fournissent les éditions Entreprise ou Pro avec la clé du contrat; ne pas utiliser de site tiers.

3. Ranger l'image dans le stockage ISO de l'hyperviseur ou le partage de déploiement interne (par exemple `\\SERVEUR\ISO`, où SERVEUR est le serveur de fichiers).
   ```powershell
   Copy-Item 'C:\ISO\Win11_FR.iso' '\\SERVEUR\ISO\' -Verbose
   ```
   👉 Explication : l'image devient disponible pour la création du support ou de la VM.

4. Consigner la version (par exemple 24H2) et l'édition dans le dossier du projet.
   👉 Explication : garantit que tous les postes sont installés avec la même version.

## 2. Production — Contrôles

Utiliser uniquement l'ISO officielle ou le miroir interne approuvé et horodaté.

## 3. Production — Sécurité

Ne jamais utiliser une ISO tierce (« allégée », pré-activée) : risque de logiciel malveillant.

## Validation et retour arrière

- **Validation** : Fichier `.iso` présent et taille cohérente (`Get-Item C:\ISO\*.iso | Select-Object Name,Length`).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/sommaire-vie-du-systeme-windows-11)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)