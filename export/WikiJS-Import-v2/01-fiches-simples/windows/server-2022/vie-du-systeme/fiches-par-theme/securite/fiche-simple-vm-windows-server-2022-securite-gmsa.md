---
title: "Fiche Simple - VM Windows Server 2022 Securite gMSA"
description: "Remplacer un compte de service à mot de passe fixe par un compte gMSA (Group Managed Service Account) dont le mot de passe est généré et renouvelé automatiquement par Active Directory, et restreindre les serveurs autorisés à l'utiliser."
published: true
date: 2026-10-29T20:22:42Z
tags: ["[windows-server-2022]", "[gmsa]", "[active-directory]", "[service-account]", "[powershell]"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# 📄 Fiche_Simple_-_VM_Windows_Server_2022_Securite_gMSA

- **Environnement** : Domaine Active Directory (contrôleur de domaine et serveur membre)
- **OS / Version** : Windows Server 2022 - Famille Windows Server (domaine AD DS)
- **Catégorie** : Sécurité / Comptes de service
- **Tags** : `[windows-server-2022]`, `[gmsa]`, `[active-directory]`, `[service-account]`, `[powershell]`

## 🎯 Problème précis à résoudre
Remplacer un compte de service à mot de passe fixe par un compte gMSA (Group Managed Service Account) dont le mot de passe est généré et renouvelé automatiquement par Active Directory, et restreindre les serveurs autorisés à l'utiliser.

---

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Créer la clé racine KDS en la datant de 10 heures dans le passé (lab uniquement) :
   ```powershell
   Add-KdsRootKey -EffectiveTime ((Get-Date).AddHours(-10))
   ```
   👉 Explication : Évite d'attendre 10 heures avant de créer un gMSA. En production, la clé se crée sans ce décalage, et il faut attendre sa date d'activation.
2. Créer le compte gMSA, limité au groupe de serveurs autorisés :
   ```powershell
   New-ADServiceAccount -Name "<nom_gmsa>" -DNSHostName "<nom_gmsa>.<nom_domaine>" -PrincipalsAllowedToRetrieveManagedPassword "<nom_groupe_serveurs>"
   ```
   👉 Explication : Le nom ne doit pas dépasser 15 caractères (limite SAM). Seuls les membres du groupe pourront récupérer le mot de passe géré.
3. Sur le serveur autorisé, installer puis tester le compte :
   ```powershell
   Install-ADServiceAccount -Identity "<nom_gmsa>"
   Test-ADServiceAccount -Identity "<nom_gmsa>"
   ```
   👉 Explication : `Test-ADServiceAccount` doit renvoyer `True`. Il confirme que le serveur peut utiliser le compte.

**Équivalent interface graphique :**

- **Utilisateurs et ordinateurs Active Directory** (`dsa.msc`) > conteneur **Managed Service Accounts** : visualiser le compte gMSA créé et ses propriétés.
  👉 Explication : la création du gMSA et de la clé KDS reste en PowerShell (pas d'assistant graphique); la GUI sert à vérifier.

## ⚡ 2. Production — Façon Simplifiée
1. Affecter le compte gMSA à un service Windows (le mot de passe reste vide) :
   ```powershell
   sc.exe config "<nom_service>" obj= "<nom_domaine>\<nom_gmsa>$" password= ""
   ```
   👉 Explication : Le nom de compte se termine par `$`. Le champ mot de passe doit rester vide, car AD le gère.
2. Redémarrer le service et contrôler son compte d'exécution :
   ```powershell
   Restart-Service -Name "<nom_service>"
   Get-CimInstance -ClassName Win32_Service -Filter "Name='<nom_service>'" | Select-Object Name, StartName, State
   ```
   👉 Explication : Confirme que le service tourne bien sous le compte gMSA.

---

## 🔒 3. Production — Façon Sécurisée (Hardening & Isolation Enterprise)
1. Auditer les gMSA existants, leur activité et leurs serveurs autorisés :
   ```powershell
   Get-ADServiceAccount -Filter * -Properties PrincipalsAllowedToRetrieveManagedPassword, LastLogonDate | Select-Object Name, Enabled, LastLogonDate, PrincipalsAllowedToRetrieveManagedPassword
   ```
   👉 Explication : Repère les comptes inutilisés ou ouverts à trop de machines. Un gMSA sans connexion récente doit être revu.
2. Restreindre la liste des serveurs autorisés à un groupe dédié au service :
   ```powershell
   Set-ADServiceAccount -Identity "<nom_gmsa>" -PrincipalsAllowedToRetrieveManagedPassword "<nom_groupe_restreint>"
   ```
   👉 Explication : Remplace la liste existante par un groupe précis. Un serveur retiré du groupe ne peut plus récupérer le mot de passe, sans avoir besoin de le changer.
3. Retirer le compte gMSA d'un serveur qui n'en a plus l'usage :
   ```powershell
   Uninstall-ADServiceAccount -Identity "<nom_gmsa>"
   ```
   👉 Explication : Supprime le compte du serveur local. Le compte reste dans l'annuaire et peut être supprimé ensuite avec `Remove-ADServiceAccount` après validation.