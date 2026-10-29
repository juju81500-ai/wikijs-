# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_10_Compte_Super_Administrateur

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 10 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-10`

---

## Problème précis à résoudre

Sécuriser le compte Administrateur local initial.

## 1. Hors-Production (Lab / Test / POC)

1. Définir le mot de passe lors de l'installation (écran **Paramètres personnalisés**). Pour le modifier ensuite : **Gestion de l'ordinateur > Utilisateurs et groupes locaux > Utilisateurs > Administrateur > Définir le mot de passe**.
   ```powershell
   $p = Read-Host 'Nouveau mot de passe' -AsSecureString
   Set-LocalUser -Name Administrateur -Password $p
   ```
   👉 Explication : le mot de passe est saisi sans écho et n'apparaît pas dans l'historique; `Administrateur` devient `Administrator` sur une édition anglaise.

2. Renommer le compte intégré (**Stratégie de sécurité locale > Stratégies locales > Options de sécurité > Comptes : renommer le compte Administrateur**) :
   ```powershell
   Rename-LocalUser -Name Administrateur -NewName ADMIN_LOCAL
   ```
   👉 Explication : `ADMIN_LOCAL` est un nom non évident défini par l'organisation.

3. Contrôler l'état et le dernier changement de mot de passe :
   ```powershell
   Get-LocalUser | Select-Object Name, Enabled, PasswordLastSet, LastLogon
   ```
   👉 Explication : repère les comptes actifs et inutilisés.

## 2. Production — Contrôles

Stocker le mot de passe dans le coffre de l'organisation; utiliser **Windows LAPS** une fois le serveur joint au domaine.

## 3. Production — Sécurité

Mot de passe long et unique; ne jamais utiliser le compte intégré pour l'administration quotidienne.

## Validation et retour arrière

- **Validation** : Connexion testée avec le mot de passe puis refus de l'ancien.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2022](./Sommaire_-_Vie_du_systeme_Windows_Server_2022.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
