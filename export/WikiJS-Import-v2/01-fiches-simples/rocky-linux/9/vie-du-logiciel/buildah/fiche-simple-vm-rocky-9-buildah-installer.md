---
title: "Fiche Simple - VM Rocky 9 Buildah Installer"
description: "Installer Buildah depuis les dépôts de la distribution."
published: true
date: 2026-10-29T20:14:10Z
tags: ["buildah", "oci", "rocky9", "rootless", "containerfile", "registre"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Rocky_9_Buildah_Installer.md

- **Environnement** : VM Rocky Linux 9 de build, compte non privilégié dédié
- **OS / Version** : Rocky Linux 9; paquet Buildah des dépôts de la distribution
- **Catégorie** : conteneurs / chaîne de build
- **Tags** : `buildah`, `oci`, `rocky9`, `rootless`, `containerfile`, `registre`

---

## Problème précis à résoudre

Installer Buildah depuis les dépôts de la distribution.

## 1. Hors-Production (Lab / Test / POC)

1. Contrôler la version proposée puis installer :
   ```bash
   dnf info buildah
   sudo dnf install -y buildah
   buildah --version
   buildah info
   ```
   👉 Explication : le paquet installe aussi `runc`/`crun`; ne pas compiler depuis les sources en production sans besoin documenté.

2. Contrôler les plages d'identifiants du compte :
   ```bash
   grep "^$USER:" /etc/subuid /etc/subgid
   ```
   👉 Explication : si elles manquent, utiliser les plages libres décidées par l'administrateur (voir `man subuid`), sans dupliquer celles d'autres comptes.

3. Si Podman est installé, appliquer les nouvelles plages (ou rouvrir la session) :
   ```bash
   podman system migrate
   ```
   👉 Explication : cette commande recharge la configuration rootless de Podman.

## 2. Production — Contrôles

Mettre à jour régulièrement le paquet.

## 3. Production — Sécurité

- Ne pas dupliquer les plages subuid/subgid.
- Installer uniquement depuis les dépôts approuvés.

## Validation et retour arrière

- **Validation** : `buildah --version` répond et `buildah info` s'exécute sans erreur.
- **Retour arrière** : `sudo dnf remove buildah` ou réinstaller la version précédente du dépôt interne, puis restaurer `/etc/containers` depuis la copie de l'étape 2.

## Si le problème n'est pas résolu

- [Buildah — Installation](https://github.com/containers/buildah/blob/main/install.md)
- [Buildah — buildah-build](https://github.com/containers/buildah/blob/main/docs/buildah-build.1.md)
- [Guide complet Buildah Rocky Linux 9](/02-fiches-completes/rocky-linux/9/installation-deploiement/87-construction-images-oci-buildah-rocky-linux-9#3-installer-buildah)