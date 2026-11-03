---
title: "Fiche Simple - VM Ubuntu 26.04 Vie Systeme 43 Controle Des Services Et"
description: "Vérifier l'état de service."
published: true
date: 2026-11-03T09:36:13Z
tags: ["ubuntu2604", "vie-du-systeme", "cycle-de-vie", "etape-43"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_VM_Ubuntu_26.04_Vie_Systeme_43_Controle_Des_Services_Et

- **Environnement** : VM Ubuntu Server 26-04 LTS
- **OS / Version** : Ubuntu 26-04; étape 43 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2604`, `vie-du-systeme`, `cycle-de-vie`, `etape-43`

---

## Problème précis à résoudre

Vérifier l'état de service.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler :
   ```bash
   systemctl --failed
   sudo ss -tulpn
   ```
   👉 Explication : aucun service en échec et seulement les ports prévus.

## 2. Production — Contrôles

Comparer à l'inventaire des ports du dossier.

## 3. Production — Sécurité

Tout port non documenté est un écart.

## Validation et retour arrière

- **Validation** : `systemctl --failed` : 0 unité.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire Ubuntu 26-04](/fr/01-fiches-simples/ubuntu/26-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-26-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)