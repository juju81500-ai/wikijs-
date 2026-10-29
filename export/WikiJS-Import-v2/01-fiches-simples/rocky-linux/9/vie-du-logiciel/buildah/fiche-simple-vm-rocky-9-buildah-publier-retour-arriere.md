---
title: "Fiche Simple - VM Rocky 9 Buildah Publier Retour Arriere"
description: "Publier un tag immuable vers le registre interne."
published: true
date: 2026-10-29T20:14:10Z
tags: ["buildah", "oci", "rocky9", "rootless", "containerfile", "registre"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Rocky_9_Buildah_Publier_Retour_Arriere.md

- **Environnement** : VM Rocky Linux 9 de build, compte non privilégié dédié
- **OS / Version** : Rocky Linux 9; paquet Buildah des dépôts de la distribution
- **Catégorie** : conteneurs / chaîne de build
- **Tags** : `buildah`, `oci`, `rocky9`, `rootless`, `containerfile`, `registre`

---

## Problème précis à résoudre

Publier un tag immuable vers le registre interne.

## 1. Hors-Production (Lab / Test / POC)

1. S'authentifier (le mot de passe est saisi de façon interactive; REGISTRE à remplacer) :
   ```bash
   buildah login REGISTRE
   ```
   👉 Explication : aucun mot de passe en argument.

2. Publier le tag (REGISTRE, PROJET, APPLICATION, VERSION à remplacer) :
   ```bash
   buildah push localhost/APPLICATION:VERSION docker://REGISTRE/PROJET/APPLICATION:VERSION
   ```
   👉 Explication : un tag immuable par version permet un retour arrière fiable.

## 2. Production — Contrôles

Conserver au moins la version précédente dans le registre et une archive OCI de la version déployée.

## 3. Production — Sécurité

- Ne pas réécrire un tag déjà utilisé en production.
- Ne pas saisir de mot de passe en argument de commande.

## Validation et retour arrière

- **Validation** : Le tag est présent dans le registre.
- **Retour arrière** : Redéployer le tag précédent ou son digest.

## Si le problème n'est pas résolu

- [Buildah — Installation](https://github.com/containers/buildah/blob/main/install.md)
- [Buildah — buildah-build](https://github.com/containers/buildah/blob/main/docs/buildah-build.1.md)
- [Guide complet Buildah Rocky Linux 9](/02-fiches-completes/rocky-linux/9/installation-deploiement/87-construction-images-oci-buildah-rocky-linux-9#6-publier-et-revenir-en-arriere)