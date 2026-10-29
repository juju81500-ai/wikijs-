---
title: "Fiche Simple - VM TrueNAS CORE 13.0 Vie Systeme 39 Chiffrement Des Flux Pki"
description: "Installer un certificat valide."
published: true
date: 2026-10-29T20:22:10Z
tags: ["truenascore130", "vie-du-systeme", "cycle-de-vie", "etape-39"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_TrueNAS_CORE_13.0_Vie_Systeme_39_Chiffrement_Des_Flux_Pki

- **Environnement** : Serveur de stockage TrueNAS CORE 13.0 (FreeBSD)
- **OS / Version** : TrueNAS CORE 13.0; étape 39 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `truenascore130`, `vie-du-systeme`, `cycle-de-vie`, `etape-39`

---

## Problème précis à résoudre

Installer un certificat valide.

## 1. Hors-Production (Lab / Test / POC)

1. GUI : Système > Certificats > Ajouter > Importer un certificat (ou CSR).
   ```sh
   midclt call certificate.query | grep -E 'name|until'
   ```
   👉 Explication : liste certificats et expiration.

2. Appliquer : Système > Général > Certificat HTTPS de l'interface web.
   ```sh
   midclt call system.general.update '{"ui_certificate": ID_CERT}'
   ```
   👉 Explication : ID_CERT est l'identifiant dans la liste.

3. Tester :
   ```sh
   openssl s_client -connect NOM_NAS:443 </dev/null 2>/dev/null | openssl x509 -noout -dates -subject
   ```
   👉 Explication : émetteur et dates.

## 2. Production — Contrôles

PKI interne ; surveiller l'expiration.

## 3. Production — Sécurité

Forcer HTTPS ; désactiver TLS 1.0/1.1.

## Validation et retour arrière

- **Validation** : Pas d'erreur du navigateur.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire TrueNAS CORE 13.0](/01-fiches-simples/truenas/core-13-0/vie-du-systeme/sommaire-vie-du-systeme-truenas-core-13-0)
- [Documentation officielle](https://www.truenas.com/docs/core/)