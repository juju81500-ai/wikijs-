# Fiche_Simple_-_Cloud_Entra_ID_Connect_Architecture

- **Environnement** : Tenant Microsoft Entra ID (SaaS), poste d'administration avec PowerShell 7 et modules Microsoft.Graph ; serveur Windows Server pour Microsoft Entra Connect
- **OS / Version** : Cloud/SaaS — administration défensive (aucun OS à installer ; licences et fonctions à vérifier)
- **Catégorie** : systèmes, annuaires et services

---

## Problème précis à résoudre

Choisir et documenter l'architecture de synchronisation d'identités hybrides avec le produit actuel, Microsoft Entra Connect (Connect Sync) ou Entra Cloud Sync.

## 1. Hors-Production (Lab / Test / POC)

1. Lire la page Learn « Choose between Connect Sync and Cloud Sync » et choisir selon la topologie (forêts, filtrage, écriture différée, objets pris en charge).
   👉 Explication : la décision ne repose pas sur le nom historique « Azure AD Connect » ; confirmer la fonctionnalité nécessaire.

2. Vérifier les prérequis publiés : système de serveur supporté, .NET, TLS 1.2, compte et rôles requis, URL/ports sortants.
   👉 Explication : ne pas déduire la matrice de support ; elle évolue. Consulter la page « Prerequisites ».

3. Télécharger Microsoft Entra Connect depuis le Centre d'administration : Entra admin center → Entra ID → Entra Connect → Get started (ou lien indiqué par Learn).
   👉 Explication : télécharger uniquement depuis la source officielle Microsoft et valider la signature.

4. Installer Connect Sync depuis le MSI officiel, puis configurer avec l'assistant GUI. Dans **Microsoft Entra Connect** > **Customize**, choisir les options adaptées à la topologie, valider le filtrage des unités d'organisation et ne démarrer l'export qu'après approbation. Pour un serveur secondaire, activer **Staging mode**.
   ```powershell
   $Installer = 'C:\INSTALL\AzureADConnect.msi' # CHEMIN_MSI_VERIFIE à remplacer
   Get-AuthenticodeSignature $Installer
   Start-Process msiexec.exe -Wait -ArgumentList '/i', $Installer
   ```
   👉 Explication : CHEMIN_MSI_VERIFIE est un placeholder à remplacer par le chemin du MSI téléchargé depuis Microsoft. Vérifier la signature avant exécution; le nom du paquet et les écrans de l'assistant peuvent varier selon la version publiée.

5. Dessiner : serveur actif, serveur de préproduction (staging), filtrage, méthode d'authentification (PHS, PTA, fédération), compte(s) utilisé(s).
   👉 Explication : un seul serveur actif d'exportation par tenant ; le serveur secondaire doit rester en mode staging jusqu'à la bascule approuvée.

6. Sur le serveur après installation, lire l'état de synchronisation :
   ```powershell
   Import-Module ADSync
   Get-ADSyncScheduler
   ```
   👉 Explication : module installé avec Entra Connect ; lecture seule.

7. Compte cloud côté Graph :
   ```powershell
   Connect-MgGraph -Scopes 'OnPremDirectorySynchronization.Read.All' -ContextScope Process
   Get-MgDirectoryOnPremiseSynchronization
   ```
   👉 Explication : consulte la configuration de synchronisation du tenant ; vérifier l'applicabilité du cmdlet dans la version du SDK.

## 2. Production — Contrôles

Production : changement approuvé, serveur durci et dédié, sauvegarde du serveur et de la configuration exportée, comptes connecteurs gérés par l'assistant, pilote par unité d'organisation.

## 3. Production — Sécurité

- Ne pas exposer, noter ou copier les identifiants du compte connecteur ; le compte est généré par l'assistant.
- Traiter le serveur Entra Connect comme un actif de niveau 0 (Tier 0).
- Ne pas lancer de synchronisation complète sans filtrage validé.

## Validation et retour arrière

- **Validation** : schéma approuvé, prérequis confirmés, pilote défini.
- **Retour arrière** : aucun changement n'a eu lieu à ce stade.

## Si le problème n'est pas résolu

- [Entra Connect Sync — installation personnalisée](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-custom)
- [Entra Connect Sync — prérequis](https://learn.microsoft.com/entra/identity/hybrid/connect/how-to-connect-install-prerequisites)
- [Choisir Connect Sync ou Cloud Sync](https://learn.microsoft.com/entra/identity/hybrid/cloud-sync/what-is-cloud-sync)
- [Documentation Microsoft Entra ID](https://learn.microsoft.com/entra/identity/)
- [Fiche d'entrée Microsoft Entra ID](/01-fiches-simples/logiciels/05-systemes-annuaires-et-services/fiche-logiciel-microsoft-entra-id)