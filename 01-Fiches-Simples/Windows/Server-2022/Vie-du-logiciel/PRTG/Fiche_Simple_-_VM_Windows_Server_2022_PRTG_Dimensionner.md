# Fiche_Simple_-_VM_Windows_Server_2022_PRTG_Dimensionner.md

- **Environnement** : Serveur Windows dédié ou VM, accès d'administration restreint
- **OS / Version** : Windows Server 2022 ou 2025 en Desktop Experience; PRTG Network Monitor maintenu
- **Catégorie** : supervision / SNMP / WMI
- **Tags** : `prtg`, `windows-server`, `supervision`, `dimensionnement`, `dotnet`

---

## Problème précis à résoudre

Dimensionner le serveur PRTG et vérifier les prérequis avant installation.

## 1. Hors-Production (Lab / Test / POC)

1. Dimensionner selon le nombre de capteurs, intervalles, protocoles et rétention en suivant les tableaux officiels Paessler.
   👉 Explication : le nombre d'équipements seul ne suffit pas.

2. Prévoir un volume de données dédié, une adresse fixe, le DNS et la sauvegarde.
   👉 Explication : la base de supervision grossit avec le temps.

3. Vérifier l'édition de Windows (Desktop Experience requis) :
   ```powershell
   Get-ComputerInfo | Select-Object WindowsProductName,WindowsInstallationType
   ```
   👉 Explication : `Server` doit apparaître comme type d'installation; ne pas installer sur Server Core.

4. Vérifier .NET Framework (4.7.2 minimum, 4.8 recommandé) :
   ```powershell
   (Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full').Release
   ```
   👉 Explication : la valeur 461808 ou plus correspond à .NET 4.7.2 ou supérieur.

5. Pour domaines ou réseaux distants, prévoir des Remote Probes ou Multi-Platform Probe selon la matrice officielle.
   👉 Explication : une sonde locale ne voit pas les réseaux isolés.

## 2. Production — Contrôles

Valider le dimensionnement, la licence et la fenêtre d'installation avec les responsables.

## 3. Production — Sécurité

- Ne pas installer sur Windows Server Core.
- Restreindre l'accès d'administration du serveur.

## Validation et retour arrière

- **Validation** : Édition Windows et .NET conformes; volume de données dédié prévu.
- **Retour arrière** : Aucune modification : rien à annuler.

## Si le problème n'est pas résolu

- [Paessler — Exigences système PRTG](https://www.paessler.com/manuals/prtg/system_requirements)
- [Paessler — Installer le Core Server](https://www.paessler.com/manuals/prtg/install_a_prtg_core_server)
- [Guide complet — dimensionner et préparer](../../../../../02-Fiches-Completes/Windows/Server-2022/Installation-Deploiement/47_Deploiement_PRTG_Network_Monitor_Windows_Server.md#1-dimensionner-et-preparer)
