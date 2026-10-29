---
title: "Fiche Simple - VM OPNsense Config Verifier"
description: "S'assurer que l'export est exploitable et hors appliance."
published: true
date: 2026-10-29T20:22:42Z
tags: ["opnsense", "sauvegarde", "configuration", "verification", "snapshot"]
editor: markdown
dateCreated: 2026-10-29T20:22:42Z
dateModified: 2026-10-29T20:22:42Z
---

# Fiche_Simple_-_VM_OPNsense_Config_Verifier.md

- **Environnement** : Appliance OPNsense physique ou virtuelle, seule ou en HA
- **OS / Version** : OPNsense Community ou Business Edition maintenue
- **Catégorie** : pare-feu / sauvegarde-restauration
- **Tags** : `opnsense`, `sauvegarde`, `configuration`, `verification`, `snapshot`

---

## Problème précis à résoudre

S'assurer que l'export est exploitable et hors appliance.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier date, taille, version source et appareil concerné dans le nom et les métadonnées du fichier.
   👉 Explication : un export sans traçabilité est difficile à exploiter.

2. Confirmer que le mot de passe est conservé dans le coffre.
   👉 Explication : sans lui, l'export est inutilisable.

3. Copier la sauvegarde hors de l'appliance et de son stockage local.
   👉 Explication : la perte de l'appliance ne doit pas détruire la sauvegarde.

4. Tester périodiquement la restauration sur une VM ou appliance isolée de même version.
   👉 Explication : seule une restauration testée prouve la sauvegarde.

5. Option : **System > Snapshots** pour un retour arrière local sur ZFS.
   👉 Explication : un snapshot accélère un retour local mais ne remplace pas l'export hors appliance.

## 2. Production — Contrôles

Planifier le test de restauration et définir la rétention.

## 3. Production — Sécurité

- Chiffrer les copies hors appliance.

## Validation et retour arrière

- **Validation** : Export lisible sur une appliance de test de même version.
- **Retour arrière** : Supprimer la VM de test.

## Si le problème n'est pas résolu

- [OPNsense — Sauvegardes de configuration](https://docs.opnsense.org/manual/backups.html)
- [OPNsense — Snapshots système](https://docs.opnsense.org/manual/snapshots.html)
- [Guide complet — vérifier la sauvegarde](/02-fiches-completes/opnsense/toutes-versions/autres/36-sauvegarde-restauration-configuration-opnsense#3-verifier-la-sauvegarde)