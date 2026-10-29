---
title: "Fiche Simple - Windows Server 2022 Nakivo Securiser"
description: "Sécuriser l'accès à NAKIVO : comptes, certificat TLS et pare-feu Windows."
published: true
date: 2026-10-29T20:36:08Z
tags: ["nakivo", "director", "transporter", "securite", "tls", "pare-feu", "comptes"]
editor: markdown
dateCreated: 2026-10-29T20:36:08Z
dateModified: 2026-10-29T20:36:08Z
---

# Fiche_Simple_-_Windows_Server_2022_Nakivo_Securiser

- **Environnement** : `Serveur Windows Server 2022 (VM ou physique), compte administrateur local ou de domaine nominatif`
- **OS / Version** : `Windows Server 2022 (Desktop Experience ou Core selon support de la version); vérifier la compatibilité et la version courante du produit auprès de l'éditeur`
- **Catégorie** : `sauvegarde / restauration / NAKIVO`
- **Tags** : `nakivo`, `director`, `transporter`, `securite`, `tls`, `pare-feu`, `comptes`

---

## Problème précis à résoudre

Sécuriser l'accès à NAKIVO : comptes, certificat TLS et pare-feu Windows.

## 1. Hors-Production (Lab / Test / POC)

1. Créer des comptes nominatifs dans l'interface web : **Settings > User Accounts** (libellé à vérifier) ; limiter les droits au strict nécessaire.
   👉 Explication : les actions de sauvegarde et de restauration sont ainsi attribuables.

2. Remplacer le certificat auto-signé par un certificat de l'autorité interne : chercher la section certificat/TLS dans **Settings** selon la version, ou la documentation officielle (vérifier version).
   👉 Explication : les navigateurs ne doivent plus avertir et le trafic reste chiffré.

3. Lister les règles pare-feu. PowerShell :
```powershell
Get-NetFirewallRule -DisplayName '*NAKIVO*' | Format-Table DisplayName,Enabled,Direction,Action
```
   👉 Explication : on contrôle ce que l'installeur a ouvert.

4. Restreindre l'accès web au réseau d'administration :
```powershell
New-NetFirewallRule -DisplayName 'NAKIVO web admin' -Direction Inbound -Protocol TCP -LocalPort PORT_WEB -RemoteAddress RESEAU_ADMIN -Action Allow
```
   👉 Explication : PORT_WEB et RESEAU_ADMIN sont à remplacer.

5. Vérifier dans la documentation les options d'authentification à deux facteurs et de chiffrement des sauvegardes pour votre version et les activer si présentes.
   👉 Explication : on n'affirme pas une option sans vérification.

## 2. Production — Contrôles

- Revoir les comptes et règles régulièrement.
- Garder une copie hors site ou immuable du dépôt si la version le permet.

## 3. Production — Sécurité

- Aucun mot de passe ni clé de chiffrement dans la fiche ; les stocker dans un coffre.
- Isoler les flux Director/Transporter.

## Validation et retour arrière

- **Validation** : Accès web en HTTPS depuis le réseau d'administration seulement; comptes nominatifs.
- **Retour arrière** : Désactiver la règle ajoutée (`Disable-NetFirewallRule -DisplayName 'NAKIVO web admin'`) et rétablir l'ancien certificat si besoin.

## Si le problème n'est pas résolu

- [NAKIVO — Help Center officiel](https://helpcenter.nakivo.com/)
- [NAKIVO — System Requirements](https://helpcenter.nakivo.com/display/NH/System+Requirements)
- [Fiche d'entrée du logiciel](/01-fiches-simples/logiciels/07-sauvegarde-restauration-et-pra-pca/fiche-logiciel-nakivo-altaro)