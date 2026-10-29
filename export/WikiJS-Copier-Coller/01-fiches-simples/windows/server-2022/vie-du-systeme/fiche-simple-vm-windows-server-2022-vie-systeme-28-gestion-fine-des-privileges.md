# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_28_Gestion_Fine_Des_Privileges

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 28 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Appliquer le moindre privilège (équivalent sudo).

## 1. Hors-Production (Lab / Test / POC)

1. Utiliser des groupes dédiés (**Gestion de l'ordinateur > Utilisateurs et groupes locaux > Groupes**) plutôt que d'ajouter tout le monde à Administrateurs :
   ```powershell
   New-LocalGroup -Name 'Admins-Sauvegarde' -Description 'Opérateurs de sauvegarde'
   Add-LocalGroupMember -Group 'Opérateurs de sauvegarde' -Member ADMIN_NOMINATIF
   ```
   👉 Explication : le groupe intégré `Opérateurs de sauvegarde` (Backup Operators) délègue la sauvegarde sans droits complets.

2. Déléguer l'administration à distance de PowerShell via JEA (Just Enough Administration) :
   ```powershell
   New-PSSessionConfigurationFile -Path C:\JEA\Operateur.pssc -SessionType RestrictedRemoteServer -VisibleCmdlets 'Restart-Service','Get-Service'
   Register-PSSessionConfiguration -Name Operateur -Path C:\JEA\Operateur.pssc
   ```
   👉 Explication : crée un point d'accès limité aux cmdlets listées (`C:\JEA` doit exister).

3. Auditer les privilèges d'un compte :
   ```powershell
   whoami /priv
   whoami /groups
   ```
   👉 Explication : liste les privilèges et groupes du jeton courant.

## 2. Production — Contrôles

Revoir trimestriellement les membres des groupes privilégiés.

## 3. Production — Sécurité

Élévation à la demande (UAC) et aucun compte partagé.

## Validation et retour arrière

- **Validation** : Un opérateur exécute uniquement les actions autorisées.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2022](/01-fiches-simples/windows/server-2022/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2022)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)