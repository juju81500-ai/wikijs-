---
title: "VM_WinSrv_2022_GPO_Configuration-Strategie-Groupe-Securite"
description: "Créer, configurer et lier une Stratégie de Groupe (GPO) dans Active Directory sous Windows Server 2022 pour durcir la politique de mots de passe, restreindre le Pare-feu Windows et bloquer l'exécution d'outils d'administration non autorisés."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[windows-server-2022]", "[gpo]", "[active-directory]", "[hardening]", "[security-policy]", "[gui]", "[powershell]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 VM_WinSrv_2022_GPO_Configuration-Strategie-Groupe-Securite.md

- **Environnement** : VM (Windows Server 2022 Active Directory)
- **OS / Version** : Windows Server 2022 - Famille Windows
- **Catégorie** : Sécurité & Stratégies de Groupe / GPO
- **Tags** : `[windows-server-2022]`, `[gpo]`, `[active-directory]`, `[hardening]`, `[security-policy]`, `[gui]`, `[powershell]`

## 🎯 Problème précis à résoudre
Créer, configurer et lier une Stratégie de Groupe (GPO) dans Active Directory sous Windows Server 2022 pour durcir la politique de mots de passe, restreindre le Pare-feu Windows et bloquer l'exécution d'outils d'administration non autorisés.

---

## 🖥️ Méthode Interface Graphique (GUI pas-à-pas)

### Préparer le changement
- Installer la fonctionnalité **Gestion de stratégie de groupe** sur le poste d'administration et vérifier les droits d'édition du GPO et de liaison à l'OU.
- Sauvegarder le GPO existant si on le modifie. Pour un nouveau réglage, commencer par une OU de test contenant uniquement des machines de laboratoire.
- Ne pas lier une GPO de test à la racine du domaine : une liaison à cet endroit peut toucher tous les utilisateurs ou ordinateurs concernés.

### Créer et lier une GPO de test
1. Dans **Gestionnaire de serveur** > **Outils**, ouvrir **Gestion de stratégie de groupe** (`gpmc.msc`).
2. Développer **Forêt** > **Domaines** > le domaine cible. Dans **Group Policy Objects**, clic droit > **Nouveau**, nommer la GPO (ex. `GPO_Test_Securite`) et ne pas la lier tout de suite.
3. Clic droit sur la GPO > **Modifier**. Pour le pare-feu, aller à **Configuration ordinateur** > **Stratégies** > **Paramètres Windows** > **Paramètres de sécurité** > **Pare-feu Windows Defender avec fonctions avancées de sécurité**. Configurer les profils et les règles selon le pare-feu approuvé du site ; ne pas couper l'administration distante avant d'avoir une règle de gestion testée.
4. Pour une restriction d'application, utiliser une stratégie AppLocker ou WDAC conçue pour l'édition de Windows et le parc cible. Commencer en mode audit, créer et vérifier les règles par éditeur/chemin appropriées, puis tester le démarrage et le support avant d'appliquer. Ne pas bloquer globalement MMC ou PowerShell : cela peut empêcher l'administration et les outils métiers.
5. Fermer l'éditeur. Dans GPMC, clic droit sur l'OU de laboratoire > **Lier un objet de stratégie de groupe existant**, choisir `GPO_Test_Securite`. Vérifier l'onglet **Étendue**, le filtrage de sécurité et les objets effectivement contenus dans l'OU.
6. Sur un client de test, actualiser la stratégie depuis une session administrative. Dans GPMC, clic droit sur **Résultats de stratégie de groupe** > **Assistant Résultats de stratégie de groupe**, sélectionner l'ordinateur et l'utilisateur de test, puis vérifier les paramètres appliqués et les GPO gagnantes.

### Traiter la stratégie de mot de passe au bon niveau
La stratégie de mot de passe de domaine ne se déploie pas en liant une GPO ordinaire à une OU d'utilisateurs : elle est définie au niveau du domaine. Une règle de mot de passe propre à un groupe d'utilisateurs doit utiliser une stratégie de mot de passe affinée (PSO) et être gérée dans le Centre d'administration Active Directory, après validation du niveau fonctionnel et du périmètre. Ne pas remplacer une politique de production sans revue et plan de retour arrière.

Références : [Microsoft Learn — Console GPMC](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-management-console) ; [Microsoft Learn — Vue d'ensemble des GPO et des OU](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/group-policy/group-policy-overview).

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Création d'une GPO de test via PowerShell :
   `New-ADOrganizationalUnit -Name "OU_Test_GPO" -Path "DC=lab,DC=local" -ProtectedFromAccidentalDeletion $true; New-GPO -Name "GPO_Test_Securite"`
   👉 Explication : Crée l'objet de stratégie de groupe vide dans l'annuaire Active Directory.
2. Liaison rapide de la GPO à la racine du domaine :
   `New-GPLink -Name "GPO_Test_Securite" -Target "OU=OU_Test_GPO,DC=lab,DC=local"`
   👉 Explication : Limite le test à une OU dédiée ; ne pas lier une GPO de test à la racine du domaine.
3. Force de la mise à jour immédiate des stratégies sur la machine locale :
   `gpupdate /force`
   👉 Explication : Applique les modifications de stratégie sans attendre l'intervalle de rafraîchissement par défaut.

---

## ⚡ 2. Production — Façon Simplifiée
1. Création et liaison d'une GPO ciblée sur l'Unité d'Organisation (OU) de production :
   `New-GPO -Name "GPO_Hardening_Postes" | New-GPLink -Target "OU=TSSR_Ordinateurs,DC=lab,DC=local"`
   👉 Explication : Génère et lie directement la stratégie à la structure organisationnelle spécifique.
2. Configuration de la politique de complexité des mots de passe du domaine :
   `Set-ADDefaultDomainPasswordPolicy -MinPasswordLength 14 -ComplexityEnabled $true -LockoutThreshold 5`
   👉 Explication : Impose des mots de passe de 14 caractères minimum et verrouille le compte après 5 échecs consécutifs.
3. Génération du rapport de vérification des stratégies appliquées :
   `gpresult /h C:\Rapport_GPO.html`
   👉 Explication : Exporte le résultat DSoP (Resultant Set of Policy) au format HTML pour audit.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Désactivation des protocoles d'authentification obsolètes et vulnérables (NetBIOS sur TCP/IP et LLMNR) via la GPO :
   `Set-GPRegistryValue -Name "GPO_Hardening_Postes" -Key "HKLM\Software\Policies\Microsoft\Windows NT\DNSClient" -ValueName "EnableMulticast" -Type DWord -Value 0`
   👉 Explication : Bloque le protocole LLMNR pour contrecarrer les attaques d'interception de hachages NTLM (Responder / Poisoning).
2. Verrouillage du Pare-feu Windows en mode Inbound-Block par GPO :
   `Set-GPRegistryValue -Name "GPO_Hardening_Postes" -Key "HKLM\System\CurrentControlSet\Services\SharedAccess\Parameters\FirewallPolicy\DomainProfile" -ValueName "EnableFirewall" -Type DWord -Value 1`
   👉 Explication : Force l'activation du pare-feu sur le profil de domaine de toutes les machines membres.
3. Restriction du ciblage GPO via le filtrage de sécurité (Security Filtering) :
   `Remove-GPPermission -Name "GPO_Hardening_Postes" -TargetName "Authenticated Users" -TargetType Group -Permission LevelGpoApply`
   👉 Explication : Empêche l'application universelle de la stratégie et la restreint au seul groupe d'ordinateurs autorisés.