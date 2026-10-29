# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_11_Compte_D_Administration_Delegue

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 11 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-11`

---

## Problème précis à résoudre

Créer un compte nominatif pour l'administration quotidienne.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Gestion de l'ordinateur > Utilisateurs et groupes locaux > Utilisateurs > Action > Nouvel utilisateur**.
   ```powershell
   $p = Read-Host 'Mot de passe' -AsSecureString
   New-LocalUser -Name ADMIN_NOMINATIF -Password $p -FullName 'Prénom Nom' -Description 'Administrateur nominatif'
   ```
   👉 Explication : `ADMIN_NOMINATIF` est l'identifiant du technicien.

2. Ajouter au groupe **Administrateurs** (**Propriétés > Membre de > Ajouter**) :
   ```powershell
   Add-LocalGroupMember -Group Administrateurs -Member ADMIN_NOMINATIF
   ```
   👉 Explication : donne les droits d'administration à un compte traçable; le groupe se nomme `Administrators` sur une édition anglaise.

3. Contrôler les membres :
   ```powershell
   Get-LocalGroupMember -Group Administrateurs
   ```
   👉 Explication : liste les comptes privilégiés à justifier.

## 2. Production — Contrôles

Après jonction au domaine, utiliser des groupes de domaine dédiés plutôt que des comptes locaux.

## 3. Production — Sécurité

Principe du moindre privilège : un compte nominatif, pas de compte partagé.

## Validation et retour arrière

- **Validation** : Ouverture de session réussie et droits administrateur confirmés (`whoami /groups`).
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2022](./Sommaire_-_Vie_du_systeme_Windows_Server_2022.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
