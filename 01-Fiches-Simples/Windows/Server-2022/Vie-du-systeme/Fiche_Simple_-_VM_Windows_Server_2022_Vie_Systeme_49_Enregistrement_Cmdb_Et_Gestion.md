# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_49_Enregistrement_Cmdb_Et_Gestion

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 49 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-49`

---

## Problème précis à résoudre

Déclarer le serveur dans l'inventaire.

## 1. Hors-Production (Lab / Test / POC)

1. Collecter les informations à saisir dans la CMDB :
   ```powershell
   Get-ComputerInfo | Select-Object CsName, CsDomain, WindowsProductName, OsVersion, BiosSeralNumber
   Get-NetIPConfiguration | Select-Object InterfaceAlias, IPv4Address
   ```
   👉 Explication : nom, domaine, version, numéro de série et adresse IP.

2. Lister les comptes administrateurs à déclarer :
   ```powershell
   Get-LocalGroupMember -Group Administrateurs
   ```
   👉 Explication : identifie les personnes ayant un accès privilégié.

3. Renseigner dans la CMDB : propriétaire, criticité, rôle, emplacement, dates de licence et d'expiration, lien vers le runbook.
   👉 Explication : la CMDB devient la source de vérité pour le support et l'audit.

## 2. Production — Contrôles

Mettre à jour la CMDB à chaque changement via la gestion des changements.

## 3. Production — Sécurité

Restreindre l'accès à la CMDB; ne jamais y enregistrer de mot de passe.

## Validation et retour arrière

- **Validation** : Fiche CMDB complète et approuvée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2022](./Sommaire_-_Vie_du_systeme_Windows_Server_2022.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
