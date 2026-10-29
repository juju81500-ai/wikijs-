# 📄 VM_WinSrv_2022_ADDS_Promotion-Controleur-Domaine.md

- **Environnement** : VM (Hyper-V / Proxmox VE)
- **OS / Version** : Windows Server 2022 - Famille Windows Server
- **Catégorie** : Annuaire & Identité (AD DS)
- **Tags** : `[winsrv2022]`, `[windows-family]`, `[active-directory]`, `[adds]`, `[dns]`, `[gui]`, `[hardening]`

## 🎯 Problème précis à résoudre
Installer le rôle AD DS (Services de domaine Active Directory), promouvoir la machine en premier Contrôleur de Domaine (DC) de la forêt et sécuriser l'annuaire.

---

## 🖥️ Méthode Interface Graphique (GUI pas-à-pas)

### Préparer la promotion
- Attribuer une adresse IP statique et vérifier le nom du serveur, la synchronisation horaire, la connectivité et les DNS selon le scénario. Pour un DC supplémentaire, utiliser les DNS du domaine existant ; ne pas inventer une configuration DNS de production.
- Confirmer que le changement crée bien une nouvelle forêt. Si le domaine existe déjà, choisir **Ajouter un contrôleur de domaine à un domaine existant** ; ne pas créer une seconde forêt par erreur.
- Préparer le nom DNS/NetBIOS, le site AD, les chemins NTDS/SYSVOL si non standards, les comptes autorisés et un mot de passe DSRM transmis par canal sécurisé. Prévoir le redémarrage et un point de retour arrière.

### Installer AD DS et promouvoir le serveur
1. Dans **Gestionnaire de serveur** > **Gérer** > **Ajouter des rôles et fonctionnalités**, choisir **Installation basée sur un rôle ou une fonctionnalité**, sélectionner le serveur local, cocher **Services AD DS**, puis **Ajouter des fonctionnalités** et terminer l'installation.
2. Dans la page **Résultats**, sélectionner **Promouvoir ce serveur en contrôleur de domaine**. Si l'assistant a été fermé, ouvrir le drapeau de notification **Gestionnaire de serveur** > **Tâches de configuration post-déploiement**.
3. Pour le premier DC, sélectionner **Ajouter une nouvelle forêt** et saisir le nom DNS complet du domaine (ex. `corp.example.test`). Pour un DC supplémentaire, sélectionner le domaine existant et fournir un compte autorisé à joindre/promotionner un DC.
4. Dans **Options du contrôleur de domaine**, choisir DNS et Catalogue global selon l'architecture, le site voulu et un mot de passe DSRM robuste. Ne pas enregistrer ce mot de passe dans la fiche ni dans un ticket.
5. Examiner les options DNS/délégation, le nom NetBIOS, les chemins de base de données/journaux/SYSVOL et la source de réplication. Ne pas placer NTDS/SYSVOL sur ReFS ; confirmer les volumes et l'espace avant de continuer.
6. Dans **Options de révision**, contrôler chaque valeur. Lancer **Vérification des conditions préalables** et corriger les erreurs ; ne pas contourner les contrôles pour faire passer la promotion. Sélectionner **Installer** uniquement après validation : le serveur redémarre.
7. Après redémarrage, ouvrir **Gestionnaire de serveur** > **Outils** > **Utilisateurs et ordinateurs Active Directory** et **DNS**. Confirmer le domaine et les zones attendues, puis vérifier les journaux **Services d'annuaire**, **Serveur DNS** et **Système** dans l'Observateur d'événements. Pour un DC supplémentaire, confirmer aussi la réplication avec l'équipe AD avant de le déclarer opérationnel.

Référence : [Microsoft Learn — Installer AD DS avec Server Manager](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/deploy/install-active-directory-domain-services--level-100-).

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installation du rôle via PowerShell en une ligne :
   `Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools`
   👉 Explication : Télécharge et installe les fichiers binaires du rôle Active Directory et la console RSAT.
2. Promotion rapide d'une nouvelle forêt de test :
   `Install-ADDSForest -DomainName "lab.local" -Force`
   👉 Explication : Crée la forêt AD `lab.local` pour le laboratoire et initialise le serveur.

---

## ⚡ 2. Production — Façon Simplifiée
1. Vérification de la pré-configuration de l'IP statique obligatoire :
   `Get-NetIPAddress -InterfaceAlias "Ethernet0"`
   👉 Explication : S'assure que la carte réseau possède une adresse IP fixe avant d'initier l'annuaire.
2. Installation du rôle AD DS et des outils de gestion :
   `Install-WindowsFeature -Name AD-Domain-Services -IncludeManagementTools`
   👉 Explication : Prépare le serveur à recevoir l'annuaire d'entreprise.
3. Promotion structurée de la forêt de production :
   `Install-ADDSForest -DomainName "corp.tssr.local" -DomainNetbiosName "CORP" -InstallDns:$true -Force`
   👉 Explication : Déploie la forêt Active Directory d'entreprise et configure automatiquement le serveur DNS intégré.

---

## 🔒 3. Production — Façon Sécurisée (Hardening Enterprise & Security Baseline)
1. Restriction des protocoles d'authentification obsolètes (Désactivation NTLMv1) :
   `Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\Lsa" -Name "LmCompatibilityLevel" -Value 5`
   👉 Explication : Force l'utilisation exclusive de NTLMv2 et Kerberos pour bloquer le relais d'identifiants.
2. Désactivation du protocole LLMNR et de NBT-NS sur le serveur :
   `Set-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient" -Name "EnableMulticast" -Value 0`
   👉 Explication : Élimine les risques d'usurpation d'identité réseau par empoisonnement LLMNR.
3. Protection du compte Administrateur du domaine :
   `Set-ADUser -Identity "Administrator" -CannotChangePassword $false -PasswordNeverExpires $false`
   👉 Explication : Applique les politiques d'expiration de mot de passe rigoureuses et verrouille l'utilisation des comptes génériques.