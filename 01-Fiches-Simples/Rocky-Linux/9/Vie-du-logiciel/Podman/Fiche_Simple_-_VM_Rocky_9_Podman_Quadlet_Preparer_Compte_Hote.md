# Fiche_Simple_-_VM_Rocky_9_Podman_Quadlet_Preparer_Compte_Hote.md

- **Environnement** : VM Rocky Linux 9 avec Podman rootless, systemd et Quadlet (pilote local)
- **OS / Version** : Rocky Linux 9; Podman des dépôts maintenus
- **Catégorie** : conteneurs / préparation
- **Tags** : `rocky9`, `podman`, `quadlet`, `rootless`, `systemd`, `subuid`, `cgroups`

---

## Problème précis à résoudre

Préparer l'hôte et un compte de service pour Podman rootless (`svcpodman` est un nom d'exemple à remplacer).

## 1. Hors-Production (Lab / Test / POC)

1. Installer les composants :
   ```bash
   sudo dnf install -y podman fuse-overlayfs slirp4netns
   ```
   👉 Explication : Podman et les outils réseau/stockage rootless.

2. Contrôler versions et cgroups :
   ```bash
   podman --version
   podman info --format '{{.Host.CgroupsVersion}}'
   ```
   👉 Explication : cgroups v2 est attendu.

3. Contrôler les plages subuid/subgid existantes avant d'en ajouter :
   ```bash
   grep svcpodman /etc/subuid /etc/subgid
   ```
   👉 Explication : ne pas ajouter de plages en doublon ou qui recouvrent d'autres identifiants.

## 2. Production — Contrôles

Choisir un compte de service dédié propriétaire des volumes et unités user; vérifier espace disque et plages UID/GID.

## 3. Production — Sécurité

- Les conteneurs rootless ne sont pas visibles depuis le Podman root.

## Validation et retour arrière

- **Validation** : Podman répond et cgroups v2 est confirmé.
- **Retour arrière** : `sudo dnf remove podman fuse-overlayfs slirp4netns` si l'hôte doit revenir à l'état initial.

## Si le problème n'est pas résolu

- [Podman — Quadlet et unités systemd](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)
- [Podman — référence CLI](https://docs.podman.io/en/latest/markdown/podman.1.html)
- [Guide complet Podman Quadlet Rocky Linux 9](../../../../../02-Fiches-Completes/Rocky-Linux/9/Installation-Deploiement/57_Deploiement_Podman_Quadlet_Rocky_Linux_9.md#1-preparer-le-compte-et-lhote)
