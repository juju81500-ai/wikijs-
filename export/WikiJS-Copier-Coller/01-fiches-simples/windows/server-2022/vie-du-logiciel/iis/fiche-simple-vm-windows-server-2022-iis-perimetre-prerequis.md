# Fiche_Simple_-_VM_Windows_Server_2022_IIS_Perimetre_Prerequis.md

- **Environnement** : VM Windows Server 2022 pilote
- **OS / Version** : Windows Server 2022; rôle Web Server (IIS)
- **Catégorie** : serveur Web / IIS

---

## Problème précis à résoudre

Confirmer que le serveur est prêt avant d'installer IIS.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier la version : **Paramètres > Système > À propos de** (ou la commande ci-dessous).
   👉 Explication : Windows Server 2022 doit être à jour.

2. Dans PowerShell élevé, contrôler version et mises à jour récentes :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName, WindowsVersion, OsBuildNumber
   Get-HotFix | Sort-Object InstalledOn -Descending | Select-Object -First 5
   ```
   👉 Explication : on confirme le niveau de correctifs.

3. Confirmer nom DNS, certificat prévu, pare-feu administré, sauvegarde de la VM et plan de changement; lister les seuls modules IIS nécessaires à l'application.
   👉 Explication : on évite d'installer des fonctionnalités optionnelles sans revue.

## 2. Production — Contrôles

Cette étape n'installe ni runtime, ni base, ni reverse proxy, ni cluster Web Farm, ni AD CS.

## 3. Production — Sécurité

- Accès administrateur approuvé uniquement.

## Validation et retour arrière

- **Validation** : Prérequis confirmés par écrit.
- **Retour arrière** : Aucune modification; rien à annuler.

## Si le problème n'est pas résolu

- [Microsoft Learn — documentation IIS](https://learn.microsoft.com/en-us/iis/)
- [Microsoft Learn — AppCmd.exe](https://learn.microsoft.com/en-us/iis/get-started/getting-started-with-iis/getting-started-with-appcmdexe)
- [Guide complet installation IIS Windows Server 2022](/02-fiches-completes/windows/server-2022/installation-deploiement/122-installation-iis-windows-server-2022#1-perimetre-et-prerequis)