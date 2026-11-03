---
title: "fiche-simple-truenas-core-13-0-deploiement-validation"
description: "Contrôler que pool, partage, snapshots, configuration et alertes sont opérationnels."
published: true
date: 2026-11-03T09:36:13Z
tags: ["truenas-core", "truenas", "freebsd", "zfs", "smb", "nas"]
editor: markdown
dateCreated: 2026-11-03T09:36:13Z
dateModified: 2026-11-03T09:36:13Z
---

# fiche-simple-truenas-core-13-0-deploiement-validation.md

- **Environnement** : Appliance TrueNAS CORE (FreeBSD) en [[Glossary:VM]] de laboratoire ou [[Glossary:NAS]] existant
- **OS / Version** : TrueNAS CORE, branche 13.0 (build exact à relever sur l'ISO)
- **Catégorie** : stockage NAS / validation
- **Tags** : `truenas-core`, `truenas`, `freebsd`, `zfs`, `smb`, `nas`

---

## Problème précis à résoudre

Contrôler que pool, partage, snapshots, configuration et alertes sont opérationnels.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler l'état du pool dans **Storage > Pools** et dans le Shell :
   ```sh
   zpool status
   ```
   👉 Explication : aucune erreur ne doit apparaître.

2. Tester l'accès SMB avec le compte de service puis avec un utilisateur non autorisé.
   👉 Explication : le second doit être refusé.

3. Vérifier l'existence du snapshot et la récupération d'un fichier via un clone.
   👉 Explication : prouve que la restauration fonctionne.

4. **System > General > Save Config**, stocker le `.db` hors du NAS.
   👉 Explication : la configuration est récupérable.

5. Configurer l'e-mail d'alerte et envoyer un test.
   👉 Explication : garantit que les alertes arrivent.

## 2. Production — Contrôles

Consigner les résultats de la recette.

## 3. Production — Sécurité

- Contenu du fichier de configuration non exposé.

## Validation et retour arrière

- **Validation** : Tous les contrôles ci-dessus passent.
- **Retour arrière** : Aucune modification ici.

## Si le problème n'est pas résolu

- [TrueNAS — documentation CORE 13.0](https://www.truenas.com/docs/core/13.0/)
- [TrueNAS — Software Status](https://www.truenas.com/docs/softwarestatus/)
- [Guide complet — 6. Validation](/fr/02-fiches-completes/truenas/core-13-0/installation-deploiement/89-deploiement-truenas-core-13-0#6-validation)