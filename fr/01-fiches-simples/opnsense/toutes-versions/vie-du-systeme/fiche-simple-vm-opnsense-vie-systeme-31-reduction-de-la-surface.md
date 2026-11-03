---
title: "Fiche Simple - VM OPNsense Vie Systeme 31 Reduction De La Surface"
description: "Désactiver les services inutiles."
published: true
date: 2026-11-03T14:22:28Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-31"]
editor: markdown
dateCreated: 2026-11-03T14:22:28Z
dateModified: 2026-11-03T14:22:28Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_31_Reduction_De_La_Surface

- **Environnement** : Pare-feu OPNsense ([[Glossary:VM]] ou matériel)
- **OS / Version** : OPNsense; étape 31 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-31`

---

## Problème précis à résoudre

Désactiver les services inutiles.

## 1. Hors-Production (Lab / Test / POC)

1. Vérifier les services actifs dans Lobby > Tableau de bord (widget Services) et dans chaque menu Services; désactiver [[Glossary:DHCP]], Unbound ou [[Glossary:SSH]] s'ils ne servent pas.
   👉 Explication : moins de services signifie moins de vulnérabilités.

2. Lister les ports en écoute :
   ```sh
   sockstat -4 -6 -l
   configctl service list 2>/dev/null | head -30
   ```
   👉 Explication : montre les services à l'écoute et les services gérés par OPNsense.

3. Retirer les plugins non utilisés dans Système > Micrologiciel > Plugins > Désinstaller.
   👉 Explication : supprime des composants inutiles.

## 2. Production — Contrôles

Comparer la liste à la baseline à chaque revue.

## 3. Production — Sécurité

Aucun service d'administration ne doit écouter sur le [[Glossary:WAN]].

## Validation et retour arrière

- **Validation** : Seuls les ports prévus sont à l'écoute.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire OPNsense](/fr/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)