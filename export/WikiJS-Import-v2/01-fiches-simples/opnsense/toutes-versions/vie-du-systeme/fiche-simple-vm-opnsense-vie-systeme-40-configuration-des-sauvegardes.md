---
title: "Fiche Simple - VM OPNsense Vie Systeme 40 Configuration Des Sauvegardes"
description: "Sauvegarder la configuration (config.xml)."
published: true
date: 2026-10-29T20:22:10Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-40"]
editor: markdown
dateCreated: 2026-10-29T20:22:10Z
dateModified: 2026-10-29T20:22:10Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_40_Configuration_Des_Sauvegardes

- **Environnement** : Pare-feu OPNsense (VM ou matériel)
- **OS / Version** : OPNsense; étape 40 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-40`

---

## Problème précis à résoudre

Sauvegarder la configuration (`config.xml`).

## 1. Hors-Production (Lab / Test / POC)

1. Aller dans Système > Configuration > Sauvegardes > Télécharger la configuration, cocher « Chiffrer ce fichier de configuration » et saisir un mot de passe `MOT_DE_PASSE_SAUVEGARDE`.
   👉 Explication : le fichier XML chiffré peut être stocké hors du pare-feu.

2. Ou en shell, copier la configuration vers un serveur de sauvegarde :
   ```sh
   cp /conf/config.xml /root/config-$(date +%Y%m%d).xml
   scp /conf/config.xml SAUVEUR@IP_SAUVEGARDE:/sauvegardes/fw01/
   ```
   👉 Explication : `SAUVEUR` et `IP_SAUVEGARDE` désignent le compte et le serveur de sauvegarde.

3. Activer une sauvegarde automatique à chaque changement via Système > Configuration > Sauvegardes (plugin `os-git-backup` ou `os-nextcloud-backup`).
   👉 Explication : chaque modification est conservée hors du pare-feu.

## 2. Production — Contrôles

Conserver plusieurs générations et tester la restauration (étape 48).

## 3. Production — Sécurité

Chiffrer les sauvegardes et restreindre l'accès : elles contiennent mots de passe et clés.

## Validation et retour arrière

- **Validation** : Fichier créé, chiffré et copié hors du pare-feu.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/00-administration/vie-du-systeme)
- [Sommaire OPNsense](/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)