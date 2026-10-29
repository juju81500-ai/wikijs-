# Fiche_Simple_-_Windows_Server_2022_MECM_Mise_a_jour_Retour_arriere

- **Environnement** : Windows Server 2022, site primaire MECM/SCCM, accès aux mises à jour du service
- **OS / Version** : Windows Server 2022; Configuration Manager current branch : vérifier la version publiée
- **Catégorie** : Automatisation, déploiement et IaC
- **Tags** : `windows-server-2022`, `mecm`, `sccm`, `mise-a-jour`, `retour-arriere`

---

## Problème précis à résoudre

Appliquer une mise à jour de Configuration Manager et savoir comment revenir en arrière : il n'existe pas de désinstallation d'une mise à jour in-console, le retour se fait par restauration.

## 1. Hors-Production (Lab / Test / POC)

1. Lister les mises à jour disponibles. GUI : `Administration > Services cloud > Mises à jour et maintenance`.
   ```powershell
   $CodeSite = "CODESITE"
   Get-CimInstance -Namespace "root\SMS\site_$CodeSite" -ClassName SMS_CM_UpdatePackages | Select-Object Name, FullVersion, State
   ```
   👉 Explication : `CODESITE` est à remplacer; la valeur de `State` est à interpréter avec la documentation (WMI). Sur le lab, `Rechercher les mises à jour` actualise la liste.

2. Lancer le contrôle de prérequis de la mise à jour. GUI : clic droit sur la mise à jour, `Exécuter la vérification des prérequis`.
   👉 Explication : consulter les résultats dans `Surveillance > Mises à jour et maintenance`; corriger les alertes avant l'installation.

3. Installer la mise à jour dans le lab. GUI : clic droit, `Installer le pack de mise à jour`.
   👉 Explication : suivre `<dossier d'installation>\Logs\CMUpdate.log`. Le site se met à jour; les clients, ensuite, sur une collection pilote avant généralisation (`Mise à niveau du client`).

4. Contrôler la version atteinte :
   ```powershell
   Get-CimInstance -Namespace "root\SMS\site_$CodeSite" -ClassName SMS_Site | Select-Object SiteCode, Version
   ```
   👉 Explication : la version doit correspondre à celle de la mise à jour publiée.

## 2. Production — Contrôles

Avant production : sauvegarde de site et de SQL récente (fiche Sauvegarde/Restauration), fenêtre de maintenance, version validée en lab, lecture des notes de version. Vérifier la compatibilité des versions client, ADK et SQL.

## 3. Production — Sécurité

- Mises à jour provenant exclusivement de la console (service Microsoft); pas de binaires tiers.
- Conserver la sauvegarde d'avant mise à jour jusqu'à la clôture de la recette.

## Validation et retour arrière

- **Validation** : version attendue, composants sains, clients pilote mis à jour, recette rejouée.
- **Retour arrière** : pas de désinstallation de mise à jour; restaurer le site depuis la sauvegarde d'avant mise à jour (`setup.exe` > `Recover a site`) ou la VM et la base SQL ensemble (même instant). Les clients déjà mis à niveau sont à traiter selon la documentation.

## Si le problème n'est pas résolu

- [Fiche d'entrée MECM/SCCM](../../../../Logiciels/09-Automatisation-deploiement-et-IaC/Fiche_Logiciel_-_Microsoft-MECM-SCCM.md)
- [Microsoft Learn — Mises à jour pour Configuration Manager](https://learn.microsoft.com/en-us/intune/configmgr/core/servers/manage/updates)
- [Microsoft Learn — Sauvegarde et récupération](https://learn.microsoft.com/en-us/intune/configmgr/core/servers/manage/backup-and-recovery)
