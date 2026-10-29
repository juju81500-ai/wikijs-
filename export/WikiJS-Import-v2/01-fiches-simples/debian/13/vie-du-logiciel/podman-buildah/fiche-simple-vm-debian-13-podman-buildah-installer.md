---
title: "Fiche Simple - VM Debian 13 Podman Buildah Installer"
description: "Installer Podman et Buildah sur Debian 13 Trixie depuis les dépôts de la distribution."
published: true
date: 2026-10-29T20:59:00Z
tags: ["debian13", "podman", "buildah", "conteneurs", "rootless", "oci"]
editor: markdown
dateCreated: 2026-10-29T20:59:00Z
dateModified: 2026-10-29T20:59:00Z
---

# Fiche_Simple_-_VM_Debian_13_Podman_Buildah_Installer

- **Environnement** : VM Debian 13 de laboratoire, utilisateur sudoer et compte de service dédié
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : conteneurs
- **Tags** : `debian13`, `podman`, `buildah`, `conteneurs`, `rootless`, `oci`

---

## Problème précis à résoudre

Installer Podman et Buildah sur Debian 13 Trixie depuis les dépôts de la distribution.

## 1. Hors-Production (Lab / Test / POC)

1. Installer les paquets :
   ```bash
   sudo apt update
   sudo apt install -y podman buildah
   ```
   👉 Explication : installe Podman (exécution) et Buildah (construction) ; les dépendances rootless (`uidmap`, runtime OCI, réseau) sont tirées par le paquet ou recommandées : vérifier avec `apt-cache depends podman`.

2. Contrôler les versions et l'origine :
   ```bash
   podman --version
   buildah --version
   apt-cache policy podman buildah
   ```
   👉 Explication : comparer aux versions approuvées.

3. En utilisateur non privilégié, contrôler le mode rootless :
   ```bash
   podman info --format '{{.Host.Security.Rootless}} {{.Host.OCIRuntime.Name}} {{.Store.GraphDriverName}}'
   ```
   👉 Explication : attendu : `true`, un runtime (`crun` ou `runc`) et un pilote de stockage ; les champs peuvent varier selon la version.

## 2. Production — Contrôles

Installer depuis le dépôt distribution uniquement, sur pilote d'abord. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Ne pas ajouter de dépôt tiers non revu.
- Ne pas ajouter l'utilisateur à un groupe privilégié pour Podman.

## Validation et retour arrière

- **Validation** : `podman --version` et `buildah --version` répondent et `Rootless` vaut `true`.
- **Retour arrière** : `sudo apt remove podman buildah` puis `podman system reset` (supprime toutes les données du compte) seulement si l'on veut repartir de zéro.

## Si le problème n'est pas résolu

- [Podman — documentation officielle](https://docs.podman.io/en/latest/)
- [Podman — installation](https://podman.io/docs/installation)
- [Fiche connexe — Prerequis Limites](/01-fiches-simples/debian/13/vie-du-logiciel/podman-buildah/fiche-simple-vm-debian-13-podman-buildah-prerequis-limites)