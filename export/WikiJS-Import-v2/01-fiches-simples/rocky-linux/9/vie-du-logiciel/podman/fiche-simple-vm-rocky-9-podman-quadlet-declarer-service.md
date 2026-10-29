---
title: "Fiche Simple - VM Rocky 9 Podman Quadlet Declarer Service"
description: "Écrire le fichier .container et démarrer l'unité utilisateur (monservice est un nom d'exemple)."
published: true
date: 2026-10-29T20:14:10Z
tags: ["rocky9", "podman", "quadlet", "rootless", "systemd", "container-unit", "linger"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Rocky_9_Podman_Quadlet_Declarer_Service.md

- **Environnement** : VM Rocky Linux 9 avec Podman rootless, systemd et Quadlet (pilote local)
- **OS / Version** : Rocky Linux 9; Podman des dépôts maintenus
- **Catégorie** : conteneurs / quadlet
- **Tags** : `rocky9`, `podman`, `quadlet`, `rootless`, `systemd`, `container-unit`, `linger`

---

## Problème précis à résoudre

Écrire le fichier `.container` et démarrer l'unité utilisateur (`monservice` est un nom d'exemple).

## 1. Hors-Production (Lab / Test / POC)

1. Créer le répertoire Quadlet du compte :
   ```bash
   sudo -iu svcpodman mkdir -p ~/.config/containers/systemd
   ```
   👉 Explication : chemin utilisateur lu par Quadlet.

2. Créer `~/.config/containers/systemd/monservice.container` (adapter l'image, le port et le volume) :
   ```ini
   [Unit]
   Description=Service pilote

   [Container]
   Image=registre.example.net/organisation/image:1.0
   ReadOnly=true
   DropCapability=all
   NoNewPrivileges=true
   Memory=256m
   PidsLimit=200
   PublishPort=127.0.0.1:8080:8080

   [Service]
   Restart=on-failure

   [Install]
   WantedBy=default.target
   ```
   👉 Explication : applique image épinglée, privilèges réduits, limites et port publié restreint.

3. Recharger systemd utilisateur et démarrer :
   ```bash
   sudo -iu svcpodman systemctl --user daemon-reload
   sudo -iu svcpodman systemctl --user start monservice.service
   ```
   👉 Explication : Quadlet génère l'unité à partir du fichier.

4. Activer le démarrage au boot sans session interactive :
   ```bash
   sudo loginctl enable-linger svcpodman
   ```
   👉 Explication : le lingering permet au gestionnaire user de tourner sans connexion.

## 2. Production — Contrôles

Ajouter `User=`, volumes dédiés et secrets Podman selon l'image.

## 3. Production — Sécurité

- Ne pas utiliser `systemctl enable` sur l'unité générée: Quadlet applique `[Install]`.
- Limiter `PublishPort=` à l'adresse nécessaire.

## Validation et retour arrière

- **Validation** : l'unité démarre.
- **Retour arrière** : `sudo -iu svcpodman systemctl --user stop monservice.service`, supprimer le fichier `.container`, puis `daemon-reload`.

## Si le problème n'est pas résolu

- [Podman — Quadlet et unités systemd](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)
- [Podman — référence CLI](https://docs.podman.io/en/latest/markdown/podman.1.html)
- [Guide complet Podman Quadlet Rocky Linux 9](/02-fiches-completes/rocky-linux/9/installation-deploiement/57-deploiement-podman-quadlet-rocky-linux-9#3-declarer-le-service-quadlet)