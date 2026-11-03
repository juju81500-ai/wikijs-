# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Securite_ADCS_Certs

- **Environnement** : VM (Windows Server 2022, autorité de certification d'entreprise) / Domaine Active Directory
- **OS / Version** : Windows Server 2022 - Famille Windows Server (AD CS)
- **Catégorie** : Sécurité / PKI et certificats
- **Tags** : `[windows-server-2022]`, `[ad-cs]`, `[pki]`, `[certificats]`, `[certutil]`, `[powershell]`

## 🎯 Problème précis à résoudre
Installer une autorité de certification Active Directory Certificate Services (AD CS) pour émettre les certificats TLS et de machine du domaine, puis demander un certificat serveur et publier les listes de révocation (CRL).

> En production, la hiérarchie recommandée est une racine hors ligne (Standalone Root CA) et une autorité émettrice subordonnée (Enterprise Subordinate CA). La procédure lab ci-dessous crée une racine d'entreprise unique, à ne pas utiliser telle quelle en production.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer le rôle AD CS avec sa console :
   ```powershell
   Install-WindowsFeature -Name ADCS-Cert-Authority -IncludeManagementTools
   ```
   👉 Explication : Ajoute le rôle d'autorité de certification sans le configurer.
2. Configurer une autorité racine d'entreprise pour le laboratoire :
   ```powershell
   Install-AdcsCertificationAuthority -CAType EnterpriseRootCa -CACommonName "<nom_autorite>" -CryptoProviderName "RSA#Microsoft Software Key Storage Provider" -KeyLength 4096 -HashAlgorithmName SHA256 -ValidityPeriod Years -ValidityPeriodUnits 5 -Force
   ```
   👉 Explication : Crée la clé RSA 4096 bits et le certificat racine valable 5 ans. Cette opération est définitive pour la forêt du lab.
3. Vérifier l'autorité et les modèles de certificats disponibles :
   ```powershell
   certutil -CAInfo
   certutil -CATemplates
   ```
   👉 Explication : Affiche le nom, le certificat et l'état de l'autorité, puis la liste des modèles publiés (par exemple WebServer).

**Équivalent interface graphique :**

- **Gestionnaire de serveur > Gérer > Ajouter des rôles et fonctionnalités > Services de certificats Active Directory**, puis la notification **Configurer les services de certificats** (Autorité de certification, **Autorité de certification d'entreprise**, racine, RSA 4096, SHA256, 5 ans). Console : `certsrv.msc`.
  👉 Explication : équivalent de `Install-WindowsFeature` et `Install-AdcsCertificationAuthority`.

## ⚡ 2. Production — Façon Simplifiée
1. Demander un certificat serveur à partir du modèle WebServer :
   ```powershell
   Get-Certificate -Template "WebServer" -DnsName "<nom_serveur_dns>" -CertStoreLocation Cert:\LocalMachine\My
   ```
   👉 Explication : Génère une demande, la soumet à l'autorité et installe le certificat dans le magasin de la machine. Le nom DNS doit correspondre au nom utilisé par les clients.
2. Contrôler le certificat installé :
   ```powershell
   Get-ChildItem -Path Cert:\LocalMachine\My | Where-Object { $_.Subject -like "*<nom_serveur_dns>*" } | Select-Object Subject, NotAfter, Thumbprint
   ```
   👉 Explication : Affiche la date d'expiration et l'empreinte du certificat, à reporter dans la supervision des échéances.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Exporter le certificat de l'autorité racine pour distribution contrôlée aux postes :
   ```powershell
   New-Item -ItemType Directory -Path "C:\PKI" -Force | Out-Null
   certutil -ca.cert "C:\PKI\ca_racine.cer"
   ```
   👉 Explication : Fournit le certificat public de l'autorité à déployer par GPO. La clé privée ne quitte jamais l'autorité.
2. Régler la période de publication des CRL (une semaine) et la publier :
   ```powershell
   certutil -setreg CA\CRLPeriodUnits 1
   certutil -setreg CA\CRLPeriod "Weeks"
   Restart-Service -Name CertSvc
   certutil -CRL
   ```
   👉 Explication : Les clients vérifient la révocation à partir de cette liste. Une période trop longue retarde la prise en compte d'un certificat révoqué ; ajuster selon la politique de l'organisation.
3. Vérifier la configuration CRL enregistrée :
   ```powershell
   certutil -getreg CA\CRLPeriod
   certutil -getreg CA\CRLPeriodUnits
   ```
   👉 Explication : Confirme que les paramètres ont bien été appliqués avant d'archiver la configuration de l'autorité.
