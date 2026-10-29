---
title: "Fiche Simple - Windows Server 2022 Citrix CVAD Securiser"
description: "Sécuriser CVAD : TLS, comptes, pare-feu, rôles d'administration."
published: true
date: 2026-10-29T20:56:04Z
tags: ["citrix", "cvad", "windows-server", "securite"]
editor: markdown
dateCreated: 2026-10-29T20:56:04Z
dateModified: 2026-10-29T20:56:04Z
---

# Fiche_Simple_-_Windows_Server_2022_Citrix_CVAD_Securiser

- **Environnement** : Serveurs Windows Server 2022 (Delivery Controller, StoreFront, licences, SQL) et VM VDA, compte administrateur nominatif
- **OS / Version** : Windows Server 2022; version CVAD à vérifier auprès de l'éditeur
- **Catégorie** : VDI / virtualisation d'applications / Citrix
- **Tags** : `citrix`, `cvad`, `windows-server`, `securite`

---

## Problème précis à résoudre

Sécuriser CVAD : TLS, comptes, pare-feu, rôles d'administration.

## 1. Hors-Production (Lab / Test / POC)

1. Demander un certificat serveur à l'AC interne pour STORE_FQDN et le Controller ; l'importer dans le magasin Ordinateur. PowerShell :
```powershell
Get-ChildItem Cert:\LocalMachine\My | Where-Object Subject -like '*STORE_FQDN*' | Format-List Subject,NotAfter,Thumbprint
```
   👉 Explication : STORE_FQDN est à remplacer ; contrôler la date d'expiration et la chaîne.

2. Lier le certificat dans IIS : GUI **Gestionnaire des services Internet > Sites > Default Web Site > Liaisons > https > Modifier**, puis passer l'URL de base StoreFront en HTTPS (**StoreFront > Server Group > Change Base URL**).
   👉 Explication : évite l'authentification en clair sur le portail.

3. Activer HTTPS entre StoreFront et Controller et restreindre les ports avec le pare-feu Windows. PowerShell :
```powershell
New-NetFirewallRule -DisplayName 'CVAD StoreFront HTTPS' -Direction Inbound -Protocol TCP -LocalPort 443 -RemoteAddress PLAGE_CLIENTS -Action Allow
```
   👉 Explication : PLAGE_CLIENTS est à remplacer ; les ports Controller/VDA (par ex. 80, 1494, 2598) sont à confirmer dans la documentation de votre version.

4. Créer des rôles d'administration délégués : GUI **Studio > Configuration > Administrators > Create Administrator**, un compte nominatif par administrateur.
   👉 Explication : évite l'usage d'un compte partagé et trace les actions via la journalisation de configuration.

## 2. Production — Contrôles

- Rotation planifiée des certificats avant expiration.
- Journalisation de configuration activée.

## 3. Production — Sécurité

- Aucun mot de passe en clair dans les scripts ; utiliser un compte de service géré.
- Désactiver HTTP sur StoreFront une fois HTTPS validé.
- Appliquer les durcissements de la section 05-Hardening-AIS-Cyber.

## Validation et retour arrière

- **Validation** : Portail accessible en HTTPS sans alerte de certificat, règles pare-feu limitées.
- **Retour arrière** : Restaurer la liaison IIS précédente et supprimer la règle pare-feu ajoutée.

## Si le problème n'est pas résolu

- [Citrix — documentation produit CVAD](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops)
- [Citrix — System requirements](https://docs.citrix.com/en-us/citrix-virtual-apps-desktops/system-requirements.html)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/13-poste-de-travail-et-vdi/fiche-logiciel-citrix-virtual-apps-and-desktops)