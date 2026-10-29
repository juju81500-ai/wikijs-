---
title: "Fiche Simple - VM Ubuntu 24.04 Vie Systeme 49 Enregistrement Cmdb Et Gestion"
description: "Inscrire la machine dans l'inventaire."
published: true
date: 2026-10-29T20:22:10Z
tags: ["ubuntu2404", "vie-du-systeme", "cycle-de-vie", "etape-49"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_Ubuntu_24.04_Vie_Systeme_49_Enregistrement_Cmdb_Et_Gestion

- **Environnement** : VM Ubuntu Server 24.04 LTS « noble »
- **OS / Version** : Ubuntu 24.04; étape 49 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `ubuntu2404`, `vie-du-systeme`, `cycle-de-vie`, `etape-49`

---

## Problème précis à résoudre

Inscrire la machine dans l'inventaire.

## 1. Hors-Production (Lab / Test / POC)

1. Relever les informations à saisir :
   ```bash
   hostnamectl
   ip -br address
   lsb_release -a
   pro status
   sudo dmidecode -s system-serial-number 2>/dev/null
   ```
   👉 Explication : nom, IP, version, statut Ubuntu Pro et numéro de série pour GLPI ou NetBox.

2. Enregistrer les secrets dans le coffre (Vaultwarden, KeePass ou Vault) et réserver l'IP dans l'IPAM.
   👉 Explication : aucun mot de passe ne reste dans un fichier ou un ticket.

## 2. Production — Contrôles

Renseigner propriétaire, criticité et date de fin de vie (fin du support standard de la LTS).

## 3. Production — Sécurité

Accès au coffre nominatif et journalisé.

## Validation et retour arrière

- **Validation** : La machine est visible dans la CMDB.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire Ubuntu 24.04](/01-fiches-simples/ubuntu/24-04/vie-du-systeme/sommaire-vie-du-systeme-ubuntu-24-04)
- [Documentation officielle](https://documentation.ubuntu.com/server/)