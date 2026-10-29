---
title: "Fiche Simple - VM OPNsense Vie Systeme 48 Test De Restauration Pra"
description: "Prouver que la sauvegarde est restaurable."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-48"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_48_Test_De_Restauration_Pra

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 48 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-48`

---

## Problème précis à résoudre

Prouver que la sauvegarde est restaurable.

## 1. Hors-Production (Lab / Test / POC)

1. Installer un OPNsense de test, puis Système > Configuration > Sauvegardes > Restaurer : choisir le fichier, saisir `MOT_DE_PASSE_SAUVEGARDE`, cocher les zones à restaurer, Restaurer, redémarrer.
   👉 Explication : recrée la configuration sur une machine propre.

2. En console, option 13 (« Restore a backup ») pour revenir à une copie de `/conf/backup`, ou en shell :
   ```sh
   ls -lt /conf/backup | head
   cp /root/config-DATE.xml /conf/config.xml
   configctl service reload all
   ```
   👉 Explication : `DATE` est la date de la copie; recharge les services avec la configuration restaurée.

3. Vérifier les interfaces, règles et VPN après restauration.
   👉 Explication : confirme que la sauvegarde est complète.

## 2. Production — Contrôles

Faire ce test au moins annuellement et noter la durée.

## 3. Production — Sécurité

Détruire la machine de test et ses copies de configuration après l'exercice.

## Validation et retour arrière

- **Validation** : Le pare-feu restauré a les mêmes règles et interfaces.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)