---
title: "Fiche Simple - VM Rocky 9 Podman Quadlet Mise A Jour Reprise"
description: "Mettre à jour l'image avec possibilité de retour."
published: true
date: 2026-10-29T20:14:10Z
tags: ["rocky9", "podman", "quadlet", "rootless", "systemd", "update", "rollback"]
editor: markdown
dateCreated: 2026-10-29T20:14:10Z
dateModified: 2026-10-29T20:14:10Z
---

# Fiche_Simple_-_VM_Rocky_9_Podman_Quadlet_Mise_A_Jour_Reprise.md

- **Environnement** : VM Rocky Linux 9 avec Podman rootless, systemd et Quadlet (pilote local)
- **OS / Version** : Rocky Linux 9; Podman des dépôts maintenus
- **Catégorie** : conteneurs / maintenance
- **Tags** : `rocky9`, `podman`, `quadlet`, `rootless`, `systemd`, `update`, `rollback`

---

## Problème précis à résoudre

Mettre à jour l'image avec possibilité de retour.

## 1. Hors-Production (Lab / Test / POC)

1. Récupérer la nouvelle image après recette :
   ```bash
   sudo -iu svcpodman podman pull registre.example.net/organisation/image:1.1
   ```
   👉 Explication : épingler une nouvelle version, garder l'ancienne pour rollback.

2. Modifier `Image=` dans le fichier `.container`, puis redémarrer proprement :
   ```bash
   sudo -iu svcpodman systemctl --user daemon-reload
   sudo -iu svcpodman systemctl --user restart monservice.service
   ```
   👉 Explication : l'unité est régénérée au rechargement.

3. Pour revenir en arrière, remettre l'ancienne valeur de `Image=` puis relancer les mêmes commandes :
   ```bash
   sudo -iu svcpodman systemctl --user restart monservice.service
   ```
   👉 Explication : la version précédente est toujours disponible localement.

## 2. Production — Contrôles

Sauvegarder les données persistantes séparément des couches d'image et tester la restauration; n'utiliser `podman auto-update` que si tags/signatures et fenêtres sont gérés; surveiller consommation et mises à jour de sécurité.

## 3. Production — Sécurité

- Ne jamais utiliser `latest` en production.

## Validation et retour arrière

- **Validation** : version attendue en service et données intactes.
- **Retour arrière** : restaurer l'ancienne version de `Image=` et, si nécessaire, les volumes sauvegardés.

## Si le problème n'est pas résolu

- [Podman — Quadlet et unités systemd](https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html)
- [Podman — référence CLI](https://docs.podman.io/en/latest/markdown/podman.1.html)
- [Guide complet Podman Quadlet Rocky Linux 9](/02-fiches-completes/rocky-linux/9/installation-deploiement/57-deploiement-podman-quadlet-rocky-linux-9#5-mise-a-jour-et-reprise)