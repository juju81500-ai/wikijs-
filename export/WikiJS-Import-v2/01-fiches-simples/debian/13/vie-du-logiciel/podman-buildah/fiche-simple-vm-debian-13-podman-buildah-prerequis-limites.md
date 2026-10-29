---
title: "Fiche Simple - VM Debian 13 Podman Buildah Prerequis Limites"
description: "Cadrer Podman et Buildah sur Debian 13 Trixie : version, rootless, cgroups, réseau."
published: true
date: 2026-10-29T20:59:00Z
tags: ["debian13", "podman", "buildah", "conteneurs", "rootless", "oci"]
editor: markdown
dateCreated: 2026-10-29T20:59:00Z
dateModified: 2026-10-29T20:59:00Z
---

# Fiche_Simple_-_VM_Debian_13_Podman_Buildah_Prerequis_Limites

- **Environnement** : VM Debian 13 de laboratoire, utilisateur sudoer et compte de service dédié
- **OS / Version** : Debian 13 Trixie
- **Catégorie** : conteneurs
- **Tags** : `debian13`, `podman`, `buildah`, `conteneurs`, `rootless`, `oci`

---

## Problème précis à résoudre

Cadrer Podman et Buildah sur Debian 13 Trixie : version, rootless, cgroups, réseau.

## 1. Hors-Production (Lab / Test / POC)

1. Relever l'OS, le noyau et la version de cgroups :
   ```bash
   cat /etc/os-release
   uname -r
   stat -fc %T /sys/fs/cgroup
   ```
   👉 Explication : `cgroup2fs` indique cgroups v2, requis pour les limites de ressources en rootless.

2. Identifier les versions disponibles dans le dépôt :
   ```bash
   apt-cache policy podman buildah
   ```
   👉 Explication : Podman et Buildah proviennent du dépôt Debian ; leur version (série 5.x pour Podman sur Debian 13) est à vérifier avec `podman --version`.

3. Prévoir un compte de service non privilégié et ses plages subuid/subgid (UTILISATEUR à remplacer) :
   ```bash
   grep UTILISATEUR /etc/subuid /etc/subgid
   ```
   👉 Explication : le mode rootless utilise des UID/GID subordonnés ; l'absence de ligne est traitée dans la fiche Configurer.

4. Retenir les limites du rootless :
   👉 Explication : pas de port inférieur à 1024 par défaut (`net.ipv4.ip_unprivileged_port_start`), réseau en espace utilisateur (pasta ou slirp4netns selon version), stockage dans le répertoire du compte ; pas de daemon contrairement à Docker.

## 2. Production — Contrôles

Valider version, registres autorisés et compte de service avec l'équipe sécurité. Commandes établies d'après la documentation officielle et non testées dans ce pack : à valider en lab avant toute production.

## 3. Production — Sécurité

- Ne pas utiliser root pour exécuter les conteneurs applicatifs.
- Pas de secret dans les images ni les variables d'environnement visibles.

## Validation et retour arrière

- **Validation** : version, cgroups et compte de service documentés.
- **Retour arrière** : aucune modification n'est faite par cette fiche.

## Si le problème n'est pas résolu

- [Podman — documentation officielle](https://docs.podman.io/en/latest/)
- [Podman — installation](https://podman.io/docs/installation)