# Fiche_Simple_-_VM_Windows_Server_2025_Vie_Systeme_38_Isolation_Des_Comptes_De

- **Environnement** : Serveur Windows Server 2025
- **OS / Version** : Windows Server 2025; étape 38 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2025`, `vie-du-systeme`, `cycle-de-vie`, `etape-38`

---

## Problème précis à résoudre

Utiliser des comptes de service dédiés (gMSA).

## 1. Hors-Production (Lab / Test / POC)

1. Dans le domaine, créer un compte de service administré de groupe (**Utilisateurs et ordinateurs Active Directory > Managed Service Accounts**). D'abord la clé racine KDS (une seule fois par forêt) :
   ```powershell
   Add-KdsRootKey -EffectiveTime ((Get-Date).AddHours(-10))
   New-ADServiceAccount -Name GMSA_APP -DNSHostName GMSA_APP.EXEMPLE.LOCAL -PrincipalsAllowedToRetrieveManagedPassword GROUPE_SERVEURS
   ```
   👉 Explication : `GMSA_APP` est le nom du compte; l'effet horaire immédiat s'utilise en laboratoire seulement.

2. Installer et tester sur le serveur :
   ```powershell
   Install-ADServiceAccount GMSA_APP
   Test-ADServiceAccount GMSA_APP
   ```
   👉 Explication : renvoie `True` si le serveur peut récupérer le mot de passe géré.

3. Configurer le service pour utiliser `EXEMPLE\GMSA_APP$` (**services.msc > Propriétés > Connexion**) sans mot de passe.
   👉 Explication : le mot de passe est renouvelé automatiquement.

## 2. Production — Contrôles

Un compte de service par application, sans droit interactif.

## 3. Production — Sécurité

Ne jamais utiliser un compte d'administrateur pour un service.

## Validation et retour arrière

- **Validation** : Le service démarre avec le gMSA.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](../../../../00-Administration/Vie_du_systeme.md)
- [Sommaire Windows Server 2025](./Sommaire_-_Vie_du_systeme_Windows_Server_2025.md)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)
