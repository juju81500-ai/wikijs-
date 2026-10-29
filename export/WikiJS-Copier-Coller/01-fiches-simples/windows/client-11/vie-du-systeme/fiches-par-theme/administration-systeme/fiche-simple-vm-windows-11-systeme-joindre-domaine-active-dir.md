# 📄 VM_Win11_Systeme_Joindre-Domaine-Active-Directory.md

- **Environnement** : VM / Poste client (Windows 11)
- **OS / Version** : Windows 11 - Famille Windows Client
- **Catégorie** : Système / Annuaire & Domaine AD DS

## 🎯 Problème précis à résoudre
Joindre un poste client Windows 11 à un domaine Active Directory d'entreprise (`lab.local`), placer l'ordinateur dans la bonne Unité d'Organisation (OU) et sécuriser la jonction.

---

## 🖥️ Méthode Interface Graphique (GUI pas-à-pas)

### Prérequis
- L'édition doit permettre l'adhésion au domaine (Pro, Enterprise ou Education ; Windows Home ne peut pas rejoindre un domaine AD classique).
- La carte réseau du poste doit utiliser le DNS du domaine ; vérifier la connectivité au contrôleur de domaine et la synchronisation de l'heure avant l'opération.
- Disposer d'un compte explicitement autorisé à joindre des postes, et connaître l'OU cible. Si l'objet ordinateur doit être précréé ou placé dans une OU précise, le faire dans ADUC selon la délégation de l'organisation.

### Joindre le poste
1. Ouvrir **Paramètres** > **Comptes** > **Accès professionnel ou scolaire** > **Se connecter**.
2. Dans la fenêtre de connexion, sélectionner **Joindre cet appareil à un domaine Active Directory local** (et non l'option d'inscription à Microsoft Entra ID).
3. Saisir le FQDN du domaine (`lab.local` seulement dans le laboratoire), puis **Suivant**. Fournir les identifiants autorisés à joindre l'ordinateur lorsqu'ils sont demandés.
4. Si l'assistant demande le type de compte, choisir l'utilisateur standard prévu ; ne pas ajouter le poste ou l'utilisateur aux administrateurs locaux sans besoin validé.
5. Terminer l'assistant et redémarrer lorsque Windows le demande.
6. Après redémarrage, se connecter avec le compte de domaine (`DOMAINE\utilisateur` ou UPN). Dans **Paramètres** > **Système** > **Informations système**, vérifier l'appartenance au domaine. Dans ADUC, contrôler que le compte ordinateur est dans l'OU attendue ; vérifier l'application des GPO avec l'équipe poste de travail.

Si le domaine est introuvable, arrêter et corriger le DNS ou la connectivité avant de répéter la jonction. Ne pas supprimer puis recréer le compte ordinateur en production sans vérifier les droits et la procédure de réutilisation sécurisée du compte.

Référence : [Microsoft Learn — Joindre un ordinateur à un domaine](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/join-computer-to-domain).

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Vérification de la résolution DNS du domaine :
   `Test-Connection -TargetName "lab.local" -Count 2`
   👉 Explication : S'assure que le poste client interroge bien le contrôleur de domaine DNS.
2. Jonction simple au domaine sans ciblage d'OU :
   `Add-Computer -DomainName "lab.local" -Credential (Get-Credential) -Restart`
   👉 Explication : Demande les identifiants d'un administrateur du domaine et redémarre la machine pour finaliser la jonction.

---

## ⚡ 2. Production — Façon Simplifiée
1. Jonction au domaine avec placement direct dans l'Unité d'Organisation cible :
   `Add-Computer -DomainName "lab.local" -OUPath "OU=Postes_Windows11,OU=TSSR_Ordinateurs,DC=lab,DC=local" -Credential "LAB\adm-jdupont" -Restart`
   👉 Explication : Place le compte ordinateur directement dans la bonne OU pour lui appliquer immédiatement les GPO de sécurité.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Pré-création sécurisée du compte ordinateur (Offline Domain Join / Provisioning dsa.msc) :
   `djoin.exe /provision /domain "lab.local" /machine "WIN11-PC01" /policypaths "OU=Postes_Windows11,DC=lab,DC=local" /savefile "C:\provision.txt"`
   👉 Explication : Prépare le jeton de jonction chiffré sur le contrôleur de domaine sans transmettre d'identifiants d'administration sur le réseau client.