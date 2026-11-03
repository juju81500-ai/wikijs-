---
title: "Fiche Simple - VM OPNsense Vie Systeme 11 Compte D Administration Delegue"
description: "Éviter l'usage quotidien de root."
published: true
date: 2026-11-03T09:36:13Z
tags: ["opnsense", "vie-du-systeme", "cycle-de-vie", "etape-11"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# Fiche_Simple_-_VM_OPNsense_Vie_Systeme_11_Compte_D_Administration_Delegue

- **Environnement** : Pare-feu OPNsense ([[Glossary:VM]] ou matériel)
- **OS / Version** : OPNsense; étape 11 sur 50 de la vie du système
- **Catégorie** : vie du système / cycle de vie
- **Tags** : `opnsense`, `vie-du-systeme`, `cycle-de-vie`, `etape-11`

---

## Problème précis à résoudre

Éviter l'usage quotidien de `root`.

## 1. Hors-Production (Lab / Test / POC)

1. Créer un groupe dans Système > Accès > Groupes (ex. `admins-fw`) et lui donner les privilèges (ex. Tous les privilèges de pages ou un jeu limité).
   👉 Explication : les droits sont attribués au groupe, pas aux personnes.

2. Créer l'utilisateur dans Système > Accès > Utilisateurs > Ajouter : nom `ADMIN01`, mot de passe fort, appartenance au groupe; cocher « Shell autorisé » si l'accès [[Glossary:SSH]] est requis.
   👉 Explication : `ADMIN01` est le compte nominatif de l'administrateur.

3. Contrôler le compte en shell :
   ```sh
   pw usershow ADMIN01
   id ADMIN01
   ```
   👉 Explication : affiche l'UID, le shell et les groupes du compte.

## 2. Production — Contrôles

Un compte nominatif par administrateur, jamais de compte partagé.

## 3. Production — Sécurité

Appliquer le moindre privilège et supprimer le compte à son départ de l'équipe.

## Validation et retour arrière

- **Validation** : Connexion web et SSH réussies avec `ADMIN01`.
- **Retour arrière** : restaurer le snapshot ou la sauvegarde pris avant l'étape; consigner l'écart avant de poursuivre.

## Si le problème n'est pas résolu

- [Vie du système : les 50 étapes, tous OS](/fr/00-administration/01-gouvernance-architecture/vie-du-systeme)
- [Sommaire OPNsense](/fr/01-fiches-simples/opnsense/toutes-versions/vie-du-systeme/sommaire-vie-du-systeme-opnsense)
- [Documentation officielle](https://docs.opnsense.org/)