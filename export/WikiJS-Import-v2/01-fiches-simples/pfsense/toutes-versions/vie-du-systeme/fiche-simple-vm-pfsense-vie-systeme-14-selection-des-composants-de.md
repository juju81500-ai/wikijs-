---
title: "Fiche Simple - VM pfSense Vie Systeme 14 Selection Des Composants De"
description: "Installer uniquement ce qui est nécessaire."
published: true
date: 2026-10-29T20:22:10Z
tags: ["pfsense", "vie-du-systeme", "cycle-de-vie", "etape-14"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_pfSense_Vie_Systeme_14_Selection_Des_Composants_De

- **Environnement** : Pare-feu pfSense CE (VM ou matériel)
- **OS / Version** : pfSense CE; étape 14 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `pfsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-14`

---

## Problème précis à résoudre

Installer uniquement ce qui est nécessaire.

## 1. Hors-Production (Lab / Test / POC)

1. Lancer l'installateur (`Install`, accepter la licence) : le système de base est copié sans choix de paquets.
   👉 Explication : pfSense CE s'installe en un bloc complet.

2. Ajouter ensuite seulement les paquets utiles dans System > Package Manager > Available Packages (ex. `qemu-guest-agent`). En shell :
   ```sh
   pkg-static info | wc -l
   pkg-static info | grep -i pfSense-pkg
   ```
   👉 Explication : compte les paquets et liste les paquets pfSense additionnels.

## 2. Production — Contrôles

Tenir la liste des paquets autorisés et la déclarer à la CMDB.

## 3. Production — Sécurité

Chaque paquet ajoute de la surface d'attaque; ne pas installer de paquet non justifié.

## Validation et retour arrière

- **Validation** : La liste des paquets correspond au besoin.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire pfSense CE](/01-fiches-simples/pfsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-pfsense)
- [Documentation officielle](https://docs.netgate.com/pfsense/en/latest/)