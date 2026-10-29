---
title: "Fiche Simple - VM Rocky 9 Conteneurs Podman Rootless Quadlet"
description: "Déployer un conteneur Podman rootless et le gérer comme un service utilisateur systemd avec Quadlet."
published: true
date: 2026-10-29T18:57:19Z
tags: ["[rocky9]", "[rhel9]", "[podman]", "[rootless]", "[quadlet]", "[systemd]", "[hardening]"]
editor: markdown
dateCreated: 2026-10-29T18:57:19Z
dateModified: 2026-10-29T18:57:19Z
---

# 📄 Fiche_Simple_-_VM_Rocky_9_Conteneurs_Podman_Rootless_Quadlet.md

- **Environnement** : VM Rocky Linux 9
- **OS / Version** : Rocky Linux 9 avec systemd et Podman
- **Catégorie** : Conteneurs / Services
- **Tags** : `[rocky9]`, `[rhel9]`, `[podman]`, `[rootless]`, `[quadlet]`, `[systemd]`, `[hardening]`

## 🎯 Problème précis à résoudre
Déployer un conteneur Podman rootless et le gérer comme un service utilisateur systemd avec Quadlet.

## 🧪 1. Hors-Production (Lab / Test / POC)
1. Installer Podman et vérifier la prise en charge de Quadlet :
   ```bash
   sudo dnf install podman
   podman --version
   ```
2. Créer un fichier utilisateur `~/.config/containers/systemd/web.container` :
   ```ini
   [Unit]
   Description=Conteneur web rootless

   [Container]
   Image=docker.io/library/nginx:alpine
   ContainerName=web
   PublishPort=8080:80

   [Service]
   Restart=on-failure

   [Install]
   WantedBy=default.target
   ```
3. Générer et démarrer l'unité utilisateur :
   ```bash
   systemctl --user daemon-reload
   systemctl --user start web.service
   systemctl --user status web.service --no-pager
   ```
   👉 *Explication : le port 8080 est publié sur l'hôte; le service et le conteneur restent sous le compte courant, sans démon rootful.*

## ⚡ 2. Production — Façon Simplifiée
1. Utiliser un compte nominatif dédié et vérifier qu'il dispose des plages UID/GID nécessaires au mode rootless.
2. Adapter l'image, les volumes et les ports dans le fichier Quadlet, puis lancer :
   ```bash
   systemctl --user daemon-reload
   systemctl --user start web.service
   podman ps
   systemctl --user status web.service --no-pager
   ```
   👉 *Explication : Quadlet génère l'unité à partir du fichier `.container`; la section `[Install]` gère son rattachement à la cible utilisateur lors du rechargement du générateur.*
3. Pour exécuter le service utilisateur après fermeture de session, activer explicitement le linger pour ce compte depuis une session administrateur :
   ```bash
   sudo loginctl enable-linger <compte-podman>
   ```

## 🔒 3. Production — Façon Sécurisée
1. Épingler une version d'image approuvée et contrôler son origine et ses mises à jour.
2. Ne pas monter le socket Podman ou des chemins hôte sensibles dans le conteneur; limiter ports, capacités et volumes aux besoins du service.
3. Garder SELinux en `Enforcing`; ne pas désactiver son étiquetage pour faire fonctionner le conteneur.

## ✅ Validation et retour arrière
- Vérifier le service utilisateur, `podman ps`, les journaux avec `journalctl --user -u web.service` et le test HTTP depuis une source autorisée.
- Pour retirer le déploiement, arrêter/désactiver l'unité, sauvegarder puis retirer le fichier `.container`, puis exécuter `systemctl --user daemon-reload`.
- Ne désactiver le linger qu'après avoir confirmé qu'aucun autre service utilisateur n'en dépend.