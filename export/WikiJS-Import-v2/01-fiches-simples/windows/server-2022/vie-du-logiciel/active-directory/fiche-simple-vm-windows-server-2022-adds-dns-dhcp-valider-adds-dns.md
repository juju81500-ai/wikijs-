---
title: "Fiche Simple - VM Windows Server 2022 ADDS DNS DHCP Valider ADDS DNS"
description: "Contrôler l'état du domaine et de la résolution DNS."
published: true
date: 2026-10-29T20:14:10Z
tags: ["windows-server-2022", "active-directory", "dns", "dhcp", "gpo"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Windows_Server_2022_ADDS_DNS_DHCP_Valider_ADDS_DNS.md

- **Environnement** : VM ou serveur dédié Windows Server 2022, domaine de laboratoire ou d'entreprise
- **OS / Version** : Windows Server 2022; rôles AD DS, DNS et DHCP
- **Catégorie** : annuaire / services réseau
- **Tags** : `windows-server-2022`, `active-directory`, `dns`, `dhcp`, `gpo`

---

## Problème précis à résoudre

Contrôler l'état du domaine et de la résolution DNS.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier domaine, forêt et DNS (ad.example.net est un exemple à remplacer) :
   ```powershell
   Get-ADDomain
   Get-ADForest
   dcdiag /test:dns /v
   Resolve-DnsName -Type SRV _ldap._tcp.dc._msdcs.ad.example.net
   ```
   👉 Explication : les enregistrements SRV du contrôleur doivent résoudre.

2. GUI : **Gestionnaire de serveur > Outils > DNS** pour inspecter les zones.
   👉 Explication : vue graphique des zones.

3. Configurer les redirecteurs DNS uniquement vers des résolveurs approuvés (**DNS > Propriétés du serveur > Redirecteurs**).
   👉 Explication : on évite des résolveurs non maîtrisés.

4. Vérifier la résolution des zones internes depuis un poste membre avant de poursuivre.
   👉 Explication : c'est le test réel côté client.

## 2. Production — Contrôles

Conserver les sorties de `dcdiag` dans le dossier de recette.

## 3. Production — Sécurité

- Ne pas exposer LDAP, Kerberos ni DNS à Internet.

## Validation et retour arrière

- **Validation** : `dcdiag /test:dns` réussit et les SRV résolvent.
- **Retour arrière** : Corriger la configuration DNS en erreur; ne pas promouvoir d'autre contrôleur avant résolution.

## Si le problème n'est pas résolu

- [Microsoft Learn — Active Directory Domain Services](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview)
- [Microsoft Learn — Install-ADDSForest](https://learn.microsoft.com/en-us/powershell/module/addsdeployment/install-addsforest)
- [Guide complet AD DS, DNS et DHCP Windows Server 2022](/02-fiches-completes/windows/server-2022/installation-deploiement/01-active-directory-ds-dns-dhcp-windows-server-2022#3-valider-ad-ds-et-dns)