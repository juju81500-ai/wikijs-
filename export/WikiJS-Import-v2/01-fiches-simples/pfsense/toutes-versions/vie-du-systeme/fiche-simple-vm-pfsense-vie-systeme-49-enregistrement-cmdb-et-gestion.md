---
title: "Fiche Simple - VM pfSense Vie Systeme 49 Enregistrement Cmdb Et Gestion"
description: "Déclarer le pare-feu dans l'inventaire."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-49"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_49_Enregistrement_Cmdb_Et_Gestion

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 49 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-49`

---

## Problème précis à résoudre

Déclarer le pare-feu dans l'inventaire.

## 1. Hors-Production (Lab / Test / POC)

1. Créer la fiche CMDB : nom, FQDN, adresses WAN/LAN, version, interfaces, rôle, propriétaire, criticité, lien vers la sauvegarde.
   👉 Explication : rend le pare-feu identifiable pour les équipes.

2. Exporter les informations techniques :
   ```sh
   cat /etc/version
   hostname
   ifconfig | grep -E '^[a-z]|inet '
   sha256 /cf/conf/config.xml
   ```
   👉 Explication : version, nom, adresses et empreinte de la configuration à saisir dans la CMDB.

3. Valider la liste des comptes dans System > User Manager.
   👉 Explication : chaque compte doit être rattaché à une personne ou un outil.

## 2. Production — Contrôles

Mettre à jour la CMDB à chaque changement majeur.

## 3. Production — Sécurité

Revue périodique des comptes et secrets.

## Validation et retour arrière

- **Validation** : Fiche CMDB complète et comptes validés.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)