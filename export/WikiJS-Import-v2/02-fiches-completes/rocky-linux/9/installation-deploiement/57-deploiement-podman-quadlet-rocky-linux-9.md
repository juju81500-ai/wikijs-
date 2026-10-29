---
title: "Déployer un service rootless avec Podman Quadlet sur Rocky Linux 9"
description: "Fiche simple : [préparer le compte et l'hôte](../../../../01-Fiches-Simples/Rocky-Linux/9/Vie-du-logiciel/Podman/FicheSimple-VMRocky9PodmanQuadletPreparerCompteHote.md)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["podman", "quadlet", "rocky9", "rootless", "systemd", "conteneurs"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Déployer un service rootless avec Podman Quadlet sur Rocky Linux 9

- **OS / Version** : Rocky Linux 9, systemd, Podman fourni par les dépôts maintenus
- **Type de fiche** : Installation/Déploiement
- **Périmètre** : Un service de conteneur rootless géré par Quadlet, pilote local
- **Catégorie** : Conteneurs / exploitation
- **Tags** : `podman`, `quadlet`, `rocky9`, `rootless`, `systemd`, `conteneurs`

## 1. Préparer le compte et l'hôte

Fiche simple : [préparer le compte et l'hôte](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/podman/fiche-simple-vm-rocky-9-podman-quadlet-preparer-compte-hote).

Choisir un compte de service dédié, propriétaire des volumes et unités user. Vérifier cgroups v2, versions de Podman/Quadlet, `fuse-overlayfs`, `slirp4netns`/`pasta`, espace disque et plages UID/GID. Rootless utilise des espaces de noms utilisateur; ses conteneurs ne sont pas visibles depuis le Podman root.

```bash
sudo dnf install -y podman fuse-overlayfs slirp4netns
podman --version
podman info --format '{{.Host.CgroupsVersion}}'
```

Si nécessaire et après vérification des plages existantes, attribuer au compte Podman des plages subuid/subgid libres. Ne pas ajouter des plages en doublon ou qui recouvrent des identifiants déjà utilisés.

## 2. Valider une image en laboratoire

Fiche simple : [valider une image en laboratoire](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/podman/fiche-simple-vm-rocky-9-podman-quadlet-valider-image).

Choisir une image officielle avec registre entièrement qualifié et version ou digest piné. Vérifier provenance/signature selon la politique interne, lire le Containerfile et tester configuration, ports et stockage avant déploiement.

```bash
sudo -iu <compte-podman> podman pull <registre>/<organisation>/<image>:<version>
sudo -iu <compte-podman> podman image inspect <registre>/<organisation>/<image>:<version>
```

Éviter `latest` en production. Tester une commande `podman run` temporaire avec volume dédié et ports liés seulement à l'adresse nécessaire; ne jamais monter le socket Podman ou le système racine du host dans le conteneur.

## 3. Déclarer le service Quadlet

Fiche simple : [déclarer le service Quadlet](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/podman/fiche-simple-vm-rocky-9-podman-quadlet-declarer-service).

Placer le fichier `.container` dans le chemin utilisateur `~/.config/containers/systemd/`. Définir `[Unit]`, `[Container]` et `[Service]`; utiliser `Image=` avec référence pinée, `User=` si l'image le permet, `ReadOnly=true` si compatible, `DropCapability=all` avec seulement les exceptions justifiées, `NoNewPrivileges=true`, `Memory=`, `PidsLimit=`, volumes dédiés, secrets Podman et `PublishPort=` limité.

Ajouter `[Install]` avec la cible user attendue. Quadlet transforme les fichiers en unités systemd; les conteneurs rootless utilisent le gestionnaire systemd utilisateur. Après validation, charger et démarrer l'unité avec `systemctl --user daemon-reload` et `systemctl --user start <nom>.service`. Pour démarrer au boot sans session interactive, activer `loginctl enable-linger <compte-podman>` selon la politique du serveur.

Ne pas utiliser `systemctl enable` directement comme pour un service normal généré de façon transitoire : Quadlet applique les clés `[Install]` quand il génère l'unité.

## 4. Vérifier et exposer le service

Fiche simple : [vérifier et exposer le service](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/podman/fiche-simple-vm-rocky-9-podman-quadlet-verifier-exposer).

```bash
sudo -iu <compte-podman> systemctl --user --no-pager status <nom>.service
sudo -iu <compte-podman> podman ps
sudo -iu <compte-podman> journalctl --user -u <nom>.service -b --no-pager
```

Vérifier la santé applicative, le mapping de port, les droits sur volume, l'état SELinux et les journaux. Ne pas désactiver SELinux pour faire fonctionner le conteneur; corriger l'étiquetage/volume et la politique nécessaires.

## 5. Mise à jour et reprise

Fiche simple : [mise à jour et reprise](/01-fiches-simples/rocky-linux/9/vie-du-logiciel/podman/fiche-simple-vm-rocky-9-podman-quadlet-mise-a-jour-reprise).

Épingler une nouvelle image après recette, garder la version précédente pour rollback, puis mettre à jour le Quadlet et redémarrer proprement. Utiliser `podman auto-update` uniquement si les tags/signatures et fenêtres de déploiement sont gérés. Sauvegarder les données persistantes séparément des couches d'image, tester la restauration et surveiller consommation, espace, état de santé et mises à jour de sécurité.

## Sources

- [Podman — Référence CLI](https://docs.podman.io/en/latest/markdown/podman.1.html)
- [Podman — Quadlet et unités systemd](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)
- [Podman — Introduction](https://docs.podman.io/en/latest/Introduction.html)
- [Rocky Linux — Documentation officielle](https://docs.rockylinux.org/)