---
title: "Fiche Simple - VM Rocky 9 AlmaLinux Inventaire Differences"
description: "Identifier OS, dépôts, release RPM et support avant réemploi d’une procédure Rocky."
published: true
date: 2026-10-29T21:06:58Z
tags: ["rocky9", "almalinux", "rhel", "migration"]
editor: markdown
dateCreated: 2026-10-29T21:06:58Z
dateModified: 2026-10-29T21:06:58Z
---

# Fiche_Simple_-_VM_Rocky_9_AlmaLinux_Inventaire_Differences

- **Environnement** : VM Rocky Linux 9 comme repère documentaire; sujet AlmaLinux
- **OS / Version** : AlmaLinux 8/9 selon la matrice officielle du chemin étudié; contrôles depuis clone Rocky Linux 9
- **Catégorie** : Vie du logiciel / AlmaLinux — Inventorier les différences
- **Tags** : `rocky9`, `almalinux`, `rhel`, `migration`

---

## Problème précis à résoudre

Identifier OS, dépôts, release RPM et support avant réemploi d’une procédure Rocky.

## 1. Hors-Production (Lab / Test / POC)

1. Inventorier les différences :
   ```bash
   cat /etc/os-release
rpm -q almalinux-release rocky-release 2>/dev/null || true
sudo dnf repolist --enabled
sudo dnf history list | head -20
   ```
   👉 Explication : Affiche identité et sources paquets; ne modifie rien.


## 2. Production — Contrôles

Comparer dépôts, clés, errata, cycle de vie et outils AlmaLinux.

## 3. Production — Sécurité

Ne pas remplacer manuellement release RPM, dépôts ou clés; ne pas présumer du support éditeur.

## Validation et retour arrière

- **Validation** : Identité et écarts documentés.
- **Retour arrière** : Aucun changement; quitter.

## Si le problème n'est pas résolu

- [Documentation officielle](https://wiki.almalinux.org/elevate/)
- [Cycle de vie Rocky Linux 9](/01-fiches-simples/rocky-linux/9/vie-du-systeme/cycle-de-vie-50-etapes)