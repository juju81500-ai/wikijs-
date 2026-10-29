---
title: "Fiche Simple - VM Windows Server 2022 Vie Systeme 17 Resolution De Noms Client"
description: "Configurer les serveurs DNS et les suffixes."
published: true
date: 2026-10-29T20:22:10Z
tags: ["windowsserver2022", "vie-du-systeme", "cycle-de-vie", "etape-17"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2022_Vie_Systeme_17_Resolution_De_Noms_Client

- **Environnement** : Serveur Windows Server 2022
- **OS / Version** : Windows Server 2022; étape 17 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `windowsserver2022`, `vie-du-systeme`, `cycle-de-vie`, `etape-17`

---

## Problème précis à résoudre

Configurer les serveurs DNS et les suffixes.

## 1. Hors-Production (Lab / Test / POC)

1. Ouvrir **Propriétés TCP/IPv4 > Avancé > DNS** pour les suffixes.
   ```powershell
   Get-DnsClientServerAddress -AddressFamily IPv4
   Get-DnsClientGlobalSetting
   ```
   👉 Explication : montre les serveurs DNS et la liste de suffixes.

2. Définir serveurs DNS et suffixes (remplacer `IP_DNS1`, `IP_DNS2`) :
   ```powershell
   Set-DnsClientServerAddress -InterfaceAlias 'ALIAS' -ServerAddresses IP_DNS1,IP_DNS2
   Set-DnsClientGlobalSetting -SuffixSearchList @('EXEMPLE.LOCAL')
   ```
   👉 Explication : deux serveurs assurent la redondance.

3. Tester et vider le cache :
   ```powershell
   Resolve-DnsName NOM_HOTE
   Clear-DnsClientCache
   ```
   👉 Explication : valide la résolution et force une nouvelle requête.

## 2. Production — Contrôles

Utiliser les DNS internes du domaine, pas de résolveur public pour un serveur joint à AD.

## 3. Production — Sécurité

Surveiller les modifications de DNS et interdire les mises à jour dynamiques non sécurisées.

## Validation et retour arrière

- **Validation** : `Resolve-DnsName` renvoie l'adresse attendue.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Windows Server 2022](/01-fiches-simples/windows/server-2022/vie-du-systeme/sommaire-vie-du-systeme-windows-server-2022)
- [Documentation officielle](https://learn.microsoft.com/fr-fr/windows-server/)