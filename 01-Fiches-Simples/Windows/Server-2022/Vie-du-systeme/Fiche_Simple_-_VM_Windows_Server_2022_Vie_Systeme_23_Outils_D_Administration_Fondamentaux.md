# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_23_Outils_D_Administration_Fondamentaux

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 23 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-23`

---

## Problème précis à résoudre

Installer les outils d'administration et de diagnostic.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Gestionnaire de serveur > Gérer > Ajouter des rôles et fonctionnalités > Fonctionnalités**, ou installer **Windows Terminal** et **RSAT** sur le poste d'administration.
   ```powershell
   Install-WindowsFeature -Name Telnet-Client,RSAT-AD-Tools -IncludeManagementTools
   ```
   👉 Explication : ajoute des outils de test et d'administration AD (le client Telnet n'est qu'un exemple de test à retirer ensuite).

2. Installer des outils via `winget` (si disponible) :
   ```powershell
   winget install --id Microsoft.Sysinternals.Suite -e
   ```
   👉 Explication : installe la suite Sysinternals (Process Explorer, Autoruns); vérifier la disponibilité de `winget` sur l'édition.

3. Mettre à jour l'aide PowerShell :
   ```powershell
   Update-Help -Force -ErrorAction SilentlyContinue
   ```
   👉 Explication : télécharge l'aide en ligne locale.

## 2. Production — Contrôles

Limiter les outils au strict nécessaire; préférer l'administration à distance depuis un poste dédié.

## 3. Production — Sécurité

Chaque outil installé augmente la surface d'attaque : retirer les outils de test après usage.

## Validation et retour arrière

- **Validation** : Les outils répondent (`Get-Command`).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2022](./Sommaire_-_Vie_du_systeme_Windows_Server_2022.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
