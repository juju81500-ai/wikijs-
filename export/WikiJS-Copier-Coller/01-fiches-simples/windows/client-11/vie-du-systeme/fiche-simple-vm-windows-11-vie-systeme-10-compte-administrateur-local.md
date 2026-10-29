# Fiche_Simple_-_VM_Windows_11_Vie_Systeme_10_Compte_Administrateur_Local

- **Environnement** : PC Windows 11 (poste de travail)
- **OS / Version** : Windows 11; étape 10 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie

---

## Problème précis à résoudre

Gérer le compte administrateur local intégré et son mot de passe unique par poste (LAPS).

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler les comptes locaux : **Gestion de l'ordinateur (compmgmt.msc) > Utilisateurs et groupes locaux > Utilisateurs**.
   ```powershell
   Get-LocalUser | Select-Object Name,Enabled,PasswordLastSet
   Get-LocalGroupMember -Group 'Administrateurs'
   ```
   👉 Explication : liste les comptes, leur état et les membres du groupe Administrateurs.

2. Désactiver ou renommer le compte `Administrateur` intégré si LAPS n'est pas utilisé.
   ```powershell
   Rename-LocalUser -Name 'Administrateur' -NewName 'ADMIN_LOCAL'
   Disable-LocalUser -Name 'Guest'
   ```
   👉 Explication : réduit la surface d'attaque (`ADMIN_LOCAL` est le nom choisi par la DSI); le compte Invité reste désactivé.

3. Activer Windows LAPS (intégré à Windows) : **GPO > Configuration ordinateur > Modèles d'administration > Système > LAPS**, ou profil Intune « Windows LAPS ».
   ```powershell
   Get-Command -Module LAPS
   Invoke-LapsPolicyProcessing
   Get-LapsDiagnostics
   ```
   👉 Explication : vérifie la disponibilité du module LAPS, applique la stratégie et fournit les journaux de diagnostic.

4. Lire le mot de passe géré (administrateur habilité) : **Entra ID > Appareils > poste > Mot de passe de l'administrateur local** ou en AD :
   ```powershell
   Get-LapsADPassword -Identity 'NOM_POSTE' -AsPlainText
   ```
   👉 Explication : récupère le mot de passe LAPS depuis l'annuaire; accès tracé et réservé.

## 2. Production — Contrôles

Un mot de passe différent par poste, changé automatiquement (30 jours par défaut) et après chaque utilisation.

## 3. Production — Sécurité

Jamais de mot de passe local commun inscrit dans une image ou une fiche; restreindre qui peut lire LAPS.

## Validation et retour arrière

- **Validation** : `Get-LapsDiagnostics` sans erreur et mot de passe récupérable par l'équipe habilitée.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows 11](/01-fiches-simples/windows/client-11/vie-du-systeme/sommaire-vie-du-systeme-windows-11)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows/)