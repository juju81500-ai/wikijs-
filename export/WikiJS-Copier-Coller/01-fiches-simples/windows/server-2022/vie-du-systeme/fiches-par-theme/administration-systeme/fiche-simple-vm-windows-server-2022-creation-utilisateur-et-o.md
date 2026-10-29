# 📄 VM_WinSrv_2022_ADDS_Creation-Utilisateur-Et-OU.md

- **Environnement** : VM (Windows Server 2022 AD DS)
- **OS / Version** : Windows Server 2022 - Famille Windows
- **Catégorie** : Annuaire & Identité / Active Directory

## 🎯 Problème précis à résoudre
Structurer l'annuaire Active Directory en créant une Unité d'Organisation (OU), y ajouter un utilisateur, configurer la réinitialisation de mot de passe à la première connexion et sécuriser le compte selon les règles de complexité d'entreprise.

---

## 🖥️ Méthode Interface Graphique (GUI pas-à-pas)

### Prérequis
- Ouvrir une session avec un compte ayant les droits délégués nécessaires sur l'OU cible ; ne pas utiliser Domain Admin pour les tâches courantes.
- Vérifier le domaine, l'OU de destination et le groupe de sécurité attribués par la procédure d'arrivée de l'organisation.

### Créer et organiser le compte
1. Dans **Gestionnaire de serveur** > **Outils**, ouvrir **Utilisateurs et ordinateurs Active Directory** (`dsa.msc`).
2. Développer le domaine. Pour créer l'OU, faire un clic droit sur le conteneur parent > **Nouveau** > **Unité d'organisation**. Saisir le nom prévu et laisser activée **Protéger le conteneur contre une suppression accidentelle**, puis valider.
3. Sélectionner la nouvelle OU, faire un clic droit > **Nouveau** > **Utilisateur**. Renseigner le prénom, le nom, le nom d'ouverture de session utilisateur et le suffixe UPN vérifié, puis passer à l'écran du mot de passe.
4. Saisir un mot de passe initial fourni par le canal approuvé, cocher **L'utilisateur doit changer le mot de passe à la prochaine ouverture de session**, et laisser le compte activé uniquement si l'arrivée est autorisée. Terminer l'assistant.
5. Ajouter le compte à son groupe de sécurité métier : ouvrir les propriétés de l'utilisateur > **Membre de** > **Ajouter**, saisir le groupe validé (ex. `GRP_TSSR_Techniciens`), cliquer **Vérifier les noms**, puis **OK**. Ne pas ajouter directement des droits applicatifs au compte si le modèle du domaine passe par des groupes.
6. Vérifier l'objet dans l'OU attendue, son UPN et l'onglet **Membre de**. Confirmer l'appartenance et les droits attendus avec le propriétaire du groupe avant de communiquer les identifiants.

Ne pas consigner le mot de passe dans la fiche ou dans un ticket. Si le mauvais compte ou la mauvaise OU a été choisi, arrêter et corriger avant d'activer ou de communiquer l'accès.

Référence : [Microsoft Learn — Utilisateurs et ordinateurs Active Directory](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview).

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Création d'une Unité d'Organisation de test :
   `New-ADOrganizationalUnit -Name "OU_Test" -Path "DC=lab,DC=local"`
   👉 Explication : Crée le dossier d'organisation OU_Test à la racine du domaine lab.local.

2. Création rapide d'un utilisateur de test avec mot de passe simple :
   `New-ADUser -Name "User Test" -SamAccountName "utest" -UserPrincipalName "utest@lab.local" -AccountPassword (ConvertTo-SecureString "Pass1234!" -AsPlainText -Force) -Enabled $true`
   👉 Explication : Crée et active le compte utilisateur utest pour des essais immédiats.

3. Vérification de l'existence du compte :
   `Get-ADUser -Identity "utest"`
   👉 Explication : Affiche les propriétés de base du compte utilisateur créé.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création de l'arborescence d'Unité d'Organisation (OU) de production :
   `New-ADOrganizationalUnit -Name "TSSR_Utilisateurs" -Path "DC=lab,DC=local" -ProtectedFromAccidentalDeletion $true`
   👉 Explication : Crée l'OU TSSR_Utilisateurs et active la protection contre la suppression accidentelle.

2. Création du compte utilisateur standard complet :
   `New-ADUser -Name "Jean Dupont" -GivenName "Jean" -Surname "Dupont" -SamAccountName "jdupont" -UserPrincipalName "jdupont@lab.local" -Path "OU=TSSR_Utilisateurs,DC=lab,DC=local" -AccountPassword (Read-Host -AsSecureString "Entrez le mot de passe initial") -ChangePasswordAtLogon $true -Enabled $true`
   👉 Explication : Crée le compte jdupont dans l'OU ciblée, masque la saisie du mot de passe et force son changement à la première ouverture de session.

3. Ajout de l'utilisateur dans un groupe de sécurité du personnel :
   `Add-ADGroupMember -Identity "GRP_TSSR_Techniciens" -Members "jdupont"`
   👉 Explication : Attribue les droits du groupe GRP_TSSR_Techniciens au nouvel utilisateur.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Création d'un compte d'administration dédié avec séparation des privilèges (Compte Tier-1 / Tier-2) :
   `New-ADUser -Name "ADM Jean Dupont" -SamAccountName "adm-jdupont" -UserPrincipalName "adm-jdupont@lab.local" -Path "OU=TSSR_Admins,DC=lab,DC=local" -AccountPassword (Read-Host -AsSecureString) -CannotChangePassword $false -PasswordNeverExpires $false -Enabled $true`
   👉 Explication : Crée un compte d'administration nommé distinct du compte bureautique standard pour appliquer le principe du moindre privilège.

2. Activation du drapeau de protection Kerberos (Account is sensitive and cannot be delegated) :
   `Set-ADUser -Identity "adm-jdupont" -AccountNotDelegated $true`
   👉 Explication : Empêche la délégation des jetons d'authentification Kerberos du compte admin pour contrecarrer les attaques de type Pass-the-Ticket / Unconstrained Delegation.

3. Ajout du compte au groupe restreint "Protected Users" :
   `Add-ADGroupMember -Identity "Protected Users" -Members "adm-jdupont"`
   👉 Explication : Force l'utilisation d'algorithmes de chiffrement forts (AES), interdit le stockage des hachages NTLM/WDigest et bloque le cache de mots de passe hors-ligne.

4. Activation de l'audit complet des modifications sur le compte utilisateur :
   `Set-ADUser -Identity "jdupont" -SmartcardLogonRequired $false`
   👉 Explication : Applique les politiques de contrôle de sécurité strictes du domaine sur l'objet AD.