---
title: "Fiche Simple - Windows Server 2022 PowerShell Securiser Signature"
description: "Durcir PowerShell sur Windows Server 2022 : stratégie d'exécution, signature de code, journalisation."
published: true
date: 2026-10-29T20:58:17Z
tags: ["windows-server-2022", "powershell", "pwsh", "scripting", "remoting"]
editor: markdown
dateCreated: 2026-10-29T20:58:17Z
dateModified: 2026-10-29T20:58:17Z
---

# Fiche_Simple_-_Windows_Server_2022_PowerShell_Securiser_Signature

- **Environnement** : Windows Server 2022 de laboratoire (Desktop Experience ou Core), session administrateur
- **OS / Version** : Windows Server 2022
- **Catégorie** : shell / scripting
- **Tags** : `windows-server-2022`, `powershell`, `pwsh`, `scripting`, `remoting`

---

## Problème précis à résoudre

Durcir PowerShell sur Windows Server 2022 : stratégie d'exécution, signature de code, journalisation.

## 1. Hors-Production (Lab / Test / POC)

1. Définir la stratégie d'exécution de la machine. GUI : gpedit.msc > Configuration ordinateur > Modèles d'administration > Composants Windows > Windows PowerShell > Activer l'exécution des scripts. Ligne de commande (administrateur) :
   ```powershell
   Get-ExecutionPolicy -List
   Set-ExecutionPolicy -ExecutionPolicy AllSigned -Scope LocalMachine
   ```
   👉 Explication : `AllSigned` exige des scripts signés par un éditeur approuvé ; `RemoteSigned` est un compromis. La stratégie n'est pas une frontière de sécurité (contournable). Exécuter la commande dans 5.1 et dans 7 et vérifier le résultat de chacun.

2. Lab uniquement : créer un certificat de signature auto-signé :
   ```powershell
   $cert = New-SelfSignedCertificate -Type CodeSigningCert -Subject 'CN=Signature Scripts Lab' -CertStoreLocation Cert:\CurrentUser\My
   ```
   👉 Explication : en production utiliser un certificat d'une autorité interne (AD CS) ou publique ; la clé privée doit être protégée.

3. Signer un script avec horodatage (CHEMIN_SCRIPT et URL_HORODATAGE à remplacer par une autorité d'horodatage approuvée) :
   ```powershell
   Set-AuthenticodeSignature -FilePath CHEMIN_SCRIPT -Certificate $cert -TimestampServer URL_HORODATAGE
   ```
   👉 Explication : l'horodatage garde la signature valide après expiration du certificat.

4. Vérifier la signature :
   ```powershell
   Get-AuthenticodeSignature -FilePath CHEMIN_SCRIPT | Format-List Status,StatusMessage,SignerCertificate
   ```
   👉 Explication : `Valid` attendu ; un certificat auto-signé n'est valide que s'il est importé dans les magasins de confiance (certlm.msc > Éditeurs approuvés et Autorités racines de confiance) — pratique réservée au lab.

5. Activer la journalisation des blocs de script et des modules. GUI : gpedit.msc > Modèles d'administration > Composants Windows > Windows PowerShell > Activer la journalisation des blocs de script PowerShell / Activer la journalisation de module.
   👉 Explication : ces stratégies existent pour 5.1 ; pour PowerShell 7 des stratégies dédiées (modèles ADMX de PowerShell 7) sont nécessaires — vérifier la documentation `about_Group_Policy_Settings`.

6. Étudier le mode de langage contraint si besoin :
   ```powershell
   $ExecutionContext.SessionState.LanguageMode
   ```
   👉 Explication : `ConstrainedLanguage` est imposé par WDAC/AppLocker ; ne pas l'activer sans plan de test.

## 2. Production — Contrôles

Définir qui signe, où est la clé, comment le certificat est révoqué et renouvelé. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Protéger la clé privée de signature (HSM ou magasin protégé).
- Ne pas importer de certificat auto-signé en production.
- Journaux PowerShell protégés et centralisés.

## Validation et retour arrière

- **Validation** : les scripts non signés sont refusés en `AllSigned` et les scripts signés s'exécutent ; les événements de journalisation apparaissent.
- **Retour arrière** : remettre la stratégie précédente (`Set-ExecutionPolicy RemoteSigned -Scope LocalMachine` si c'était la valeur d'origine) et supprimer le certificat de lab.

## Si le problème n'est pas résolu

- [Microsoft Learn — stratégies d'exécution](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_execution_policies)
- [Microsoft Learn — signature](https://learn.microsoft.com/powershell/module/microsoft.powershell.core/about/about_signing)
- [Fiche connexe — Prerequis Limites](/01-fiches-simples/windows/server-2022/vie-du-logiciel/powershell/fiche-simple-windows-server-2022-powershell-prerequis-limites)