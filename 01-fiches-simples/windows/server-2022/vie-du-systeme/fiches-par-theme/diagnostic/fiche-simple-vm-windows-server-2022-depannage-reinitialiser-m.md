# 📄 VM_WinSrv_2022_Depannage_Reinitialiser-Mot-De-Passe-Local.md

- **Environnement** : VM / Physique (Windows Server 2022)
- **OS / Version** : Windows Server 2022 - Famille Windows Server
- **Catégorie** : Dépannage & Administration / Identité
- **Tags** : `[windows-server-2022]`, `[depannage]`, `[mot-de-passe]`, `[gui]`, `[hardening]`

## 🎯 Problème précis à résoudre
Réinitialiser le mot de passe d'un compte utilisateur local ou du compte Administrateur local sur Windows Server 2022 lorsqu'il est perdu ou expiré, et déverrouiller le compte.

---

## 🖥️ Méthode Interface Graphique (GUI pas-à-pas)

### Vérifier le périmètre
- Cette procédure concerne un serveur autonome ou membre d'un domaine, pas la réinitialisation d'un compte de domaine.
- Sur un contrôleur de domaine, **Utilisateurs et groupes locaux** ne gère pas les comptes du domaine ; le compte Administrateur de restauration des services d'annuaire (DSRM) relève d'une procédure distincte.
- Utiliser un compte d'administration autorisé et vérifier l'identité de la machine et du compte avant toute réinitialisation.

### Réinitialiser un compte local
1. Ouvrir **Gestion de l'ordinateur** (`compmgmt.msc`) > **Utilisateurs et groupes locaux** > **Utilisateurs**.
2. Clic droit sur le compte concerné > **Définir le mot de passe...**. Lire l'avertissement de Windows avant de confirmer : une réinitialisation forcée peut rendre inaccessibles certains fichiers chiffrés EFS, certificats ou secrets enregistrés avec l'ancien mot de passe.
3. Saisir un nouveau mot de passe conforme à la stratégie locale et le confirmer. Le transmettre par le canal approuvé, sans l'inscrire dans la fiche ou un ticket.
4. Ouvrir les propriétés du compte et vérifier **Compte désactivé** et, si la console le propose, **Le compte est verrouillé**. Ne réactiver/déverrouiller qu'après validation de l'identité et de la cause ; le compte Administrateur intégré ne peut pas être verrouillé.
5. Faire tester l'ouverture de session par le propriétaire du compte, puis vérifier les journaux de sécurité en cas de suspicion d'accès non autorisé.

Références : [Microsoft Learn — Comptes locaux](https://learn.microsoft.com/en-us/windows/security/identity-protection/access-control/local-accounts) ; [Microsoft Learn — commande net user](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/net-user).

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Affichage de la liste des comptes utilisateurs locaux :
   `net user`
   👉 Explication : Liste tous les comptes enregistrés dans la base SAM locale.
2. Réinitialisation en invite de commande avec saisie masquée :
   `net user Administrateur *`
   👉 Explication : Demande le nouveau mot de passe sans l'afficher dans la commande ou l'historique du terminal.

---

## ⚡ 2. Production — Façon Simplifiée
1. Réinitialisation sécurisée du mot de passe via PowerShell :
   `$Password = Read-Host -AsSecureString "Saisir le nouveau mot de passe"`
   `Set-LocalUser -Name "AdminLocal" -Password $Password`
   👉 Explication : Modifie le mot de passe du compte local sans que les caractères ne soient visibles.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Activation de la solution LAPS (Local Administrator Password Solution) de Microsoft :
   `Set-LapsADPasswordEncryptionPrincipal -Identity "Domain Controllers"`
   👉 Explication : Automatise la génération de mots de passe complexes uniques et aléatoires.